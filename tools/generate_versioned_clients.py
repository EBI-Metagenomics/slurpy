#!/usr/bin/env python3
"""
Script to generate version-specific Slurm API clients by filtering OpenAPI operations.

This script:
1. Fetches the OpenAPI specification from a Slurm REST API endpoint
2. Analyzes operation IDs to group them by API version (see VERSIONS)
3. Generates separate Python clients for each version using openapi-generator-cli
4. Uses the --openapi-normalizer FILTER to include only version-specific operations
"""

import argparse
import copy
import json
import logging
import os
import re
import shutil
import subprocess
import sys
from collections import defaultdict
from glob import glob
from pathlib import Path
from typing import Dict, List, Union

import httpx

# A Slurm release only serves a few of these (e.g. 26.05 serves v0042-v0045),
# so use --versions to pick ones served by the cluster you generate from.
VERSIONS = ["v0040", "v0041", "v0042", "v0045"]


class SlurmClientGenerator:
    """Generator for version-specific Slurm API clients."""

    def __init__(
        self,
        api_url: str = "http://localhost:6820/openapi/v3",
        output_dir: Union[str, Path] = ".",
    ):
        self.api_url = api_url
        self.output_dir = Path(output_dir)
        self.spec_data = None
        self.version_operations: Dict[str, List[str]] = defaultdict(list)
        self.version_models: Dict[str, List[str]] = defaultdict(list)
        self.logger = logging.getLogger(__name__)

        # API version patterns to match operations (util_* operations were added in v0044)
        self.version_patterns = {
            version: re.compile(rf"(?:slurm(?:db)?|util)_{version}_")
            for version in VERSIONS
        }

        # Model version patterns to match model names (actual format: v0.0.40_*)
        self.model_patterns = {
            version: re.compile(rf"^v0\.0\.{int(version[1:])}_") for version in VERSIONS
        }

    def fetch_openapi_spec(self) -> Dict:
        """Fetch the OpenAPI specification from the API endpoint."""
        self.logger.info(f"Fetching OpenAPI spec from {self.api_url}")

        try:
            # Set up authorization header if token is available
            headers = {}
            token = os.getenv("X_SLURM_USER_TOKEN")
            if token:
                headers["Authorization"] = f"Bearer {token}"

            with httpx.Client(timeout=30.0) as client:
                response = client.get(self.api_url, headers=headers)
                response.raise_for_status()
                self.spec_data = response.json()
                self.logger.info("✓ Successfully fetched OpenAPI spec")
                return self.spec_data
        except httpx.RequestError as e:
            self.logger.error(f"✗ Failed to fetch OpenAPI spec: {e}")
            sys.exit(1)
        except httpx.HTTPStatusError as e:
            self.logger.error(f"✗ HTTP error fetching OpenAPI spec: {e}")
            sys.exit(1)

    def analyze_operations(self) -> Dict[str, List[str]]:
        """Analyze the OpenAPI spec and group operations and models by version."""
        if not self.spec_data:
            self.fetch_openapi_spec()

        self.logger.info("Analyzing operations by version...")

        # Extract all operation IDs from paths
        operation_ids = set()
        if "paths" in self.spec_data:
            for path, methods in self.spec_data["paths"].items():
                for method, operation in methods.items():
                    if isinstance(operation, dict) and "operationId" in operation:
                        operation_ids.add(operation["operationId"])

        # Group operations by version
        for operation_id in operation_ids:
            for version, pattern in self.version_patterns.items():
                if pattern.match(operation_id):
                    self.version_operations[version].append(operation_id)
                    break

        # Also extract models
        self.extract_models_by_version()

        # Log combined summary
        self.logger.info("Analysis Summary:")
        for version in sorted(
            set(self.version_operations.keys()) | set(self.version_models.keys())
        ):
            ops_count = len(self.version_operations.get(version, []))
            models_count = len(self.version_models.get(version, []))
            self.logger.info(
                f"  {version}: {ops_count} operations, {models_count} models"
            )

        return dict(self.version_operations)

    def extract_models_by_version(self) -> Dict[str, List[str]]:
        """Extract and group model names by version from the OpenAPI spec."""
        if not self.spec_data:
            self.fetch_openapi_spec()

        self.logger.info("Extracting models by version...")

        # Extract all model names from components/schemas
        model_names = set()
        if "components" in self.spec_data and "schemas" in self.spec_data["components"]:
            model_names = set(self.spec_data["components"]["schemas"].keys())

        self.logger.debug(f"Found {len(model_names)} total models in spec")
        if model_names:
            sample_models = list(model_names)[:5]
            self.logger.debug(f"Sample model names: {sample_models}")

        # Group models by version
        for model_name in model_names:
            for version, pattern in self.model_patterns.items():
                if pattern.match(model_name):
                    self.version_models[version].append(model_name)
                    self.logger.debug(f"Matched {model_name} to {version}")
                    break

        # Log summary
        self.logger.info("Found models:")
        for version, models in self.version_models.items():
            self.logger.info(f"  {version}: {len(models)} models")
            if models:
                self.logger.info(f"    Sample: {models[:3]}")

        return dict(self.version_models)

    def _capitalize_model_name(self, name: str) -> str:
        """Convert snake_case model name to PascalCase for proper class naming."""
        # Split by underscores and capitalize each part
        parts = name.split("_")
        # Capitalize each part, handling special cases
        capitalized_parts = []
        for part in parts:
            if part.lower() in ["api", "http", "url", "json", "xml", "id"]:
                # Keep certain acronyms uppercase
                capitalized_parts.append(part.upper())
            elif part.lower() == "openapi":
                capitalized_parts.append("OpenAPI")
            else:
                capitalized_parts.append(part.capitalize())
        return "".join(capitalized_parts)

    def create_filtered_spec(self, version: str, operations: List[str]) -> str:
        """Create a filtered OpenAPI spec containing only operations and models for the specified version."""
        if not self.spec_data:
            self.fetch_openapi_spec()

        # Deep copy the spec
        filtered_spec = copy.deepcopy(self.spec_data)

        # Filter paths to only include version-specific operations
        if "paths" in filtered_spec:
            original_paths = filtered_spec["paths"]
            filtered_paths = {}
            operation_set = set(operations)

            for path, path_methods in original_paths.items():
                filtered_path_methods = {}
                for method, operation_spec in path_methods.items():
                    if (
                        isinstance(operation_spec, dict)
                        and "operationId" in operation_spec
                    ):
                        if operation_spec["operationId"] in operation_set:
                            filtered_path_methods[method] = operation_spec

                # Only include the path if it has operations for this version
                if filtered_path_methods:
                    filtered_paths[path] = filtered_path_methods

            filtered_spec["paths"] = filtered_paths
            self.logger.debug(
                f"Filtered spec from {len(original_paths)} to {len(filtered_paths)} paths for {version}"
            )

        # Find and keep only models that are actually needed by the filtered operations
        required_models = self._find_required_models(filtered_spec, version)

        # Store required models for use in model mappings
        self.version_required_models = getattr(self, "version_required_models", {})
        self.version_required_models[version] = required_models

        # Filter components/schemas to only include required models
        if "components" in filtered_spec and "schemas" in filtered_spec["components"]:
            original_schemas = filtered_spec["components"]["schemas"]
            filtered_schemas = {}

            for model_name in required_models:
                if model_name in original_schemas:
                    filtered_schemas[model_name] = original_schemas[model_name]

            filtered_spec["components"]["schemas"] = filtered_schemas
            self.logger.debug(
                f"Filtered models from {len(original_schemas)} to {len(filtered_schemas)} for {version}"
            )
        else:
            self.logger.debug("No models to filter")

        # Write filtered spec to a temporary file
        filtered_spec_path = self.output_dir / f"filtered_spec_{version}.json"
        # Ensure parent directory exists
        filtered_spec_path.parent.mkdir(parents=True, exist_ok=True)
        with open(filtered_spec_path, "w") as f:
            json.dump(filtered_spec, f, indent=2)

        self.logger.debug(f"Created filtered spec at {filtered_spec_path}")
        return str(filtered_spec_path)

    def _find_required_models(self, spec: dict, version: str) -> set:
        """Find all models required by the filtered operations through dependency analysis."""
        required_models = set()

        # Step 1: Find models directly referenced by operations
        if "paths" in spec:
            for path, path_methods in spec["paths"].items():
                for method, operation_spec in path_methods.items():
                    if isinstance(operation_spec, dict):
                        # Check responses
                        if "responses" in operation_spec:
                            for response_code, response_spec in operation_spec[
                                "responses"
                            ].items():
                                self._extract_model_refs(response_spec, required_models)

                        # Check request bodies
                        if "requestBody" in operation_spec:
                            self._extract_model_refs(
                                operation_spec["requestBody"], required_models
                            )

                        # Check parameters
                        if "parameters" in operation_spec:
                            for param in operation_spec["parameters"]:
                                self._extract_model_refs(param, required_models)

        # Step 2: Recursively find model dependencies
        all_schemas = spec.get("components", {}).get("schemas", {})
        self._find_model_dependencies(required_models, all_schemas, version)

        self.logger.debug(f"Found {len(required_models)} required models for {version}")
        if required_models:
            sample_models = list(required_models)[:5]
            self.logger.debug(f"Sample required models: {sample_models}")

            # Debug: Show which models have version prefixes
            versioned_models = [m for m in required_models if m.startswith("v0.0.")]
            unversioned_models = [
                m for m in required_models if not m.startswith("v0.0.")
            ]
            self.logger.debug(
                f"{len(versioned_models)} versioned models, {len(unversioned_models)} unversioned models"
            )
            if versioned_models:
                self.logger.debug(f"Sample versioned models: {versioned_models[:3]}")

        return required_models

    def _extract_model_refs(self, obj: dict, model_refs: set) -> None:
        """Recursively extract $ref model references from an OpenAPI object."""
        if isinstance(obj, dict):
            if "$ref" in obj:
                ref = obj["$ref"]
                if ref.startswith("#/components/schemas/"):
                    model_name = ref.split("/")[-1]
                    model_refs.add(model_name)
            else:
                for value in obj.values():
                    self._extract_model_refs(value, model_refs)
        elif isinstance(obj, list):
            for item in obj:
                self._extract_model_refs(item, model_refs)

    def _find_model_dependencies(
        self, required_models: set, all_schemas: dict, version: str
    ) -> None:
        """Recursively find dependencies of required models."""
        models_to_process = required_models.copy()
        processed_models = set()

        while models_to_process:
            model_name = models_to_process.pop()
            if model_name in processed_models or model_name not in all_schemas:
                continue

            processed_models.add(model_name)
            model_schema = all_schemas[model_name]

            # Find references in this model
            model_deps = set()
            self._extract_model_refs(model_schema, model_deps)

            # Add new dependencies to process and required sets
            new_deps = model_deps - required_models
            models_to_process.update(new_deps)
            required_models.update(model_deps)

        # Filter out models from other versions
        version_number = version[-4:]  # Extract 0040, 0041, 0042
        actual_version = str(int(version_number))
        current_version_prefix = f"v0.0.{actual_version}_"

        # Remove models from other versions, but keep unversioned models
        filtered_models = set()
        for model in required_models:
            # Keep if: unversioned OR matches current version
            if not model.startswith("v0.0.") or model.startswith(
                current_version_prefix
            ):
                filtered_models.add(model)
            else:
                self.logger.debug(f"Excluding cross-version model: {model}")

        required_models.clear()
        required_models.update(filtered_models)

    def generate_operation_mappings(self, operations: List[str], version: str) -> str:
        """Generate operation ID mappings to remove version prefixes."""
        mappings = []

        for operation_id in operations:
            # Remove version prefix: slurm_v0040_get_jobs -> get_jobs, slurmdb_v0040_get_accounts -> get_accounts
            version_code = version[-4:]  # Extract 0040, 0041, 0042
            if f"_v{version_code}_" in operation_id:
                clean_name = re.sub(
                    rf"^(?:slurm(?:db)?|util)_v{version_code}_", "", operation_id
                )
                mappings.append(f"{operation_id}={clean_name}")

        return ",".join(mappings) if mappings else ""

    def generate_model_mappings(self, models: List[str], version: str) -> str:
        """Generate model name mappings to remove version prefixes."""
        mappings = []

        self.logger.debug(f"Processing {len(models)} models for mappings")

        # Debug: Show which models we're processing
        versioned_input_models = [m for m in models if m.startswith("v0.0.")]
        self.logger.debug(f"Input has {len(versioned_input_models)} versioned models")
        if versioned_input_models:
            self.logger.debug(
                f"Sample versioned input models: {versioned_input_models[:3]}"
            )

        for model_name in models:
            # Check if this model has ANY version prefix pattern (v0.0.XX_)
            if model_name.startswith("v0.0.") and "_" in model_name:
                # Find the version prefix (e.g., "v0.0.40_", "v0.0.41_")
                prefix_end = model_name.find("_", 5)  # Start searching after "v0.0."
                if prefix_end != -1:
                    clean_name = model_name[prefix_end + 1 :]  # Remove vX.X.XX_ prefix

                    # Capitalize the first letter for proper class names: assoc_max -> AssocMax
                    capitalized_name = self._capitalize_model_name(clean_name)
                    mappings.append(f"{model_name}={capitalized_name}")
                    self.logger.debug(
                        f"Model mapping: {model_name} -> {capitalized_name}"
                    )
                else:
                    self.logger.debug(
                        f"Versioned model has no underscore: {model_name}"
                    )
            else:
                if model_name.startswith("v0.0."):
                    self.logger.debug(
                        f"Versioned model has no underscore: {model_name}"
                    )

        self.logger.debug(f"Generated {len(mappings)} model mappings")
        if mappings:
            self.logger.debug(f"First few mappings: {mappings[:3]}")
        return ",".join(mappings) if mappings else ""

    def generate_client_command(
        self, as_async: bool, version: str, operations: List[str]
    ) -> List[str]:
        """Generate the openapi-generator-cli command for a specific version."""
        if not operations:
            self.logger.warning(f"No operations found for {version}, skipping...")
            return []

        if as_async:
            package_name = f"slurpy.{version}.asyncio"
        else:
            package_name = f"slurpy.{version}"

        version_output_dir = self.output_dir

        # Create filtered spec with only operations and models for this version
        filtered_spec_path = self.create_filtered_spec(version, operations)

        # Generate operation and model mappings to remove version prefixes
        operation_mappings = self.generate_operation_mappings(operations, version)
        # Use actual required models from dependency analysis, not pattern-matched models
        required_models = getattr(self, "version_required_models", {}).get(version, [])
        model_mappings = self.generate_model_mappings(list(required_models), version)

        # Debug output
        self.logger.debug(f"Found {len(required_models)} required models for {version}")
        if required_models:
            self.logger.debug(f"Sample required models: {list(required_models)[:5]}")
        self.logger.debug(
            f"Model mappings: {model_mappings[:100]}{'...' if len(model_mappings) > 100 else ''}"
        )

        command = [
            "poetry",
            "run",
            "openapi-generator-cli",
            "generate",
            "-i",
            filtered_spec_path,  # Use filtered spec
            "-g",
            "python",
            "-o",
            str(version_output_dir),
            "--global-property",
            "modelDocs=false,modelTests=false",
            "--additional-properties",
            f"packageName={package_name},generateSourceCodeOnly=true",
        ]

        if as_async:
            command.extend(["--library", "asyncio"])

        # Add operation ID mappings if any exist
        if operation_mappings:
            command.extend(["--operation-id-name-mappings", operation_mappings])

        # Add model name mappings if any exist
        if model_mappings:
            command.extend(["--model-name-mappings", model_mappings])
            self.logger.debug(
                f"Added model mappings to command: {model_mappings[:200]}{'...' if len(model_mappings) > 200 else ''}"
            )
        else:
            self.logger.debug("No model mappings to add to command")

        return command

    def execute_generation(
        self, as_async: bool, version: str, operations: List[str]
    ) -> bool:
        """Execute the client generation for a specific version."""
        command = self.generate_client_command(as_async, version, operations)
        if not command:
            return False

        self.logger.info(f"\n🔄 Generating {version} client...")
        self.logger.debug(f"Command: {' '.join(command)}")

        try:
            # Create output directory if it doesn't exist
            version_output_dir = self.output_dir
            version_output_dir.mkdir(parents=True, exist_ok=True)

            # Execute the command
            result = subprocess.run(
                command, capture_output=True, text=True, timeout=300
            )

            if result.returncode == 0:
                self.logger.info(
                    f"✓ Successfully generated {version} {'async' if as_async else 'sync'} client in {version_output_dir}/"
                )
                return True
            else:
                self.logger.error(
                    f"✗ Failed to generate {version} {'async' if as_async else 'sync'} client:"
                )
                self.logger.error(f"stdout: {result.stdout}")
                self.logger.error(f"stderr: {result.stderr}")
                return False

        except subprocess.TimeoutExpired:
            self.logger.error(f"✗ Generation timed out for {version}")
            return False
        except Exception as e:
            self.logger.error(f"✗ Error generating {version} client: {e}")
            return False

    def generate_all_clients(self) -> bool:
        """Generate all version-specific clients."""
        if not self.version_operations:
            self.analyze_operations()

        success_count = 0
        total_versions = len(self.version_operations) * 2

        # Async client
        for version, operations in self.version_operations.items():
            if self.execute_generation(True, version, operations):
                success_count += 1

        # Sync client
        for version, operations in self.version_operations.items():
            if self.execute_generation(False, version, operations):
                success_count += 1

        self.logger.info("📊 Generation Summary:")
        self.logger.info(
            f"✓ {success_count}/{total_versions} version clients generated successfully"
        )

        return success_count == total_versions

    def cleanup(self):
        """Clean up generated temporary files and directories."""

        self.logger.info("🧹 Cleaning up generated files...")

        # Remove filtered spec files using glob pattern
        spec_pattern = str(self.output_dir / "filtered_spec_*.json")
        spec_files = glob(spec_pattern)

        removed_count = 0
        for spec_file in spec_files:
            try:
                Path(spec_file).unlink()
                self.logger.debug(f"✓ Removed {spec_file}")
                removed_count += 1
            except FileNotFoundError:
                pass  # File already doesn't exist
            except Exception as e:
                self.logger.warning(f"⚠ Could not remove {spec_file}: {e}")

        # Remove .openapi-generator directory
        openapi_gen_dir = self.output_dir / ".openapi-generator"
        if openapi_gen_dir.exists():
            try:
                shutil.rmtree(openapi_gen_dir)
                self.logger.debug(f"✓ Removed {openapi_gen_dir}")
                removed_count += 1
            except Exception as e:
                self.logger.warning(f"⚠ Could not remove {openapi_gen_dir}: {e}")

        if removed_count > 0:
            self.logger.info(f"🧹 Cleanup completed - removed {removed_count} items")
        else:
            self.logger.info("🧹 Cleanup completed - no files to remove")


