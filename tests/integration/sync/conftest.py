"""
Sync-specific pytest fixtures for synchronous integration tests.
"""

from typing import Dict, Any
import pytest


@pytest.fixture(scope="module")
def jwt_token(slurm_cluster) -> str:
    """
    Generate a JWT token for the 'slurm' user using scontrol inside the container.
    """
    compose = slurm_cluster["compose"]

    # Execute scontrol command inside the container to generate JWT token
    result, error, exit_code = compose.exec_in_container(
        ["scontrol", "token", "username=slurm"],
        slurm_cluster["service"],
    )

    if exit_code:
        raise RuntimeError(f"Failed to extract JWT token from scontrol output: {error}")

    # Parse the token from the output
    # Expected output format: "SLURM_JWT=<token>"
    output = result.strip()
    for line in output.split("\n"):
        if line.startswith("SLURM_JWT="):
            return line.split("=", 1)[1]

    raise RuntimeError(f"Failed to extract JWT token from scontrol output: {output}")


@pytest.fixture(scope="module")
def slurm_config(slurm_cluster, jwt_token) -> Dict[str, Any]:
    """
    Provide complete Slurm configuration for sync tests.
    """
    return {"host": slurm_cluster["base_url"], "user": "slurm", "token": jwt_token}
