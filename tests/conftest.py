"""
Shared pytest fixtures for slurpy integration tests.
"""

import time
from contextlib import ExitStack
from pathlib import Path
from typing import Dict, Any
import pytest
from testcontainers.compose import DockerCompose

# Clusters in slurm/docker-compose.yaml. A Slurm release only serves a few API
# versions, so test modules pick one with pytest.mark.slurm_release(...).
SLURM_RELEASES = {
    "24.11": {"services": ["slurm_db", "slurm_node"], "node": "slurm_node"},
    "26.05": {
        "services": ["slurm_db_26_05", "slurm_node_26_05"],
        "node": "slurm_node_26_05",
    },
}
DEFAULT_SLURM_RELEASE = "24.11"


@pytest.fixture(scope="session")
def slurm_clusters():
    """
    Start Slurm clusters using Docker Compose, on first use of each release.

    Returns a function mapping a Slurm release to its connection details.
    """
    compose_dir = Path(__file__).parent.parent / "slurm"
    clusters: Dict[str, Dict[str, Any]] = {}

    with ExitStack() as stack:

        def get_cluster(release: str) -> Dict[str, Any]:
            if release not in clusters:
                services = SLURM_RELEASES[release]["services"]
                node = SLURM_RELEASES[release]["node"]

                compose = DockerCompose(
                    context=str(compose_dir),
                    compose_file_name="docker-compose.yaml",
                    pull=True,
                    build=True,
                    services=services,
                )
                # Registered before starting, so a failed start is still torn down
                stack.callback(compose.stop)
                compose.start()
                # Wait for services to be healthy
                # compose.wait_for("http://localhost:6820")

                # Get the exposed port for the REST API
                rest_api_port = compose.get_service_port(node, 6820)

                # Additional wait to ensure all services are fully ready
                time.sleep(10)

                clusters[release] = {
                    "host": "localhost",
                    "port": rest_api_port,
                    "base_url": f"http://localhost:{rest_api_port}",
                    "compose": compose,
                    "service": node,
                }
            return clusters[release]

        yield get_cluster


@pytest.fixture(scope="module")
def slurm_cluster(request, slurm_clusters):
    """
    Connection details for the Slurm cluster selected by the module's
    slurm_release marker.
    """
    marker = request.node.get_closest_marker("slurm_release")
    release = marker.args[0] if marker else DEFAULT_SLURM_RELEASE
    return slurm_clusters(release)


@pytest.fixture
def sample_job() -> Dict[str, Any]:
    """
    Sample job specification for testing.
    """
    return {
        "script": "#!/bin/bash\nsleep 30\necho 'Job completed'\n",
        "job": {
            "current_working_directory": "/home/slurm",
            "environment": ["PATH=/bin/:/usr/bin/:/sbin/"],
            "name": "test_job",
            "ntasks": 1,
            "time_limit": {"set": True, "number": 300},  # 5 minutes
        },
    }
