"""
Integration tests for Slurm API v0045.
"""

import pytest
import pytest_asyncio
from typing import Dict, Any, Optional

import slurpy.v0045.asyncio as slurpy
from slurpy.v0045.asyncio.rest import ApiException

pytestmark = pytest.mark.slurm_release("26.05")


@pytest_asyncio.fixture
async def api_client(slurm_config: Dict[str, Any]):
    """Create an authenticated API client for v0045."""
    configuration = slurpy.Configuration(host=slurm_config["host"])

    # Configure authentication
    configuration.api_key["user"] = slurm_config["user"]
    configuration.api_key["token"] = slurm_config["token"]

    async with slurpy.ApiClient(configuration) as client:
        yield slurpy.SlurmApi(client)


@pytest.mark.asyncio
class TestSlurmV0045:
    """Integration tests for Slurm REST API v0045."""

    async def test_ping_cluster(self, api_client: slurpy.SlurmApi):
        """Test basic connectivity to the Slurm cluster."""
        try:
            response = await api_client.get_ping()
            assert response is not None
            # Check if we get a valid ping response
            ping_data = response.to_dict()
            assert "pings" in ping_data or "ping" in ping_data
        except ApiException as e:
            pytest.fail(f"Failed to ping cluster: {e}")

    async def test_list_jobs(self, api_client: slurpy.SlurmApi):
        """Test listing jobs."""
        try:
            response = await api_client.get_jobs()
            assert response is not None
            jobs_data = response.to_dict()
            assert "jobs" in jobs_data
            # Should return a list (could be empty)
            assert isinstance(jobs_data["jobs"], list)
        except ApiException as e:
            pytest.fail(f"Failed to list jobs: {e}")

    async def test_create_job(
        self, api_client: slurpy.SlurmApi, sample_job: Dict[str, Any]
    ):
        """Test creating a job."""
        job_created_id: Optional[int] = None

        try:
            # Create job submission request
            job_request = slurpy.JobSubmitReq.from_dict(sample_job)

            response = await api_client.post_job_submit(job_submit_req=job_request)

            assert response is not None
            submit_data = response.to_dict()

            # Extract job ID from response
            if "job_id" in submit_data:
                job_created_id = submit_data["job_id"]
            elif "jobs" in submit_data and len(submit_data["jobs"]) > 0:
                job_created_id = submit_data["jobs"][0].get("job_id")

            assert job_created_id is not None, "Job ID not found in response"

        except ApiException as e:
            pytest.fail(f"Failed to create job: {e}")

        finally:
            # Clean up: try to cancel the job if it was created
            if job_created_id:
                try:
                    await api_client.delete_job(str(job_created_id))
                except ApiException:
                    # Job might have already completed or failed, ignore cleanup errors
                    pass

    async def test_get_single_job(
        self, api_client: slurpy.SlurmApi, sample_job: Dict[str, Any]
    ):
        """Test getting details for a single job."""
        job_created_id: Optional[int] = None

        try:
            # First create a job
            job_request = slurpy.JobSubmitReq.from_dict(sample_job)

            submit_response = await api_client.post_job_submit(
                job_submit_req=job_request
            )

            submit_data = submit_response.to_dict()

            # Extract job ID
            if "job_id" in submit_data:
                job_created_id = submit_data["job_id"]
            elif "jobs" in submit_data and len(submit_data["jobs"]) > 0:
                job_created_id = submit_data["jobs"][0].get("job_id")

            assert job_created_id is not None, "Job ID not found in submit response"

            # Now get the job details
            job_response = await api_client.get_job(job_id=str(job_created_id))
            assert job_response is not None

            job_data = job_response.to_dict()
            assert "jobs" in job_data
            assert len(job_data["jobs"]) > 0

            job_info = job_data["jobs"][0]
            assert job_info["job_id"] == job_created_id
            assert job_info["name"] == sample_job["job"]["name"]

        except ApiException as e:
            pytest.fail(f"Failed to get single job: {e}")

        finally:
            # Clean up
            if job_created_id:
                try:
                    await api_client.delete_job(str(job_created_id))
                except ApiException:
                    pass

    async def test_delete_job(
        self, api_client: slurpy.SlurmApi, sample_job: Dict[str, Any]
    ):
        """Test deleting/canceling a job."""
        job_created_id: Optional[int] = None

        try:
            # First create a job
            job_request = slurpy.JobSubmitReq.from_dict(sample_job)

            submit_response = await api_client.post_job_submit(
                job_submit_req=job_request
            )

            submit_data = submit_response.to_dict()

            # Extract job ID
            if "job_id" in submit_data:
                job_created_id = submit_data["job_id"]
            elif "jobs" in submit_data and len(submit_data["jobs"]) > 0:
                job_created_id = submit_data["jobs"][0].get("job_id")

            assert job_created_id is not None, "Job ID not found in submit response"

            # Now delete the job
            delete_response = await api_client.delete_job(str(job_created_id))
            assert delete_response is not None

            # Verify the job was cancelled/deleted
            # The delete response should indicate success
            # Different versions might return different response structures
            # Just ensure we got a response without exception

        except ApiException as e:
            pytest.fail(f"Failed to delete job: {e}")

    async def test_hostlist_conversion(self, api_client: slurpy.SlurmApi):
        """Test converting between hostlist expressions and host names."""
        util_api = slurpy.UtilApi(api_client.api_client)
        try:
            hostnames_response = await util_api.post_hostnames(
                slurpy.OpenAPIHostlistReqResp(hostlist="node[1-3]")
            )
            assert hostnames_response.hostnames == ["node1", "node2", "node3"]

            hostlist_response = await util_api.post_hostlist(
                slurpy.OpenAPIHostnamesReqResp(hostnames=hostnames_response.hostnames)
            )
            assert hostlist_response.hostlist == "node[1-3]"
        except ApiException as e:
            pytest.fail(f"Failed to convert hostlist: {e}")
