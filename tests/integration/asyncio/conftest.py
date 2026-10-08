"""
Async-specific pytest fixtures for asyncio integration tests.
"""

import asyncio
from typing import Dict, Any
import pytest
import pytest_asyncio


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="module")
async def jwt_token(slurm_cluster) -> str:
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


@pytest_asyncio.fixture(scope="module")
async def slurm_config(slurm_cluster, jwt_token) -> Dict[str, Any]:
    """
    Provide complete Slurm configuration for async tests.
    """
    return {"host": slurm_cluster["base_url"], "user": "slurm", "token": jwt_token}