def main():
    """Main entry point."""

    parser = argparse.ArgumentParser(
        description="Generate version-specific Slurm API clients"
    )
    parser.add_argument(
        "--api-url",
        default="http://localhost:6820/openapi/v3",
        help="URL to the Slurm OpenAPI specification (default: http://localhost:6820/openapi/v3)",
    )
    parser.add_argument(
        "--versions",
        nargs="+",
        choices=VERSIONS,
        help="Only generate clients for specified versions",
    )
    parser.add_argument(
        "--output-dir",
        default=".",
        help="Output directory for generated clients (default: current directory)",
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Set the logging level (default: INFO)",
    )

    args = parser.parse_args()

    # Configure logging
    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="%(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Initialize generator
    generator = SlurmClientGenerator(args.api_url, args.output_dir)

    # Analyze operations
    version_operations = generator.analyze_operations()

    if not version_operations:
        generator.logger.error("✗ No versioned operations found in the OpenAPI spec")
        sys.exit(1)

    # Filter versions if specified
    if args.versions:
        filtered_operations = {
            v: ops for v, ops in version_operations.items() if v in args.versions
        }
        generator.version_operations = filtered_operations

    # Generate clients
    success = generator.generate_all_clients()
    generator.cleanup()

    if success:
        generator.logger.info("🎉 All version-specific clients generated successfully!")
        generator.logger.info("Next steps:")
        generator.logger.info(
            f"1. Review the generated clients in {args.output_dir}/v00X directories"
        )
        generator.logger.info("2. Test the clients with your Slurm cluster")
        generator.logger.info(
            "3. Update your main package to use version-specific imports"
        )
    else:
        generator.logger.error(
            "❌ Some client generations failed. Check the output above for details."
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
