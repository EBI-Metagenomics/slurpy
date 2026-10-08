# Slurpy (SLUrm Rest api PYthon client)

Slurpy is a Python client for the [Slurm REST API](https://slurm.schedmd.com/rest.html).
Slurm is an open-source job scheduler for high performance compute environments.
Its REST API is a set of HTTP endpoints for submitting, monitoring, and managing compute jobs.
This Python client is a convenience library for interacting with that API.

## Features

- ✨ **Multiple API versions** - Support for Slurm REST API v0.0.40, v0.0.41, v0.0.42, and v0.0.45
- 🔐 **JWT Authentication** - Built-in support for Slurm JWT token authentication
- 🚀 **Sync & Async** - Both synchronous and asynchronous client support
- 🐍 **Type Hints** - Complete type annotations for better IDE support
- 🧪 **Well Tested** - Comprehensive integration tests with real Slurm clusters
- 📦 **Easy Installation** - Simple pip installation with minimal dependencies

## Installation

```bash
pip install ebi-slurpy
```

## Quick Start

Slurpy supports both **synchronous** and **asynchronous** clients. Choose the one that fits your application:

### Synchronous Client

```python
import slurpy.v0040 as slurpy

# Configure the client
configuration = slurpy.Configuration(
    host="http://your-slurm-rest-api:6820"
)

# Set up authentication
configuration.api_key['user'] = "your-username"
configuration.api_key['token'] = "your-jwt-token"

# Create API client
with slurpy.ApiClient(configuration) as client:
    api = slurpy.SlurmApi(client)
    
    # Test connectivity
    response = api.get_ping()
    print(f"Cluster status: {response.to_dict()}")
    
    # List all jobs
    jobs_response = api.get_jobs()
    jobs = jobs_response.to_dict()
    print(f"Found {len(jobs['jobs'])} jobs")
```

### Asynchronous Client

```python
import asyncio
import slurpy.v0040.asyncio as slurpy

async def main():
    # Configure the client
    configuration = slurpy.Configuration(
        host="http://your-slurm-rest-api:6820"
    )
    
    # Set up authentication
    configuration.api_key['user'] = "your-username"
    configuration.api_key['token'] = "your-jwt-token"
    
    # Create API client
    async with slurpy.ApiClient(configuration) as client:
        api = slurpy.SlurmApi(client)
        
        # Test connectivity
        response = await api.get_ping()
        print(f"Cluster status: {response.to_dict()}")
        
        # List all jobs
        jobs_response = await api.get_jobs()
        jobs = jobs_response.to_dict()
        print(f"Found {len(jobs['jobs'])} jobs")

if __name__ == "__main__":
    asyncio.run(main())
```

### Environment Variables

You can use environment variables for configuration with both sync and async clients:

**Sync version:**
```python
import os
import slurpy.v0040 as slurpy

configuration = slurpy.Configuration(
    host=os.getenv("SLURM_REST_URL", "http://localhost:6820")
)

configuration.api_key['user'] = os.getenv("SLURM_USER_NAME")
configuration.api_key['token'] = os.getenv("SLURM_USER_TOKEN")
```

**Async version:**
```python
import os
import slurpy.v0040.asyncio as slurpy

configuration = slurpy.Configuration(
    host=os.getenv("SLURM_REST_URL", "http://localhost:6820")
)

configuration.api_key['user'] = os.getenv("SLURM_USER_NAME")
configuration.api_key['token'] = os.getenv("SLURM_USER_TOKEN")
```

## API Versions

Slurpy supports multiple Slurm REST API versions, each available in both sync and async variants.
Use a version that your Slurm cluster serves:

| API version | Served by Slurm |
|-------------|-----------------|
| v0.0.40 | 23.11 – 25.05 |
| v0.0.41 | 24.05 – 25.11 |
| v0.0.42 | 24.11 – 26.05 |
| v0.0.45 | 26.05 |

### v0.0.40
```python
# Synchronous
import slurpy.v0040 as slurpy

# Asynchronous  
import slurpy.v0040.asyncio as slurpy
```

### v0.0.41
```python
# Synchronous
import slurpy.v0041 as slurpy

# Asynchronous
import slurpy.v0041.asyncio as slurpy
```

### v0.0.42
```python
# Synchronous
import slurpy.v0042 as slurpy

# Asynchronous
import slurpy.v0042.asyncio as slurpy
```

### v0.0.45
```python
# Synchronous
import slurpy.v0045 as slurpy

# Asynchronous
import slurpy.v0045.asyncio as slurpy
```

v0.0.45 also has a `UtilApi`, for converting between hostlist expressions and host names:

```python
util = slurpy.UtilApi(client)
response = util.post_hostnames(slurpy.OpenAPIHostlistReqResp(hostlist="node[1-3]"))
print(response.hostnames)  # ['node1', 'node2', 'node3']
```

> **Note:** The API interface is consistent across versions and between sync/async variants, but some features and response formats may differ between Slurm versions. Check the Slurm documentation for version-specific differences.

## Common Operations

### List Jobs

**Sync version:**
```python
def list_jobs():
    with slurpy.ApiClient(configuration) as client:
        api = slurpy.SlurmApi(client)
        
        response = api.get_jobs()
        jobs = response.to_dict()
        
        for job in jobs['jobs']:
            print(f"Job {job['job_id']}: {job['name']} ({job['job_state']})")
```

**Async version:**
```python
async def list_jobs():
    async with slurpy.ApiClient(configuration) as client:
        api = slurpy.SlurmApi(client)
        
        response = await api.get_jobs()
        jobs = response.to_dict()
        
        for job in jobs['jobs']:
            print(f"Job {job['job_id']}: {job['name']} ({job['job_state']})")
```

### Submit a Job

**Sync version:**
```python
def submit_job():
    job_spec = {
        "script": "#!/bin/bash\\nsleep 60\\necho 'Job completed'",
        "job": {
            "name": "my_job",
            "current_working_directory": "/home/user",
            "environment": ["PATH=/bin:/usr/bin"],
            "ntasks": 1,
            "time_limit": {"set": True, "number": 300},  # 5 minutes
        }
    }
    
    with slurpy.ApiClient(configuration) as client:
        api = slurpy.SlurmApi(client)
        
        job_request = slurpy.JobSubmitReq.from_dict(job_spec)
        response = api.post_job_submit(job_submit_req=job_request)
        
        result = response.to_dict()
        print(f"Job submitted with ID: {result['job_id']}")
```

**Async version:**
```python
async def submit_job():
    job_spec = {
        "script": "#!/bin/bash\\nsleep 60\\necho 'Job completed'",
        "job": {
            "name": "my_job",
            "current_working_directory": "/home/user",
            "environment": ["PATH=/bin:/usr/bin"],
            "ntasks": 1,
            "time_limit": {"set": True, "number": 300},  # 5 minutes
        }
    }
    
    async with slurpy.ApiClient(configuration) as client:
        api = slurpy.SlurmApi(client)
        
        job_request = slurpy.JobSubmitReq.from_dict(job_spec)
        response = await api.post_job_submit(job_submit_req=job_request)
        
        result = response.to_dict()
        print(f"Job submitted with ID: {result['job_id']}")
```

### Get Job Details

**Sync version:**
```python
def get_job(job_id: str):
    with slurpy.ApiClient(configuration) as client:
        api = slurpy.SlurmApi(client)
        
        response = api.get_job(job_id=job_id)
        job = response.to_dict()
        
        print(f"Job {job_id} status: {job['jobs'][0]['job_state']}")
```

**Async version:**
```python
async def get_job(job_id: str):
    async with slurpy.ApiClient(configuration) as client:
        api = slurpy.SlurmApi(client)
        
        response = await api.get_job(job_id=job_id)
        job = response.to_dict()
        
        print(f"Job {job_id} status: {job['jobs'][0]['job_state']}")
```

### Cancel a Job

**Sync version:**
```python
def cancel_job(job_id: str):
    with slurpy.ApiClient(configuration) as client:
        api = slurpy.SlurmApi(client)
        
        response = api.delete_job(job_id)
        print(f"Job {job_id} cancellation requested")
```

**Async version:**
```python
async def cancel_job(job_id: str):
    async with slurpy.ApiClient(configuration) as client:
        api = slurpy.SlurmApi(client)
        
        response = await api.delete_job(job_id)
        print(f"Job {job_id} cancellation requested")
```

## Error Handling

Error handling works the same for both sync and async clients:

**Sync version:**
```python
from slurpy.v0040.rest import ApiException

def robust_job_operation():
    try:
        with slurpy.ApiClient(configuration) as client:
            api = slurpy.SlurmApi(client)
            response = api.get_jobs()
            return response.to_dict()
            
    except ApiException as e:
        print(f"API Error: {e.status} - {e.reason}")
        print(f"Response body: {e.body}")
        
    except Exception as e:
        print(f"Unexpected error: {e}")
```

**Async version:**
```python
from slurpy.v0040.asyncio.rest import ApiException

async def robust_job_operation():
    try:
        async with slurpy.ApiClient(configuration) as client:
            api = slurpy.SlurmApi(client)
            response = await api.get_jobs()
            return response.to_dict()
            
    except ApiException as e:
        print(f"API Error: {e.status} - {e.reason}")
        print(f"Response body: {e.body}")
        
    except Exception as e:
        print(f"Unexpected error: {e}")
```

## Configuration Options

### SSL/TLS Configuration

```python
configuration = slurpy.Configuration(
    host="https://secure-slurm-api:6820",
    ssl_ca_cert="/path/to/ca-cert.pem",  # CA certificate
    cert_file="/path/to/client-cert.pem",  # Client certificate
    key_file="/path/to/client-key.pem",   # Client private key
    verify_ssl=True
)
```

## Complete Example

Here's a complete workflow example available in both sync and async versions:

### Synchronous Version

```python
#!/usr/bin/env python3
import os
from typing import Optional

import slurpy.v0040 as slurpy
from slurpy.v0040.rest import ApiException


def slurm_workflow():
    """Complete workflow: ping, submit job, monitor, cleanup."""
    
    # Configuration
    configuration = slurpy.Configuration(
        host=os.getenv("SLURM_REST_URL", "http://localhost:6820")
    )
    configuration.api_key['user'] = os.getenv("SLURM_USER_NAME", "slurm")
    configuration.api_key['token'] = os.getenv("SLURM_USER_TOKEN")
    
    if not configuration.api_key['token']:
        print("Error: SLURM_USER_TOKEN environment variable is required")
        return
    
    job_id: Optional[str] = None
    
    try:
        with slurpy.ApiClient(configuration) as client:
            api = slurpy.SlurmApi(client)
            
            # 1. Test connectivity
            print("🔍 Testing cluster connectivity...")
            ping_response = api.get_ping()
            print(f"✅ Cluster is responsive: {ping_response.to_dict()}")
            
            # 2. Submit a job
            print("\\n📤 Submitting job...")
            job_spec = {
                "script": "#!/bin/bash\\nsleep 30\\necho 'Hello from Slurm!'",
                "job": {
                    "name": "slurpy_demo",
                    "current_working_directory": "/tmp",
                    "environment": ["PATH=/bin:/usr/bin"],
                    "ntasks": 1,
                    "time_limit": {"set": True, "number": 120},
                }
            }
            
            job_request = slurpy.JobSubmitReq.from_dict(job_spec)
            submit_response = api.post_job_submit(job_submit_req=job_request)
            result = submit_response.to_dict()
            job_id = str(result['job_id'])
            print(f"✅ Job submitted successfully with ID: {job_id}")
            
            # 3. Monitor job
            print(f"\\n👀 Monitoring job {job_id}...")
            job_response = api.get_job(job_id=job_id)
            job_data = job_response.to_dict()
            job_info = job_data['jobs'][0]
            print(f"📊 Job status: {job_info['job_state']}")
            print(f"📋 Job details: {job_info['name']} on {job_info.get('nodes', 'pending')}")
            
            # 4. List all current jobs
            print("\\n📋 Current cluster jobs:")
            jobs_response = api.get_jobs()
            jobs = jobs_response.to_dict()
            print(f"Found {len(jobs['jobs'])} total jobs in the cluster")
            
    except ApiException as e:
        print(f"❌ Slurm API error: {e.status} - {e.reason}")
        if e.body:
            print(f"Response: {e.body}")
            
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        
    finally:
        # Cleanup: Cancel the job if it was created
        if job_id:
            try:
                with slurpy.ApiClient(configuration) as client:
                    api = slurpy.SlurmApi(client)
                    api.delete_job(job_id)
                    print(f"\\n🧹 Cleanup: Job {job_id} cancellation requested")
            except Exception as cleanup_error:
                print(f"⚠️ Cleanup warning: Could not cancel job {job_id}: {cleanup_error}")


if __name__ == "__main__":
    slurm_workflow()
```

### Asynchronous Version

```python
#!/usr/bin/env python3
import asyncio
import os
from typing import Optional

import slurpy.v0040.asyncio as slurpy
from slurpy.v0040.asyncio.rest import ApiException


async def slurm_workflow():
    """Complete workflow: ping, submit job, monitor, cleanup."""
    
    # Configuration
    configuration = slurpy.Configuration(
        host=os.getenv("SLURM_REST_URL", "http://localhost:6820")
    )
    configuration.api_key['user'] = os.getenv("SLURM_USER_NAME", "slurm")
    configuration.api_key['token'] = os.getenv("SLURM_USER_TOKEN")
    
    if not configuration.api_key['token']:
        print("Error: SLURM_USER_TOKEN environment variable is required")
        return
    
    job_id: Optional[str] = None
    
    try:
        async with slurpy.ApiClient(configuration) as client:
            api = slurpy.SlurmApi(client)
            
            # 1. Test connectivity
            print("🔍 Testing cluster connectivity...")
            ping_response = await api.get_ping()
            print(f"✅ Cluster is responsive: {ping_response.to_dict()}")
            
            # 2. Submit a job
            print("\\n📤 Submitting job...")
            job_spec = {
                "script": "#!/bin/bash\\nsleep 30\\necho 'Hello from Slurm!'",
                "job": {
                    "name": "slurpy_demo",
                    "current_working_directory": "/tmp",
                    "environment": ["PATH=/bin:/usr/bin"],
                    "ntasks": 1,
                    "time_limit": {"set": True, "number": 120},
                }
            }
            
            job_request = slurpy.JobSubmitReq.from_dict(job_spec)
            submit_response = await api.post_job_submit(job_submit_req=job_request)
            result = submit_response.to_dict()
            job_id = str(result['job_id'])
            print(f"✅ Job submitted successfully with ID: {job_id}")
            
            # 3. Monitor job
            print(f"\\n👀 Monitoring job {job_id}...")
            job_response = await api.get_job(job_id=job_id)
            job_data = job_response.to_dict()
            job_info = job_data['jobs'][0]
            print(f"📊 Job status: {job_info['job_state']}")
            print(f"📋 Job details: {job_info['name']} on {job_info.get('nodes', 'pending')}")
            
            # 4. List all current jobs
            print("\\n📋 Current cluster jobs:")
            jobs_response = await api.get_jobs()
            jobs = jobs_response.to_dict()
            print(f"Found {len(jobs['jobs'])} total jobs in the cluster")
            
    except ApiException as e:
        print(f"❌ Slurm API error: {e.status} - {e.reason}")
        if e.body:
            print(f"Response: {e.body}")
            
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        
    finally:
        # Cleanup: Cancel the job if it was created
        if job_id:
            try:
                async with slurpy.ApiClient(configuration) as client:
                    api = slurpy.SlurmApi(client)
                    await api.delete_job(job_id)
                    print(f"\\n🧹 Cleanup: Job {job_id} cancellation requested")
            except Exception as cleanup_error:
                print(f"⚠️ Cleanup warning: Could not cancel job {job_id}: {cleanup_error}")


if __name__ == "__main__":
    asyncio.run(slurm_workflow())
```

## License

This project is licensed under the Apache 2.0 License - see the LICENSE file for details.

## Support

- 📖 **Documentation**: Check the docstrings and type hints
- 🐛 **Issues**: Report bugs on GitHub Issues
- 💬 **Discussions**: Ask questions in GitHub Discussions
- 📧 **Contact**: Reach out to the maintainers

## Related Projects

- [Slurm](https://slurm.schedmd.com/) - The original Slurm Workload Manager
- [Slurm REST API Documentation](https://slurm.schedmd.com/rest_api.html) - Official REST API docs