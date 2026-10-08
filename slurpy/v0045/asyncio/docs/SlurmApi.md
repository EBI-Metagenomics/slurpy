# slurpy.v0045.asyncio.SlurmApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_job**](SlurmApi.md#delete_job) | **DELETE** /slurm/v0.0.45/job/{job_id} | cancel or signal job
[**delete_jobs**](SlurmApi.md#delete_jobs) | **DELETE** /slurm/v0.0.45/jobs/ | send signal to list of jobs
[**delete_node**](SlurmApi.md#delete_node) | **DELETE** /slurm/v0.0.45/node/{node_name} | delete node
[**delete_partition**](SlurmApi.md#delete_partition) | **DELETE** /slurm/v0.0.45/partition/{partition_name} | delete partition
[**delete_reservation**](SlurmApi.md#delete_reservation) | **DELETE** /slurm/v0.0.45/reservation/{reservation_name} | delete a reservation
[**get_conf**](SlurmApi.md#get_conf) | **GET** /slurm/v0.0.45/conf | Dump slurm configuration
[**get_diag**](SlurmApi.md#get_diag) | **GET** /slurm/v0.0.45/diag/ | get diagnostics
[**get_job**](SlurmApi.md#get_job) | **GET** /slurm/v0.0.45/job/{job_id} | get job info
[**get_job_requeue**](SlurmApi.md#get_job_requeue) | **GET** /slurm/v0.0.45/job/{job_id}/requeue | request job requeue
[**get_jobs**](SlurmApi.md#get_jobs) | **GET** /slurm/v0.0.45/jobs/ | get list of jobs
[**get_jobs_state**](SlurmApi.md#get_jobs_state) | **GET** /slurm/v0.0.45/jobs/state/ | get list of job states
[**get_licenses**](SlurmApi.md#get_licenses) | **GET** /slurm/v0.0.45/licenses/ | get all Slurm tracked license info
[**get_node**](SlurmApi.md#get_node) | **GET** /slurm/v0.0.45/node/{node_name} | get node info
[**get_nodes**](SlurmApi.md#get_nodes) | **GET** /slurm/v0.0.45/nodes/ | get node(s) info
[**get_partition**](SlurmApi.md#get_partition) | **GET** /slurm/v0.0.45/partition/{partition_name} | get partition info
[**get_partitions**](SlurmApi.md#get_partitions) | **GET** /slurm/v0.0.45/partitions/ | get all partition info
[**get_ping**](SlurmApi.md#get_ping) | **GET** /slurm/v0.0.45/ping/ | ping test
[**get_reconfigure**](SlurmApi.md#get_reconfigure) | **GET** /slurm/v0.0.45/reconfigure/ | request slurmctld reconfigure
[**get_reservation**](SlurmApi.md#get_reservation) | **GET** /slurm/v0.0.45/reservation/{reservation_name} | get reservation info
[**get_reservations**](SlurmApi.md#get_reservations) | **GET** /slurm/v0.0.45/reservations/ | get all reservation info
[**get_resources**](SlurmApi.md#get_resources) | **GET** /slurm/v0.0.45/resources/{job_id} | get resource layout info
[**get_shares**](SlurmApi.md#get_shares) | **GET** /slurm/v0.0.45/shares | get fairshare info
[**post_job**](SlurmApi.md#post_job) | **POST** /slurm/v0.0.45/job/{job_id} | update job
[**post_job_allocate**](SlurmApi.md#post_job_allocate) | **POST** /slurm/v0.0.45/job/allocate | submit new job allocation without any steps that must be signaled to stop
[**post_job_submit**](SlurmApi.md#post_job_submit) | **POST** /slurm/v0.0.45/job/submit | submit new job
[**post_jobs_requeue**](SlurmApi.md#post_jobs_requeue) | **POST** /slurm/v0.0.45/jobs/requeue | batch requeue job(s)
[**post_new_node**](SlurmApi.md#post_new_node) | **POST** /slurm/v0.0.45/new/node/ | create node
[**post_node**](SlurmApi.md#post_node) | **POST** /slurm/v0.0.45/node/{node_name} | update node properties
[**post_nodes**](SlurmApi.md#post_nodes) | **POST** /slurm/v0.0.45/nodes/ | batch update node(s)
[**post_partitions**](SlurmApi.md#post_partitions) | **POST** /slurm/v0.0.45/partitions/ | create or update partitions
[**post_reservation**](SlurmApi.md#post_reservation) | **POST** /slurm/v0.0.45/reservation | create or update a reservation
[**post_reservations**](SlurmApi.md#post_reservations) | **POST** /slurm/v0.0.45/reservations/ | create or update reservations


# **delete_job**
> OpenAPIKillJobResp delete_job(job_id, signal=signal, flags=flags)

cancel or signal job

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_kill_job_resp import OpenAPIKillJobResp
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Job ID
    signal = 'signal_example' # str | Signal to send to Job (optional)
    flags = 'flags_example' # str | Signalling flags (optional)

    try:
        # cancel or signal job
        api_response = await api_instance.delete_job(job_id, signal=signal, flags=flags)
        print("The response of SlurmApi->delete_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->delete_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID | 
 **signal** | **str**| Signal to send to Job | [optional] 
 **flags** | **str**| Signalling flags | [optional] 

### Return type

[**OpenAPIKillJobResp**](OpenAPIKillJobResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job signal result |  -  |
**0** | job signal result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_jobs**
> OpenAPIKillJobsResp delete_jobs(kill_jobs_msg=kill_jobs_msg)

send signal to list of jobs

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.kill_jobs_msg import KillJobsMsg
from slurpy.v0045.asyncio.models.open_api_kill_jobs_resp import OpenAPIKillJobsResp
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)
    kill_jobs_msg = slurpy.v0045.asyncio.KillJobsMsg() # KillJobsMsg | Signal or cancel jobs (optional)

    try:
        # send signal to list of jobs
        api_response = await api_instance.delete_jobs(kill_jobs_msg=kill_jobs_msg)
        print("The response of SlurmApi->delete_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->delete_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kill_jobs_msg** | [**KillJobsMsg**](KillJobsMsg.md)| Signal or cancel jobs | [optional] 

### Return type

[**OpenAPIKillJobsResp**](OpenAPIKillJobsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | description of jobs to signal |  -  |
**0** | description of jobs to signal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_node**
> OpenAPIResp delete_node(node_name)

delete node

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_resp import OpenAPIResp
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)
    node_name = 'node_name_example' # str | Node name

    try:
        # delete node
        api_response = await api_instance.delete_node(node_name)
        print("The response of SlurmApi->delete_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->delete_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Node name | 

### Return type

[**OpenAPIResp**](OpenAPIResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node delete request result |  -  |
**0** | node delete request result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_partition**
> OpenAPIResp delete_partition(partition_name)

delete partition

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_resp import OpenAPIResp
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)
    partition_name = 'partition_name_example' # str | Partition name

    try:
        # delete partition
        api_response = await api_instance.delete_partition(partition_name)
        print("The response of SlurmApi->delete_partition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->delete_partition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_name** | **str**| Partition name | 

### Return type

[**OpenAPIResp**](OpenAPIResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | partition deletion result |  -  |
**0** | partition deletion result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_reservation**
> OpenAPIResp delete_reservation(reservation_name)

delete a reservation

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_resp import OpenAPIResp
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)
    reservation_name = 'reservation_name_example' # str | Reservation name

    try:
        # delete a reservation
        api_response = await api_instance.delete_reservation(reservation_name)
        print("The response of SlurmApi->delete_reservation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->delete_reservation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_name** | **str**| Reservation name | 

### Return type

[**OpenAPIResp**](OpenAPIResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reservation delete request result |  -  |
**0** | reservation delete request result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conf**
> OpenAPIConfResp get_conf(update_time=update_time)

Dump slurm configuration

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_conf_resp import OpenAPIConfResp
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Query config updated more recently than this time (UNIX timestamp) (optional)

    try:
        # Dump slurm configuration
        api_response = await api_instance.get_conf(update_time=update_time)
        print("The response of SlurmApi->get_conf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_conf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Query config updated more recently than this time (UNIX timestamp) | [optional] 

### Return type

[**OpenAPIConfResp**](OpenAPIConfResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | slurm configuration |  -  |
**0** | slurm configuration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_diag**
> OpenAPIDiagResp get_diag()

get diagnostics

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_diag_resp import OpenAPIDiagResp
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)

    try:
        # get diagnostics
        api_response = await api_instance.get_diag()
        print("The response of SlurmApi->get_diag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_diag: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OpenAPIDiagResp**](OpenAPIDiagResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | diagnostic results |  -  |
**0** | diagnostic results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job**
> OpenAPIJobInfoResp get_job(job_id, update_time=update_time, flags=flags)

get job info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_job_info_resp import OpenAPIJobInfoResp
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Job ID
    update_time = 'update_time_example' # str | Query jobs updated more recently than this time (UNIX timestamp) (optional)
    flags = 'flags_example' # str | Query flags (optional)

    try:
        # get job info
        api_response = await api_instance.get_job(job_id, update_time=update_time, flags=flags)
        print("The response of SlurmApi->get_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID | 
 **update_time** | **str**| Query jobs updated more recently than this time (UNIX timestamp) | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**OpenAPIJobInfoResp**](OpenAPIJobInfoResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job(s) information |  -  |
**0** | job(s) information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_requeue**
> OpenAPIJobRequeueResp get_job_requeue(job_id, incomplete=incomplete, hold=hold, special_exit=special_exit)

request job requeue

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_job_requeue_resp import OpenAPIJobRequeueResp
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Job ID
    incomplete = 'incomplete_example' # str | Operate only on jobs (or tasks of a job array) which have not completed (optional)
    hold = 'hold_example' # str | Hold job after requeue, will require manual release to run again (optional)
    special_exit = 'special_exit_example' # str | Set SPECIAL_EXIT state after requeue; must also specify the Hold flag (optional)

    try:
        # request job requeue
        api_response = await api_instance.get_job_requeue(job_id, incomplete=incomplete, hold=hold, special_exit=special_exit)
        print("The response of SlurmApi->get_job_requeue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_job_requeue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID | 
 **incomplete** | **str**| Operate only on jobs (or tasks of a job array) which have not completed | [optional] 
 **hold** | **str**| Hold job after requeue, will require manual release to run again | [optional] 
 **special_exit** | **str**| Set SPECIAL_EXIT state after requeue; must also specify the Hold flag | [optional] 

### Return type

[**OpenAPIJobRequeueResp**](OpenAPIJobRequeueResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job requeue result |  -  |
**0** | job requeue result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobs**
> OpenAPIJobInfoResp get_jobs(update_time=update_time, flags=flags)

get list of jobs

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_job_info_resp import OpenAPIJobInfoResp
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Query jobs updated more recently than this time (UNIX timestamp) (optional)
    flags = 'flags_example' # str | Query flags (optional)

    try:
        # get list of jobs
        api_response = await api_instance.get_jobs(update_time=update_time, flags=flags)
        print("The response of SlurmApi->get_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Query jobs updated more recently than this time (UNIX timestamp) | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**OpenAPIJobInfoResp**](OpenAPIJobInfoResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job(s) information |  -  |
**0** | job(s) information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobs_state**
> OpenAPIJobInfoResp get_jobs_state(job_id=job_id)

get list of job states

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_job_info_resp import OpenAPIJobInfoResp
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)
    job_id = 'job_id_example' # str | CSV list of Job IDs to search for (optional)

    try:
        # get list of job states
        api_response = await api_instance.get_jobs_state(job_id=job_id)
        print("The response of SlurmApi->get_jobs_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_jobs_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| CSV list of Job IDs to search for | [optional] 

### Return type

[**OpenAPIJobInfoResp**](OpenAPIJobInfoResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job(s) state information |  -  |
**0** | job(s) state information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_licenses**
> OpenAPILicensesResp get_licenses()

get all Slurm tracked license info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_licenses_resp import OpenAPILicensesResp
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)

    try:
        # get all Slurm tracked license info
        api_response = await api_instance.get_licenses()
        print("The response of SlurmApi->get_licenses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_licenses: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OpenAPILicensesResp**](OpenAPILicensesResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | results of get all licenses |  -  |
**0** | results of get all licenses |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node**
> OpenAPINodesResp get_node(node_name, update_time=update_time, flags=flags)

get node info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_nodes_resp import OpenAPINodesResp
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)
    node_name = 'node_name_example' # str | Node name
    update_time = 'update_time_example' # str | Query nodes updated more recently than this time (UNIX timestamp) (optional)
    flags = 'flags_example' # str | Query flags (optional)

    try:
        # get node info
        api_response = await api_instance.get_node(node_name, update_time=update_time, flags=flags)
        print("The response of SlurmApi->get_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Node name | 
 **update_time** | **str**| Query nodes updated more recently than this time (UNIX timestamp) | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**OpenAPINodesResp**](OpenAPINodesResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node information |  -  |
**0** | node information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nodes**
> OpenAPINodesResp get_nodes(update_time=update_time, flags=flags)

get node(s) info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_nodes_resp import OpenAPINodesResp
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Query nodes updated more recently than this time (UNIX timestamp) (optional)
    flags = 'flags_example' # str | Query flags (optional)

    try:
        # get node(s) info
        api_response = await api_instance.get_nodes(update_time=update_time, flags=flags)
        print("The response of SlurmApi->get_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Query nodes updated more recently than this time (UNIX timestamp) | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**OpenAPINodesResp**](OpenAPINodesResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node(s) information |  -  |
**0** | node(s) information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_partition**
> OpenAPIPartitionResp get_partition(partition_name, update_time=update_time, flags=flags)

get partition info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_partition_resp import OpenAPIPartitionResp
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)
    partition_name = 'partition_name_example' # str | Partition name
    update_time = 'update_time_example' # str | Query partitions updated more recently than this time (UNIX timestamp) (optional)
    flags = 'flags_example' # str | Query flags (optional)

    try:
        # get partition info
        api_response = await api_instance.get_partition(partition_name, update_time=update_time, flags=flags)
        print("The response of SlurmApi->get_partition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_partition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_name** | **str**| Partition name | 
 **update_time** | **str**| Query partitions updated more recently than this time (UNIX timestamp) | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**OpenAPIPartitionResp**](OpenAPIPartitionResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | partition information |  -  |
**0** | partition information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_partitions**
> OpenAPIPartitionResp get_partitions(update_time=update_time, flags=flags)

get all partition info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_partition_resp import OpenAPIPartitionResp
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Query partitions updated more recently than this time (UNIX timestamp) (optional)
    flags = 'flags_example' # str | Query flags (optional)

    try:
        # get all partition info
        api_response = await api_instance.get_partitions(update_time=update_time, flags=flags)
        print("The response of SlurmApi->get_partitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_partitions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Query partitions updated more recently than this time (UNIX timestamp) | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**OpenAPIPartitionResp**](OpenAPIPartitionResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | partition information |  -  |
**0** | partition information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ping**
> OpenAPIPingArrayResp get_ping()

ping test

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_ping_array_resp import OpenAPIPingArrayResp
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)

    try:
        # ping test
        api_response = await api_instance.get_ping()
        print("The response of SlurmApi->get_ping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_ping: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OpenAPIPingArrayResp**](OpenAPIPingArrayResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | results of ping test |  -  |
**0** | results of ping test |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reconfigure**
> OpenAPIResp get_reconfigure()

request slurmctld reconfigure

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_resp import OpenAPIResp
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)

    try:
        # request slurmctld reconfigure
        api_response = await api_instance.get_reconfigure()
        print("The response of SlurmApi->get_reconfigure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_reconfigure: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OpenAPIResp**](OpenAPIResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reconfigure request result |  -  |
**0** | reconfigure request result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reservation**
> OpenAPIReservationResp get_reservation(reservation_name, update_time=update_time)

get reservation info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_reservation_resp import OpenAPIReservationResp
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)
    reservation_name = 'reservation_name_example' # str | Reservation name
    update_time = 'update_time_example' # str | Query reservations updated more recently than this time (UNIX timestamp) (optional)

    try:
        # get reservation info
        api_response = await api_instance.get_reservation(reservation_name, update_time=update_time)
        print("The response of SlurmApi->get_reservation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_reservation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_name** | **str**| Reservation name | 
 **update_time** | **str**| Query reservations updated more recently than this time (UNIX timestamp) | [optional] 

### Return type

[**OpenAPIReservationResp**](OpenAPIReservationResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reservation information |  -  |
**0** | reservation information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reservations**
> OpenAPIReservationResp get_reservations(update_time=update_time)

get all reservation info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_reservation_resp import OpenAPIReservationResp
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Query reservations updated more recently than this time (UNIX timestamp) (optional)

    try:
        # get all reservation info
        api_response = await api_instance.get_reservations(update_time=update_time)
        print("The response of SlurmApi->get_reservations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_reservations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Query reservations updated more recently than this time (UNIX timestamp) | [optional] 

### Return type

[**OpenAPIReservationResp**](OpenAPIReservationResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reservation information |  -  |
**0** | reservation information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resources**
> OpenAPIResourceLayoutResp get_resources(job_id)

get resource layout info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_resource_layout_resp import OpenAPIResourceLayoutResp
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Job ID

    try:
        # get resource layout info
        api_response = await api_instance.get_resources(job_id)
        print("The response of SlurmApi->get_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_resources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID | 

### Return type

[**OpenAPIResourceLayoutResp**](OpenAPIResourceLayoutResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | resource layout information |  -  |
**0** | resource layout information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shares**
> OpenAPISharesResp get_shares(accounts=accounts, users=users)

get fairshare info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_shares_resp import OpenAPISharesResp
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)
    accounts = 'accounts_example' # str | Accounts to query (optional)
    users = 'users_example' # str | Users to query (optional)

    try:
        # get fairshare info
        api_response = await api_instance.get_shares(accounts=accounts, users=users)
        print("The response of SlurmApi->get_shares:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_shares: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accounts** | **str**| Accounts to query | [optional] 
 **users** | **str**| Users to query | [optional] 

### Return type

[**OpenAPISharesResp**](OpenAPISharesResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | shares information |  -  |
**0** | shares information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_job**
> OpenAPIJobPostResponse post_job(job_id, job_desc_msg=job_desc_msg)

update job

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.job_desc_msg import JobDescMsg
from slurpy.v0045.asyncio.models.open_api_job_post_response import OpenAPIJobPostResponse
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Job ID
    job_desc_msg = slurpy.v0045.asyncio.JobDescMsg() # JobDescMsg | Job update description (optional)

    try:
        # update job
        api_response = await api_instance.post_job(job_id, job_desc_msg=job_desc_msg)
        print("The response of SlurmApi->post_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->post_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID | 
 **job_desc_msg** | [**JobDescMsg**](JobDescMsg.md)| Job update description | [optional] 

### Return type

[**OpenAPIJobPostResponse**](OpenAPIJobPostResponse.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job update result |  -  |
**0** | job update result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_job_allocate**
> OpenAPIJobAllocResp post_job_allocate(job_alloc_req=job_alloc_req)

submit new job allocation without any steps that must be signaled to stop

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.job_alloc_req import JobAllocReq
from slurpy.v0045.asyncio.models.open_api_job_alloc_resp import OpenAPIJobAllocResp
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)
    job_alloc_req = slurpy.v0045.asyncio.JobAllocReq() # JobAllocReq | Job allocation description (optional)

    try:
        # submit new job allocation without any steps that must be signaled to stop
        api_response = await api_instance.post_job_allocate(job_alloc_req=job_alloc_req)
        print("The response of SlurmApi->post_job_allocate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->post_job_allocate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_alloc_req** | [**JobAllocReq**](JobAllocReq.md)| Job allocation description | [optional] 

### Return type

[**OpenAPIJobAllocResp**](OpenAPIJobAllocResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job allocation response |  -  |
**0** | job allocation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_job_submit**
> OpenAPIJobSubmitResponse post_job_submit(job_submit_req=job_submit_req)

submit new job

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.job_submit_req import JobSubmitReq
from slurpy.v0045.asyncio.models.open_api_job_submit_response import OpenAPIJobSubmitResponse
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)
    job_submit_req = slurpy.v0045.asyncio.JobSubmitReq() # JobSubmitReq | Job description (optional)

    try:
        # submit new job
        api_response = await api_instance.post_job_submit(job_submit_req=job_submit_req)
        print("The response of SlurmApi->post_job_submit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->post_job_submit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_submit_req** | [**JobSubmitReq**](JobSubmitReq.md)| Job description | [optional] 

### Return type

[**OpenAPIJobSubmitResponse**](OpenAPIJobSubmitResponse.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job submission response |  -  |
**0** | job submission response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_jobs_requeue**
> OpenAPIJobsRequeueResp post_jobs_requeue(open_api_jobs_requeue_query=open_api_jobs_requeue_query)

batch requeue job(s)

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_jobs_requeue_query import OpenAPIJobsRequeueQuery
from slurpy.v0045.asyncio.models.open_api_jobs_requeue_resp import OpenAPIJobsRequeueResp
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)
    open_api_jobs_requeue_query = slurpy.v0045.asyncio.OpenAPIJobsRequeueQuery() # OpenAPIJobsRequeueQuery | batch job requeue request parameters (optional)

    try:
        # batch requeue job(s)
        api_response = await api_instance.post_jobs_requeue(open_api_jobs_requeue_query=open_api_jobs_requeue_query)
        print("The response of SlurmApi->post_jobs_requeue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->post_jobs_requeue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_api_jobs_requeue_query** | [**OpenAPIJobsRequeueQuery**](OpenAPIJobsRequeueQuery.md)| batch job requeue request parameters | [optional] 

### Return type

[**OpenAPIJobsRequeueResp**](OpenAPIJobsRequeueResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | batch job requeue request result |  -  |
**0** | batch job requeue request result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_new_node**
> OpenAPIResp post_new_node(open_api_create_node_req=open_api_create_node_req)

create node

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_create_node_req import OpenAPICreateNodeReq
from slurpy.v0045.asyncio.models.open_api_resp import OpenAPIResp
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)
    open_api_create_node_req = slurpy.v0045.asyncio.OpenAPICreateNodeReq() # OpenAPICreateNodeReq | node create request (optional)

    try:
        # create node
        api_response = await api_instance.post_new_node(open_api_create_node_req=open_api_create_node_req)
        print("The response of SlurmApi->post_new_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->post_new_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_api_create_node_req** | [**OpenAPICreateNodeReq**](OpenAPICreateNodeReq.md)| node create request | [optional] 

### Return type

[**OpenAPIResp**](OpenAPIResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node create request result |  -  |
**0** | node create request result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_node**
> OpenAPIResp post_node(node_name, update_node_msg=update_node_msg)

update node properties

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_resp import OpenAPIResp
from slurpy.v0045.asyncio.models.update_node_msg import UpdateNodeMsg
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)
    node_name = 'node_name_example' # str | Node name
    update_node_msg = slurpy.v0045.asyncio.UpdateNodeMsg() # UpdateNodeMsg | Node update description (optional)

    try:
        # update node properties
        api_response = await api_instance.post_node(node_name, update_node_msg=update_node_msg)
        print("The response of SlurmApi->post_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->post_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Node name | 
 **update_node_msg** | [**UpdateNodeMsg**](UpdateNodeMsg.md)| Node update description | [optional] 

### Return type

[**OpenAPIResp**](OpenAPIResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node update request result |  -  |
**0** | node update request result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_nodes**
> OpenAPIResp post_nodes(update_node_msg=update_node_msg)

batch update node(s)

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_resp import OpenAPIResp
from slurpy.v0045.asyncio.models.update_node_msg import UpdateNodeMsg
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)
    update_node_msg = slurpy.v0045.asyncio.UpdateNodeMsg() # UpdateNodeMsg | Nodelist update description (optional)

    try:
        # batch update node(s)
        api_response = await api_instance.post_nodes(update_node_msg=update_node_msg)
        print("The response of SlurmApi->post_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->post_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_node_msg** | [**UpdateNodeMsg**](UpdateNodeMsg.md)| Nodelist update description | [optional] 

### Return type

[**OpenAPIResp**](OpenAPIResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | batch node update request result |  -  |
**0** | batch node update request result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_partitions**
> OpenAPIResp post_partitions(open_api_partitions_mod_req=open_api_partitions_mod_req)

create or update partitions

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_partitions_mod_req import OpenAPIPartitionsModReq
from slurpy.v0045.asyncio.models.open_api_resp import OpenAPIResp
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)
    open_api_partitions_mod_req = slurpy.v0045.asyncio.OpenAPIPartitionsModReq() # OpenAPIPartitionsModReq | partition description (optional)

    try:
        # create or update partitions
        api_response = await api_instance.post_partitions(open_api_partitions_mod_req=open_api_partitions_mod_req)
        print("The response of SlurmApi->post_partitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->post_partitions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_api_partitions_mod_req** | [**OpenAPIPartitionsModReq**](OpenAPIPartitionsModReq.md)| partition description | [optional] 

### Return type

[**OpenAPIResp**](OpenAPIResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | partition update or create request results |  -  |
**0** | partition update or create request results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_reservation**
> OpenAPIReservationModResp post_reservation(reservation_desc_msg=reservation_desc_msg)

create or update a reservation

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_reservation_mod_resp import OpenAPIReservationModResp
from slurpy.v0045.asyncio.models.reservation_desc_msg import ReservationDescMsg
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)
    reservation_desc_msg = slurpy.v0045.asyncio.ReservationDescMsg() # ReservationDescMsg | reservation description (optional)

    try:
        # create or update a reservation
        api_response = await api_instance.post_reservation(reservation_desc_msg=reservation_desc_msg)
        print("The response of SlurmApi->post_reservation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->post_reservation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_desc_msg** | [**ReservationDescMsg**](ReservationDescMsg.md)| reservation description | [optional] 

### Return type

[**OpenAPIReservationModResp**](OpenAPIReservationModResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reservation description |  -  |
**0** | reservation description |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_reservations**
> OpenAPIReservationModResp post_reservations(reservation_mod_req=reservation_mod_req)

create or update reservations

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_reservation_mod_resp import OpenAPIReservationModResp
from slurpy.v0045.asyncio.models.reservation_mod_req import ReservationModReq
from slurpy.v0045.asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.asyncio.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0045.asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
async with slurpy.v0045.asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.asyncio.SlurmApi(api_client)
    reservation_mod_req = slurpy.v0045.asyncio.ReservationModReq() # ReservationModReq | reservation descriptions (optional)

    try:
        # create or update reservations
        api_response = await api_instance.post_reservations(reservation_mod_req=reservation_mod_req)
        print("The response of SlurmApi->post_reservations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->post_reservations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_mod_req** | [**ReservationModReq**](ReservationModReq.md)| reservation descriptions | [optional] 

### Return type

[**OpenAPIReservationModResp**](OpenAPIReservationModResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reservation descriptions |  -  |
**0** | reservation descriptions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

