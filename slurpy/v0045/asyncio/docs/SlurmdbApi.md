# slurpy.v0045.asyncio.SlurmdbApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_account**](SlurmdbApi.md#delete_account) | **DELETE** /slurmdb/v0.0.45/account/{account_name} | Delete account
[**delete_association**](SlurmdbApi.md#delete_association) | **DELETE** /slurmdb/v0.0.45/association/ | Delete association
[**delete_associations**](SlurmdbApi.md#delete_associations) | **DELETE** /slurmdb/v0.0.45/associations/ | Delete associations
[**delete_cluster**](SlurmdbApi.md#delete_cluster) | **DELETE** /slurmdb/v0.0.45/cluster/{cluster_name} | Delete cluster
[**delete_single_qos**](SlurmdbApi.md#delete_single_qos) | **DELETE** /slurmdb/v0.0.45/qos/{qos} | Delete QOS
[**delete_user**](SlurmdbApi.md#delete_user) | **DELETE** /slurmdb/v0.0.45/user/{name} | Delete user
[**delete_wckey**](SlurmdbApi.md#delete_wckey) | **DELETE** /slurmdb/v0.0.45/wckey/{id} | Delete wckey
[**get_account**](SlurmdbApi.md#get_account) | **GET** /slurmdb/v0.0.45/account/{account_name} | Get account info
[**get_accounts**](SlurmdbApi.md#get_accounts) | **GET** /slurmdb/v0.0.45/accounts/ | Get account list
[**get_association**](SlurmdbApi.md#get_association) | **GET** /slurmdb/v0.0.45/association/ | Get association info
[**get_associations**](SlurmdbApi.md#get_associations) | **GET** /slurmdb/v0.0.45/associations/ | Get association list
[**get_cluster**](SlurmdbApi.md#get_cluster) | **GET** /slurmdb/v0.0.45/cluster/{cluster_name} | Get cluster info
[**get_clusters**](SlurmdbApi.md#get_clusters) | **GET** /slurmdb/v0.0.45/clusters/ | Get cluster list
[**get_conf**](SlurmdbApi.md#get_conf) | **GET** /slurmdb/v0.0.45/conf | Dump slurmdbd configuration
[**get_config**](SlurmdbApi.md#get_config) | **GET** /slurmdb/v0.0.45/config | Dump all configuration information
[**get_diag**](SlurmdbApi.md#get_diag) | **GET** /slurmdb/v0.0.45/diag/ | Get slurmdb diagnostics
[**get_instance**](SlurmdbApi.md#get_instance) | **GET** /slurmdb/v0.0.45/instance/ | Get instance info
[**get_instances**](SlurmdbApi.md#get_instances) | **GET** /slurmdb/v0.0.45/instances/ | Get instance list
[**get_job**](SlurmdbApi.md#get_job) | **GET** /slurmdb/v0.0.45/job/{job_id} | Get job info
[**get_jobs**](SlurmdbApi.md#get_jobs) | **GET** /slurmdb/v0.0.45/jobs/ | Get job list
[**get_ping**](SlurmdbApi.md#get_ping) | **GET** /slurmdb/v0.0.45/ping/ | ping test
[**get_qos**](SlurmdbApi.md#get_qos) | **GET** /slurmdb/v0.0.45/qos/ | Get QOS list
[**get_single_qos**](SlurmdbApi.md#get_single_qos) | **GET** /slurmdb/v0.0.45/qos/{qos} | Get QOS info
[**get_tres**](SlurmdbApi.md#get_tres) | **GET** /slurmdb/v0.0.45/tres/ | Get TRES info
[**get_user**](SlurmdbApi.md#get_user) | **GET** /slurmdb/v0.0.45/user/{name} | Get user info
[**get_users**](SlurmdbApi.md#get_users) | **GET** /slurmdb/v0.0.45/users/ | Get user list
[**get_wckey**](SlurmdbApi.md#get_wckey) | **GET** /slurmdb/v0.0.45/wckey/{id} | Get wckey info
[**get_wckeys**](SlurmdbApi.md#get_wckeys) | **GET** /slurmdb/v0.0.45/wckeys/ | Get wckey list
[**post_accounts**](SlurmdbApi.md#post_accounts) | **POST** /slurmdb/v0.0.45/accounts/ | Add/update list of accounts
[**post_accounts_association**](SlurmdbApi.md#post_accounts_association) | **POST** /slurmdb/v0.0.45/accounts_association/ | Add accounts with conditional association
[**post_associations**](SlurmdbApi.md#post_associations) | **POST** /slurmdb/v0.0.45/associations/ | Set associations info
[**post_clusters**](SlurmdbApi.md#post_clusters) | **POST** /slurmdb/v0.0.45/clusters/ | Get cluster list
[**post_config**](SlurmdbApi.md#post_config) | **POST** /slurmdb/v0.0.45/config | Load all configuration information
[**post_job**](SlurmdbApi.md#post_job) | **POST** /slurmdb/v0.0.45/job/{job_id} | Update job
[**post_jobs**](SlurmdbApi.md#post_jobs) | **POST** /slurmdb/v0.0.45/jobs/ | Update jobs
[**post_qos**](SlurmdbApi.md#post_qos) | **POST** /slurmdb/v0.0.45/qos/ | Add or update QOSs
[**post_tres**](SlurmdbApi.md#post_tres) | **POST** /slurmdb/v0.0.45/tres/ | Add TRES
[**post_users**](SlurmdbApi.md#post_users) | **POST** /slurmdb/v0.0.45/users/ | Update users
[**post_users_association**](SlurmdbApi.md#post_users_association) | **POST** /slurmdb/v0.0.45/users_association/ | Add users with conditional association
[**post_wckeys**](SlurmdbApi.md#post_wckeys) | **POST** /slurmdb/v0.0.45/wckeys/ | Add or update wckeys


# **delete_account**
> OpenAPIAccountsRemovedResp delete_account(account_name)

Delete account

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_accounts_removed_resp import OpenAPIAccountsRemovedResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    account_name = 'account_name_example' # str | Account name

    try:
        # Delete account
        api_response = await api_instance.delete_account(account_name)
        print("The response of SlurmdbApi->delete_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->delete_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| Account name | 

### Return type

[**OpenAPIAccountsRemovedResp**](OpenAPIAccountsRemovedResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of account deletion request |  -  |
**0** | Status of account deletion request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_association**
> OpenAPIAssocsRemovedResp delete_association(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)

Delete association

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_assocs_removed_resp import OpenAPIAssocsRemovedResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    account = 'account_example' # str | CSV accounts list (optional)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    default_qos = 'default_qos_example' # str | CSV QOS list (optional)
    include_deleted_associations = 'include_deleted_associations_example' # str |  (optional)
    include_usage = 'include_usage_example' # str |  (optional)
    filter_to_only_defaults = 'filter_to_only_defaults_example' # str |  (optional)
    include_the_raw_qos_or_delta_qos = 'include_the_raw_qos_or_delta_qos_example' # str |  (optional)
    include_sub_acct_information = 'include_sub_acct_information_example' # str |  (optional)
    exclude_parent_id_name = 'exclude_parent_id_name_example' # str |  (optional)
    exclude_limits_from_parents = 'exclude_limits_from_parents_example' # str |  (optional)
    id = 'id_example' # str | CSV ID list (optional)
    parent_account = 'parent_account_example' # str | CSV names of parent account (optional)
    partition = 'partition_example' # str | CSV partition name list (optional)
    qos = 'qos_example' # str | CSV QOS list (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    user = 'user_example' # str | CSV user list (optional)

    try:
        # Delete association
        api_response = await api_instance.delete_association(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)
        print("The response of SlurmdbApi->delete_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->delete_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| CSV accounts list | [optional] 
 **cluster** | **str**| CSV clusters list | [optional] 
 **default_qos** | **str**| CSV QOS list | [optional] 
 **include_deleted_associations** | **str**|  | [optional] 
 **include_usage** | **str**|  | [optional] 
 **filter_to_only_defaults** | **str**|  | [optional] 
 **include_the_raw_qos_or_delta_qos** | **str**|  | [optional] 
 **include_sub_acct_information** | **str**|  | [optional] 
 **exclude_parent_id_name** | **str**|  | [optional] 
 **exclude_limits_from_parents** | **str**|  | [optional] 
 **id** | **str**| CSV ID list | [optional] 
 **parent_account** | **str**| CSV names of parent account | [optional] 
 **partition** | **str**| CSV partition name list | [optional] 
 **qos** | **str**| CSV QOS list | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **user** | **str**| CSV user list | [optional] 

### Return type

[**OpenAPIAssocsRemovedResp**](OpenAPIAssocsRemovedResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of associations delete request |  -  |
**0** | Status of associations delete request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_associations**
> OpenAPIAssocsRemovedResp delete_associations(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)

Delete associations

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_assocs_removed_resp import OpenAPIAssocsRemovedResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    account = 'account_example' # str | CSV accounts list (optional)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    default_qos = 'default_qos_example' # str | CSV QOS list (optional)
    include_deleted_associations = 'include_deleted_associations_example' # str |  (optional)
    include_usage = 'include_usage_example' # str |  (optional)
    filter_to_only_defaults = 'filter_to_only_defaults_example' # str |  (optional)
    include_the_raw_qos_or_delta_qos = 'include_the_raw_qos_or_delta_qos_example' # str |  (optional)
    include_sub_acct_information = 'include_sub_acct_information_example' # str |  (optional)
    exclude_parent_id_name = 'exclude_parent_id_name_example' # str |  (optional)
    exclude_limits_from_parents = 'exclude_limits_from_parents_example' # str |  (optional)
    id = 'id_example' # str | CSV ID list (optional)
    parent_account = 'parent_account_example' # str | CSV names of parent account (optional)
    partition = 'partition_example' # str | CSV partition name list (optional)
    qos = 'qos_example' # str | CSV QOS list (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    user = 'user_example' # str | CSV user list (optional)

    try:
        # Delete associations
        api_response = await api_instance.delete_associations(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)
        print("The response of SlurmdbApi->delete_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->delete_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| CSV accounts list | [optional] 
 **cluster** | **str**| CSV clusters list | [optional] 
 **default_qos** | **str**| CSV QOS list | [optional] 
 **include_deleted_associations** | **str**|  | [optional] 
 **include_usage** | **str**|  | [optional] 
 **filter_to_only_defaults** | **str**|  | [optional] 
 **include_the_raw_qos_or_delta_qos** | **str**|  | [optional] 
 **include_sub_acct_information** | **str**|  | [optional] 
 **exclude_parent_id_name** | **str**|  | [optional] 
 **exclude_limits_from_parents** | **str**|  | [optional] 
 **id** | **str**| CSV ID list | [optional] 
 **parent_account** | **str**| CSV names of parent account | [optional] 
 **partition** | **str**| CSV partition name list | [optional] 
 **qos** | **str**| CSV QOS list | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **user** | **str**| CSV user list | [optional] 

### Return type

[**OpenAPIAssocsRemovedResp**](OpenAPIAssocsRemovedResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of associations deleted |  -  |
**0** | List of associations deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster**
> OpenAPIClustersRemovedResp delete_cluster(cluster_name, classification=classification, cluster=cluster, federation=federation, flags=flags, rpc_version=rpc_version, usage_end=usage_end, usage_start=usage_start, with_deleted=with_deleted, with_usage=with_usage)

Delete cluster

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_clusters_removed_resp import OpenAPIClustersRemovedResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    classification = 'classification_example' # str | Type of machine (optional)
    cluster = 'cluster_example' # str | CSV cluster list (optional)
    federation = 'federation_example' # str | CSV federation list (optional)
    flags = 'flags_example' # str | Query flags (optional)
    rpc_version = 'rpc_version_example' # str | CSV RPC version list (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted clusters (optional)
    with_usage = 'with_usage_example' # str | Include usage (optional)

    try:
        # Delete cluster
        api_response = await api_instance.delete_cluster(cluster_name, classification=classification, cluster=cluster, federation=federation, flags=flags, rpc_version=rpc_version, usage_end=usage_end, usage_start=usage_start, with_deleted=with_deleted, with_usage=with_usage)
        print("The response of SlurmdbApi->delete_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->delete_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **classification** | **str**| Type of machine | [optional] 
 **cluster** | **str**| CSV cluster list | [optional] 
 **federation** | **str**| CSV federation list | [optional] 
 **flags** | **str**| Query flags | [optional] 
 **rpc_version** | **str**| CSV RPC version list | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **with_deleted** | **str**| Include deleted clusters | [optional] 
 **with_usage** | **str**| Include usage | [optional] 

### Return type

[**OpenAPIClustersRemovedResp**](OpenAPIClustersRemovedResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of delete cluster request |  -  |
**0** | Result of delete cluster request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_single_qos**
> OpenAPISlurmdbdQosRemovedResp delete_single_qos(qos)

Delete QOS

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_slurmdbd_qos_removed_resp import OpenAPISlurmdbdQosRemovedResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    qos = 'qos_example' # str | QOS name

    try:
        # Delete QOS
        api_response = await api_instance.delete_single_qos(qos)
        print("The response of SlurmdbApi->delete_single_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->delete_single_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qos** | **str**| QOS name | 

### Return type

[**OpenAPISlurmdbdQosRemovedResp**](OpenAPISlurmdbdQosRemovedResp.md)

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

# **delete_user**
> OpenAPIResp delete_user(name)

Delete user

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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    name = 'name_example' # str | User name

    try:
        # Delete user
        api_response = await api_instance.delete_user(name)
        print("The response of SlurmdbApi->delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| User name | 

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
**200** | Result of user delete request |  -  |
**0** | Result of user delete request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_wckey**
> OpenAPIWckeyRemovedResp delete_wckey(id)

Delete wckey

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_wckey_removed_resp import OpenAPIWckeyRemovedResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    id = 'id_example' # str | WCKey ID

    try:
        # Delete wckey
        api_response = await api_instance.delete_wckey(id)
        print("The response of SlurmdbApi->delete_wckey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->delete_wckey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| WCKey ID | 

### Return type

[**OpenAPIWckeyRemovedResp**](OpenAPIWckeyRemovedResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of wckey deletion request |  -  |
**0** | Result of wckey deletion request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account**
> OpenAPIAccountsResp get_account(account_name, with_assocs=with_assocs, with_coords=with_coords, with_deleted=with_deleted)

Get account info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_accounts_resp import OpenAPIAccountsResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    account_name = 'account_name_example' # str | Account name
    with_assocs = 'with_assocs_example' # str | Include associations (optional)
    with_coords = 'with_coords_example' # str | Include coordinators (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted (optional)

    try:
        # Get account info
        api_response = await api_instance.get_account(account_name, with_assocs=with_assocs, with_coords=with_coords, with_deleted=with_deleted)
        print("The response of SlurmdbApi->get_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->get_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| Account name | 
 **with_assocs** | **str**| Include associations | [optional] 
 **with_coords** | **str**| Include coordinators | [optional] 
 **with_deleted** | **str**| Include deleted | [optional] 

### Return type

[**OpenAPIAccountsResp**](OpenAPIAccountsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of accounts |  -  |
**0** | List of accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts**
> OpenAPIAccountsResp get_accounts(description=description, deleted=deleted, with_associations=with_associations, with_coordinators=with_coordinators, no_users_are_coords=no_users_are_coords, users_are_coords=users_are_coords)

Get account list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_accounts_resp import OpenAPIAccountsResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    description = 'description_example' # str | CSV description list (optional)
    deleted = 'deleted_example' # str | include deleted associations (optional)
    with_associations = 'with_associations_example' # str | query includes associations (optional)
    with_coordinators = 'with_coordinators_example' # str | query includes coordinators (optional)
    no_users_are_coords = 'no_users_are_coords_example' # str | remove users as coordinators (optional)
    users_are_coords = 'users_are_coords_example' # str | users are coordinators (optional)

    try:
        # Get account list
        api_response = await api_instance.get_accounts(description=description, deleted=deleted, with_associations=with_associations, with_coordinators=with_coordinators, no_users_are_coords=no_users_are_coords, users_are_coords=users_are_coords)
        print("The response of SlurmdbApi->get_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->get_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| CSV description list | [optional] 
 **deleted** | **str**| include deleted associations | [optional] 
 **with_associations** | **str**| query includes associations | [optional] 
 **with_coordinators** | **str**| query includes coordinators | [optional] 
 **no_users_are_coords** | **str**| remove users as coordinators | [optional] 
 **users_are_coords** | **str**| users are coordinators | [optional] 

### Return type

[**OpenAPIAccountsResp**](OpenAPIAccountsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of accounts |  -  |
**0** | List of accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_association**
> OpenAPIAssocsResp get_association(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)

Get association info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_assocs_resp import OpenAPIAssocsResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    account = 'account_example' # str | CSV accounts list (optional)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    default_qos = 'default_qos_example' # str | CSV QOS list (optional)
    include_deleted_associations = 'include_deleted_associations_example' # str |  (optional)
    include_usage = 'include_usage_example' # str |  (optional)
    filter_to_only_defaults = 'filter_to_only_defaults_example' # str |  (optional)
    include_the_raw_qos_or_delta_qos = 'include_the_raw_qos_or_delta_qos_example' # str |  (optional)
    include_sub_acct_information = 'include_sub_acct_information_example' # str |  (optional)
    exclude_parent_id_name = 'exclude_parent_id_name_example' # str |  (optional)
    exclude_limits_from_parents = 'exclude_limits_from_parents_example' # str |  (optional)
    id = 'id_example' # str | CSV ID list (optional)
    parent_account = 'parent_account_example' # str | CSV names of parent account (optional)
    partition = 'partition_example' # str | CSV partition name list (optional)
    qos = 'qos_example' # str | CSV QOS list (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    user = 'user_example' # str | CSV user list (optional)

    try:
        # Get association info
        api_response = await api_instance.get_association(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)
        print("The response of SlurmdbApi->get_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->get_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| CSV accounts list | [optional] 
 **cluster** | **str**| CSV clusters list | [optional] 
 **default_qos** | **str**| CSV QOS list | [optional] 
 **include_deleted_associations** | **str**|  | [optional] 
 **include_usage** | **str**|  | [optional] 
 **filter_to_only_defaults** | **str**|  | [optional] 
 **include_the_raw_qos_or_delta_qos** | **str**|  | [optional] 
 **include_sub_acct_information** | **str**|  | [optional] 
 **exclude_parent_id_name** | **str**|  | [optional] 
 **exclude_limits_from_parents** | **str**|  | [optional] 
 **id** | **str**| CSV ID list | [optional] 
 **parent_account** | **str**| CSV names of parent account | [optional] 
 **partition** | **str**| CSV partition name list | [optional] 
 **qos** | **str**| CSV QOS list | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **user** | **str**| CSV user list | [optional] 

### Return type

[**OpenAPIAssocsResp**](OpenAPIAssocsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of associations |  -  |
**0** | List of associations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_associations**
> OpenAPIAssocsResp get_associations(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)

Get association list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_assocs_resp import OpenAPIAssocsResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    account = 'account_example' # str | CSV accounts list (optional)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    default_qos = 'default_qos_example' # str | CSV QOS list (optional)
    include_deleted_associations = 'include_deleted_associations_example' # str |  (optional)
    include_usage = 'include_usage_example' # str |  (optional)
    filter_to_only_defaults = 'filter_to_only_defaults_example' # str |  (optional)
    include_the_raw_qos_or_delta_qos = 'include_the_raw_qos_or_delta_qos_example' # str |  (optional)
    include_sub_acct_information = 'include_sub_acct_information_example' # str |  (optional)
    exclude_parent_id_name = 'exclude_parent_id_name_example' # str |  (optional)
    exclude_limits_from_parents = 'exclude_limits_from_parents_example' # str |  (optional)
    id = 'id_example' # str | CSV ID list (optional)
    parent_account = 'parent_account_example' # str | CSV names of parent account (optional)
    partition = 'partition_example' # str | CSV partition name list (optional)
    qos = 'qos_example' # str | CSV QOS list (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    user = 'user_example' # str | CSV user list (optional)

    try:
        # Get association list
        api_response = await api_instance.get_associations(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)
        print("The response of SlurmdbApi->get_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->get_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| CSV accounts list | [optional] 
 **cluster** | **str**| CSV clusters list | [optional] 
 **default_qos** | **str**| CSV QOS list | [optional] 
 **include_deleted_associations** | **str**|  | [optional] 
 **include_usage** | **str**|  | [optional] 
 **filter_to_only_defaults** | **str**|  | [optional] 
 **include_the_raw_qos_or_delta_qos** | **str**|  | [optional] 
 **include_sub_acct_information** | **str**|  | [optional] 
 **exclude_parent_id_name** | **str**|  | [optional] 
 **exclude_limits_from_parents** | **str**|  | [optional] 
 **id** | **str**| CSV ID list | [optional] 
 **parent_account** | **str**| CSV names of parent account | [optional] 
 **partition** | **str**| CSV partition name list | [optional] 
 **qos** | **str**| CSV QOS list | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **user** | **str**| CSV user list | [optional] 

### Return type

[**OpenAPIAssocsResp**](OpenAPIAssocsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of associations |  -  |
**0** | List of associations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster**
> OpenAPIClustersResp get_cluster(cluster_name, classification=classification, cluster=cluster, federation=federation, flags=flags, rpc_version=rpc_version, usage_end=usage_end, usage_start=usage_start, with_deleted=with_deleted, with_usage=with_usage)

Get cluster info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_clusters_resp import OpenAPIClustersResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    classification = 'classification_example' # str | Type of machine (optional)
    cluster = 'cluster_example' # str | CSV cluster list (optional)
    federation = 'federation_example' # str | CSV federation list (optional)
    flags = 'flags_example' # str | Query flags (optional)
    rpc_version = 'rpc_version_example' # str | CSV RPC version list (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted clusters (optional)
    with_usage = 'with_usage_example' # str | Include usage (optional)

    try:
        # Get cluster info
        api_response = await api_instance.get_cluster(cluster_name, classification=classification, cluster=cluster, federation=federation, flags=flags, rpc_version=rpc_version, usage_end=usage_end, usage_start=usage_start, with_deleted=with_deleted, with_usage=with_usage)
        print("The response of SlurmdbApi->get_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->get_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **classification** | **str**| Type of machine | [optional] 
 **cluster** | **str**| CSV cluster list | [optional] 
 **federation** | **str**| CSV federation list | [optional] 
 **flags** | **str**| Query flags | [optional] 
 **rpc_version** | **str**| CSV RPC version list | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **with_deleted** | **str**| Include deleted clusters | [optional] 
 **with_usage** | **str**| Include usage | [optional] 

### Return type

[**OpenAPIClustersResp**](OpenAPIClustersResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cluster information |  -  |
**0** | Cluster information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusters**
> OpenAPIClustersResp get_clusters(update_time=update_time)

Get cluster list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_clusters_resp import OpenAPIClustersResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    update_time = 'update_time_example' # str | Query reservations updated more recently than this time (UNIX timestamp) (optional)

    try:
        # Get cluster list
        api_response = await api_instance.get_clusters(update_time=update_time)
        print("The response of SlurmdbApi->get_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->get_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Query reservations updated more recently than this time (UNIX timestamp) | [optional] 

### Return type

[**OpenAPIClustersResp**](OpenAPIClustersResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of clusters |  -  |
**0** | List of clusters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conf**
> OpenAPISlurmdbdConfResp get_conf()

Dump slurmdbd configuration

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_slurmdbd_conf_resp import OpenAPISlurmdbdConfResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)

    try:
        # Dump slurmdbd configuration
        api_response = await api_instance.get_conf()
        print("The response of SlurmdbApi->get_conf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->get_conf: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OpenAPISlurmdbdConfResp**](OpenAPISlurmdbdConfResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | slurmdbd configuration |  -  |
**0** | slurmdbd configuration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config**
> OpenAPISlurmdbdConfigResp get_config()

Dump all configuration information

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_slurmdbd_config_resp import OpenAPISlurmdbdConfigResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)

    try:
        # Dump all configuration information
        api_response = await api_instance.get_config()
        print("The response of SlurmdbApi->get_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->get_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OpenAPISlurmdbdConfigResp**](OpenAPISlurmdbdConfigResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | slurmdbd configuration |  -  |
**0** | slurmdbd configuration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_diag**
> OpenAPISlurmdbdStatsResp get_diag()

Get slurmdb diagnostics

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_slurmdbd_stats_resp import OpenAPISlurmdbdStatsResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)

    try:
        # Get slurmdb diagnostics
        api_response = await api_instance.get_diag()
        print("The response of SlurmdbApi->get_diag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->get_diag: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OpenAPISlurmdbdStatsResp**](OpenAPISlurmdbdStatsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dictionary of statistics |  -  |
**0** | Dictionary of statistics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instance**
> OpenAPIInstancesResp get_instance(cluster=cluster, extra=extra, instance_id=instance_id, instance_type=instance_type, node_list=node_list, time_end=time_end, time_start=time_start)

Get instance info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_instances_resp import OpenAPIInstancesResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    extra = 'extra_example' # str | CSV extra list (optional)
    instance_id = 'instance_id_example' # str | CSV instance_id list (optional)
    instance_type = 'instance_type_example' # str | CSV instance_type list (optional)
    node_list = 'node_list_example' # str | Ranged node string (optional)
    time_end = 'time_end_example' # str | Time end (UNIX timestamp) (optional)
    time_start = 'time_start_example' # str | Time start (UNIX timestamp) (optional)

    try:
        # Get instance info
        api_response = await api_instance.get_instance(cluster=cluster, extra=extra, instance_id=instance_id, instance_type=instance_type, node_list=node_list, time_end=time_end, time_start=time_start)
        print("The response of SlurmdbApi->get_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->get_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| CSV clusters list | [optional] 
 **extra** | **str**| CSV extra list | [optional] 
 **instance_id** | **str**| CSV instance_id list | [optional] 
 **instance_type** | **str**| CSV instance_type list | [optional] 
 **node_list** | **str**| Ranged node string | [optional] 
 **time_end** | **str**| Time end (UNIX timestamp) | [optional] 
 **time_start** | **str**| Time start (UNIX timestamp) | [optional] 

### Return type

[**OpenAPIInstancesResp**](OpenAPIInstancesResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of instances |  -  |
**0** | List of instances |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instances**
> OpenAPIInstancesResp get_instances(cluster=cluster, extra=extra, instance_id=instance_id, instance_type=instance_type, node_list=node_list, time_end=time_end, time_start=time_start)

Get instance list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_instances_resp import OpenAPIInstancesResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    extra = 'extra_example' # str | CSV extra list (optional)
    instance_id = 'instance_id_example' # str | CSV instance_id list (optional)
    instance_type = 'instance_type_example' # str | CSV instance_type list (optional)
    node_list = 'node_list_example' # str | Ranged node string (optional)
    time_end = 'time_end_example' # str | Time end (UNIX timestamp) (optional)
    time_start = 'time_start_example' # str | Time start (UNIX timestamp) (optional)

    try:
        # Get instance list
        api_response = await api_instance.get_instances(cluster=cluster, extra=extra, instance_id=instance_id, instance_type=instance_type, node_list=node_list, time_end=time_end, time_start=time_start)
        print("The response of SlurmdbApi->get_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->get_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| CSV clusters list | [optional] 
 **extra** | **str**| CSV extra list | [optional] 
 **instance_id** | **str**| CSV instance_id list | [optional] 
 **instance_type** | **str**| CSV instance_type list | [optional] 
 **node_list** | **str**| Ranged node string | [optional] 
 **time_end** | **str**| Time end (UNIX timestamp) | [optional] 
 **time_start** | **str**| Time start (UNIX timestamp) | [optional] 

### Return type

[**OpenAPIInstancesResp**](OpenAPIInstancesResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of instances |  -  |
**0** | List of instances |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job**
> OpenAPISlurmdbdJobsResp get_job(job_id)

Get job info

This endpoint may return multiple job entries since job_id is not a unique key - only the tuple (cluster, job_id, start_time) is unique. If the requested job_id is a component of a heterogeneous job all components are returned.

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_slurmdbd_jobs_resp import OpenAPISlurmdbdJobsResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    job_id = 'job_id_example' # str | Job ID

    try:
        # Get job info
        api_response = await api_instance.get_job(job_id)
        print("The response of SlurmdbApi->get_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->get_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID | 

### Return type

[**OpenAPISlurmdbdJobsResp**](OpenAPISlurmdbdJobsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job description |  -  |
**0** | Job description |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobs**
> OpenAPISlurmdbdJobsResp get_jobs(account=account, association=association, cluster=cluster, constraints=constraints, scheduler_unset=scheduler_unset, scheduled_on_submit=scheduled_on_submit, scheduled_by_main=scheduled_by_main, scheduled_by_backfill=scheduled_by_backfill, job_started=job_started, job_altered=job_altered, exit_code=exit_code, show_duplicates=show_duplicates, skip_steps=skip_steps, disable_truncate_usage_time=disable_truncate_usage_time, whole_hetjob=whole_hetjob, disable_whole_hetjob=disable_whole_hetjob, disable_wait_for_result=disable_wait_for_result, usage_time_as_submit_time=usage_time_as_submit_time, show_batch_script=show_batch_script, show_job_environment=show_job_environment, groups=groups, job_name=job_name, partition=partition, qos=qos, reason=reason, reservation=reservation, reservation_id=reservation_id, state=state, step=step, end_time=end_time, start_time=start_time, node=node, users=users, wckey=wckey)

Get job list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_slurmdbd_jobs_resp import OpenAPISlurmdbdJobsResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    account = 'account_example' # str | CSV account list (optional)
    association = 'association_example' # str | CSV association list (optional)
    cluster = 'cluster_example' # str | CSV cluster list (optional)
    constraints = 'constraints_example' # str | CSV constraint list (optional)
    scheduler_unset = 'scheduler_unset_example' # str | Schedule bits not set (optional)
    scheduled_on_submit = 'scheduled_on_submit_example' # str | Job was started on submit (optional)
    scheduled_by_main = 'scheduled_by_main_example' # str | Job was started from main scheduler (optional)
    scheduled_by_backfill = 'scheduled_by_backfill_example' # str | Job was started from backfill (optional)
    job_started = 'job_started_example' # str | Job start RPC was received (optional)
    job_altered = 'job_altered_example' # str | Job record has been altered (optional)
    exit_code = 'exit_code_example' # str | Job exit code (numeric) (optional)
    show_duplicates = 'show_duplicates_example' # str | Include duplicate job entries (optional)
    skip_steps = 'skip_steps_example' # str | Exclude job step details (optional)
    disable_truncate_usage_time = 'disable_truncate_usage_time_example' # str | Do not truncate the time to usage_start and usage_end (optional)
    whole_hetjob = 'whole_hetjob_example' # str | Include details on all hetjob components (optional)
    disable_whole_hetjob = 'disable_whole_hetjob_example' # str | Only show details on specified hetjob components (optional)
    disable_wait_for_result = 'disable_wait_for_result_example' # str | Tell dbd not to wait for the result (optional)
    usage_time_as_submit_time = 'usage_time_as_submit_time_example' # str | Use usage_time as the submit_time of the job (optional)
    show_batch_script = 'show_batch_script_example' # str | Include job script (optional)
    show_job_environment = 'show_job_environment_example' # str | Include job environment (optional)
    groups = 'groups_example' # str | CSV group list (optional)
    job_name = 'job_name_example' # str | CSV job name list (optional)
    partition = 'partition_example' # str | CSV partition name list (optional)
    qos = 'qos_example' # str | CSV QOS name list (optional)
    reason = 'reason_example' # str | CSV reason list (optional)
    reservation = 'reservation_example' # str | CSV reservation name list (optional)
    reservation_id = 'reservation_id_example' # str | CSV reservation ID list (optional)
    state = 'state_example' # str | CSV state list (optional)
    step = 'step_example' # str | CSV step id list (optional)
    end_time = 'end_time_example' # str | Usage end (UNIX timestamp) (optional)
    start_time = 'start_time_example' # str | Usage start (UNIX timestamp) (optional)
    node = 'node_example' # str | Ranged node string where jobs ran (optional)
    users = 'users_example' # str | CSV user name list (optional)
    wckey = 'wckey_example' # str | CSV WCKey list (optional)

    try:
        # Get job list
        api_response = await api_instance.get_jobs(account=account, association=association, cluster=cluster, constraints=constraints, scheduler_unset=scheduler_unset, scheduled_on_submit=scheduled_on_submit, scheduled_by_main=scheduled_by_main, scheduled_by_backfill=scheduled_by_backfill, job_started=job_started, job_altered=job_altered, exit_code=exit_code, show_duplicates=show_duplicates, skip_steps=skip_steps, disable_truncate_usage_time=disable_truncate_usage_time, whole_hetjob=whole_hetjob, disable_whole_hetjob=disable_whole_hetjob, disable_wait_for_result=disable_wait_for_result, usage_time_as_submit_time=usage_time_as_submit_time, show_batch_script=show_batch_script, show_job_environment=show_job_environment, groups=groups, job_name=job_name, partition=partition, qos=qos, reason=reason, reservation=reservation, reservation_id=reservation_id, state=state, step=step, end_time=end_time, start_time=start_time, node=node, users=users, wckey=wckey)
        print("The response of SlurmdbApi->get_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->get_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| CSV account list | [optional] 
 **association** | **str**| CSV association list | [optional] 
 **cluster** | **str**| CSV cluster list | [optional] 
 **constraints** | **str**| CSV constraint list | [optional] 
 **scheduler_unset** | **str**| Schedule bits not set | [optional] 
 **scheduled_on_submit** | **str**| Job was started on submit | [optional] 
 **scheduled_by_main** | **str**| Job was started from main scheduler | [optional] 
 **scheduled_by_backfill** | **str**| Job was started from backfill | [optional] 
 **job_started** | **str**| Job start RPC was received | [optional] 
 **job_altered** | **str**| Job record has been altered | [optional] 
 **exit_code** | **str**| Job exit code (numeric) | [optional] 
 **show_duplicates** | **str**| Include duplicate job entries | [optional] 
 **skip_steps** | **str**| Exclude job step details | [optional] 
 **disable_truncate_usage_time** | **str**| Do not truncate the time to usage_start and usage_end | [optional] 
 **whole_hetjob** | **str**| Include details on all hetjob components | [optional] 
 **disable_whole_hetjob** | **str**| Only show details on specified hetjob components | [optional] 
 **disable_wait_for_result** | **str**| Tell dbd not to wait for the result | [optional] 
 **usage_time_as_submit_time** | **str**| Use usage_time as the submit_time of the job | [optional] 
 **show_batch_script** | **str**| Include job script | [optional] 
 **show_job_environment** | **str**| Include job environment | [optional] 
 **groups** | **str**| CSV group list | [optional] 
 **job_name** | **str**| CSV job name list | [optional] 
 **partition** | **str**| CSV partition name list | [optional] 
 **qos** | **str**| CSV QOS name list | [optional] 
 **reason** | **str**| CSV reason list | [optional] 
 **reservation** | **str**| CSV reservation name list | [optional] 
 **reservation_id** | **str**| CSV reservation ID list | [optional] 
 **state** | **str**| CSV state list | [optional] 
 **step** | **str**| CSV step id list | [optional] 
 **end_time** | **str**| Usage end (UNIX timestamp) | [optional] 
 **start_time** | **str**| Usage start (UNIX timestamp) | [optional] 
 **node** | **str**| Ranged node string where jobs ran | [optional] 
 **users** | **str**| CSV user name list | [optional] 
 **wckey** | **str**| CSV WCKey list | [optional] 

### Return type

[**OpenAPISlurmdbdJobsResp**](OpenAPISlurmdbdJobsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of jobs |  -  |
**0** | List of jobs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ping**
> OpenAPISlurmdbdPingResp get_ping()

ping test

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_slurmdbd_ping_resp import OpenAPISlurmdbdPingResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)

    try:
        # ping test
        api_response = await api_instance.get_ping()
        print("The response of SlurmdbApi->get_ping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->get_ping: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OpenAPISlurmdbdPingResp**](OpenAPISlurmdbdPingResp.md)

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

# **get_qos**
> OpenAPISlurmdbdQosResp get_qos(description=description, include_deleted_qos=include_deleted_qos, id=id, name=name, preempt_mode=preempt_mode)

Get QOS list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_slurmdbd_qos_resp import OpenAPISlurmdbdQosResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    description = 'description_example' # str | CSV description list (optional)
    include_deleted_qos = 'include_deleted_qos_example' # str |  (optional)
    id = 'id_example' # str | CSV QOS id list (optional)
    name = 'name_example' # str | CSV QOS name list (optional)
    preempt_mode = 'preempt_mode_example' # str | PreemptMode used when jobs in this QOS are preempted (optional)

    try:
        # Get QOS list
        api_response = await api_instance.get_qos(description=description, include_deleted_qos=include_deleted_qos, id=id, name=name, preempt_mode=preempt_mode)
        print("The response of SlurmdbApi->get_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->get_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| CSV description list | [optional] 
 **include_deleted_qos** | **str**|  | [optional] 
 **id** | **str**| CSV QOS id list | [optional] 
 **name** | **str**| CSV QOS name list | [optional] 
 **preempt_mode** | **str**| PreemptMode used when jobs in this QOS are preempted | [optional] 

### Return type

[**OpenAPISlurmdbdQosResp**](OpenAPISlurmdbdQosResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of QOS |  -  |
**0** | List of QOS |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_qos**
> OpenAPISlurmdbdQosResp get_single_qos(qos, with_deleted=with_deleted)

Get QOS info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_slurmdbd_qos_resp import OpenAPISlurmdbdQosResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    qos = 'qos_example' # str | QOS name
    with_deleted = 'with_deleted_example' # str | Query includes deleted QOS (optional)

    try:
        # Get QOS info
        api_response = await api_instance.get_single_qos(qos, with_deleted=with_deleted)
        print("The response of SlurmdbApi->get_single_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->get_single_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qos** | **str**| QOS name | 
 **with_deleted** | **str**| Query includes deleted QOS | [optional] 

### Return type

[**OpenAPISlurmdbdQosResp**](OpenAPISlurmdbdQosResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | QOS information |  -  |
**0** | QOS information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tres**
> OpenAPITresResp get_tres()

Get TRES info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_tres_resp import OpenAPITresResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)

    try:
        # Get TRES info
        api_response = await api_instance.get_tres()
        print("The response of SlurmdbApi->get_tres:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->get_tres: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OpenAPITresResp**](OpenAPITresResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TRES |  -  |
**0** | List of TRES |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> OpenAPIUsersResp get_user(name, with_deleted=with_deleted, with_assocs=with_assocs, with_coords=with_coords, with_wckeys=with_wckeys)

Get user info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_users_resp import OpenAPIUsersResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    name = 'name_example' # str | User name
    with_deleted = 'with_deleted_example' # str | Include deleted users (optional)
    with_assocs = 'with_assocs_example' # str | Include associations (optional)
    with_coords = 'with_coords_example' # str | Include coordinators (optional)
    with_wckeys = 'with_wckeys_example' # str | Include WCKeys (optional)

    try:
        # Get user info
        api_response = await api_instance.get_user(name, with_deleted=with_deleted, with_assocs=with_assocs, with_coords=with_coords, with_wckeys=with_wckeys)
        print("The response of SlurmdbApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| User name | 
 **with_deleted** | **str**| Include deleted users | [optional] 
 **with_assocs** | **str**| Include associations | [optional] 
 **with_coords** | **str**| Include coordinators | [optional] 
 **with_wckeys** | **str**| Include WCKeys | [optional] 

### Return type

[**OpenAPIUsersResp**](OpenAPIUsersResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users |  -  |
**0** | List of users |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> OpenAPIUsersResp get_users(admin_level=admin_level, default_account=default_account, default_wckey=default_wckey, with_assocs=with_assocs, with_coords=with_coords, with_deleted=with_deleted, with_wckeys=with_wckeys, without_defaults=without_defaults)

Get user list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_users_resp import OpenAPIUsersResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    admin_level = 'admin_level_example' # str | Administrator level (optional)
    default_account = 'default_account_example' # str | CSV default account list (optional)
    default_wckey = 'default_wckey_example' # str | CSV default WCKey list (optional)
    with_assocs = 'with_assocs_example' # str | With associations (optional)
    with_coords = 'with_coords_example' # str | With coordinators (optional)
    with_deleted = 'with_deleted_example' # str | With deleted (optional)
    with_wckeys = 'with_wckeys_example' # str | With WCKeys (optional)
    without_defaults = 'without_defaults_example' # str | Exclude defaults (optional)

    try:
        # Get user list
        api_response = await api_instance.get_users(admin_level=admin_level, default_account=default_account, default_wckey=default_wckey, with_assocs=with_assocs, with_coords=with_coords, with_deleted=with_deleted, with_wckeys=with_wckeys, without_defaults=without_defaults)
        print("The response of SlurmdbApi->get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->get_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_level** | **str**| Administrator level | [optional] 
 **default_account** | **str**| CSV default account list | [optional] 
 **default_wckey** | **str**| CSV default WCKey list | [optional] 
 **with_assocs** | **str**| With associations | [optional] 
 **with_coords** | **str**| With coordinators | [optional] 
 **with_deleted** | **str**| With deleted | [optional] 
 **with_wckeys** | **str**| With WCKeys | [optional] 
 **without_defaults** | **str**| Exclude defaults | [optional] 

### Return type

[**OpenAPIUsersResp**](OpenAPIUsersResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users |  -  |
**0** | List of users |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wckey**
> OpenAPIWckeyResp get_wckey(id)

Get wckey info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_wckey_resp import OpenAPIWckeyResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    id = 'id_example' # str | WCKey ID

    try:
        # Get wckey info
        api_response = await api_instance.get_wckey(id)
        print("The response of SlurmdbApi->get_wckey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->get_wckey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| WCKey ID | 

### Return type

[**OpenAPIWckeyResp**](OpenAPIWckeyResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Description of wckey |  -  |
**0** | Description of wckey |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wckeys**
> OpenAPIWckeyResp get_wckeys(cluster=cluster, id=id, name=name, only_defaults=only_defaults, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted)

Get wckey list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_wckey_resp import OpenAPIWckeyResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    cluster = 'cluster_example' # str | CSV cluster name list (optional)
    id = 'id_example' # str | CSV ID list (optional)
    name = 'name_example' # str | CSV name list (optional)
    only_defaults = 'only_defaults_example' # str | Only query defaults (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    user = 'user_example' # str | CSV user list (optional)
    with_usage = 'with_usage_example' # str | Include usage (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted WCKeys (optional)

    try:
        # Get wckey list
        api_response = await api_instance.get_wckeys(cluster=cluster, id=id, name=name, only_defaults=only_defaults, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted)
        print("The response of SlurmdbApi->get_wckeys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->get_wckeys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| CSV cluster name list | [optional] 
 **id** | **str**| CSV ID list | [optional] 
 **name** | **str**| CSV name list | [optional] 
 **only_defaults** | **str**| Only query defaults | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **user** | **str**| CSV user list | [optional] 
 **with_usage** | **str**| Include usage | [optional] 
 **with_deleted** | **str**| Include deleted WCKeys | [optional] 

### Return type

[**OpenAPIWckeyResp**](OpenAPIWckeyResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of wckeys |  -  |
**0** | List of wckeys |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_accounts**
> OpenAPIResp post_accounts(open_api_accounts_resp=open_api_accounts_resp)

Add/update list of accounts

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_accounts_resp import OpenAPIAccountsResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    open_api_accounts_resp = slurpy.v0045.asyncio.OpenAPIAccountsResp() # OpenAPIAccountsResp | Description of accounts to update/create (optional)

    try:
        # Add/update list of accounts
        api_response = await api_instance.post_accounts(open_api_accounts_resp=open_api_accounts_resp)
        print("The response of SlurmdbApi->post_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->post_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_api_accounts_resp** | [**OpenAPIAccountsResp**](OpenAPIAccountsResp.md)| Description of accounts to update/create | [optional] 

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
**200** | Status of account update request |  -  |
**0** | Status of account update request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_accounts_association**
> OpenAPIAccountsAddCondRespStr post_accounts_association(open_api_accounts_add_cond_resp=open_api_accounts_add_cond_resp)

Add accounts with conditional association

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_accounts_add_cond_resp import OpenAPIAccountsAddCondResp
from slurpy.v0045.asyncio.models.open_api_accounts_add_cond_resp_str import OpenAPIAccountsAddCondRespStr
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    open_api_accounts_add_cond_resp = slurpy.v0045.asyncio.OpenAPIAccountsAddCondResp() # OpenAPIAccountsAddCondResp | Add list of accounts with conditional association (optional)

    try:
        # Add accounts with conditional association
        api_response = await api_instance.post_accounts_association(open_api_accounts_add_cond_resp=open_api_accounts_add_cond_resp)
        print("The response of SlurmdbApi->post_accounts_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->post_accounts_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_api_accounts_add_cond_resp** | [**OpenAPIAccountsAddCondResp**](OpenAPIAccountsAddCondResp.md)| Add list of accounts with conditional association | [optional] 

### Return type

[**OpenAPIAccountsAddCondRespStr**](OpenAPIAccountsAddCondRespStr.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of account addition request |  -  |
**0** | Status of account addition request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_associations**
> OpenAPIResp post_associations(open_api_assocs_resp=open_api_assocs_resp)

Set associations info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_assocs_resp import OpenAPIAssocsResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    open_api_assocs_resp = slurpy.v0045.asyncio.OpenAPIAssocsResp() # OpenAPIAssocsResp | Job description (optional)

    try:
        # Set associations info
        api_response = await api_instance.post_associations(open_api_assocs_resp=open_api_assocs_resp)
        print("The response of SlurmdbApi->post_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->post_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_api_assocs_resp** | [**OpenAPIAssocsResp**](OpenAPIAssocsResp.md)| Job description | [optional] 

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
**200** | status of associations update |  -  |
**0** | status of associations update |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_clusters**
> OpenAPIResp post_clusters(update_time=update_time, open_api_clusters_resp=open_api_clusters_resp)

Get cluster list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_clusters_resp import OpenAPIClustersResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    update_time = 'update_time_example' # str | Query reservations updated more recently than this time (UNIX timestamp) (optional)
    open_api_clusters_resp = slurpy.v0045.asyncio.OpenAPIClustersResp() # OpenAPIClustersResp | Cluster add or update descriptions (optional)

    try:
        # Get cluster list
        api_response = await api_instance.post_clusters(update_time=update_time, open_api_clusters_resp=open_api_clusters_resp)
        print("The response of SlurmdbApi->post_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->post_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Query reservations updated more recently than this time (UNIX timestamp) | [optional] 
 **open_api_clusters_resp** | [**OpenAPIClustersResp**](OpenAPIClustersResp.md)| Cluster add or update descriptions | [optional] 

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
**200** | Result of modify clusters request |  -  |
**0** | Result of modify clusters request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_config**
> OpenAPIResp post_config(open_api_slurmdbd_config_resp=open_api_slurmdbd_config_resp)

Load all configuration information

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_resp import OpenAPIResp
from slurpy.v0045.asyncio.models.open_api_slurmdbd_config_resp import OpenAPISlurmdbdConfigResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    open_api_slurmdbd_config_resp = slurpy.v0045.asyncio.OpenAPISlurmdbdConfigResp() # OpenAPISlurmdbdConfigResp | Add or update config (optional)

    try:
        # Load all configuration information
        api_response = await api_instance.post_config(open_api_slurmdbd_config_resp=open_api_slurmdbd_config_resp)
        print("The response of SlurmdbApi->post_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->post_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_api_slurmdbd_config_resp** | [**OpenAPISlurmdbdConfigResp**](OpenAPISlurmdbdConfigResp.md)| Add or update config | [optional] 

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
**200** | slurmdbd configuration |  -  |
**0** | slurmdbd configuration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_job**
> OpenAPIJobModifyResp post_job(job_id, job_modify=job_modify)

Update job

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.job_modify import JobModify
from slurpy.v0045.asyncio.models.open_api_job_modify_resp import OpenAPIJobModifyResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    job_id = 'job_id_example' # str | Job ID
    job_modify = slurpy.v0045.asyncio.JobModify() # JobModify | Job update description (optional)

    try:
        # Update job
        api_response = await api_instance.post_job(job_id, job_modify=job_modify)
        print("The response of SlurmdbApi->post_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->post_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID | 
 **job_modify** | [**JobModify**](JobModify.md)| Job update description | [optional] 

### Return type

[**OpenAPIJobModifyResp**](OpenAPIJobModifyResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job update results |  -  |
**0** | Job update results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_jobs**
> OpenAPIJobModifyResp post_jobs(open_api_job_modify_req=open_api_job_modify_req)

Update jobs

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_job_modify_req import OpenAPIJobModifyReq
from slurpy.v0045.asyncio.models.open_api_job_modify_resp import OpenAPIJobModifyResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    open_api_job_modify_req = slurpy.v0045.asyncio.OpenAPIJobModifyReq() # OpenAPIJobModifyReq | Job update description (optional)

    try:
        # Update jobs
        api_response = await api_instance.post_jobs(open_api_job_modify_req=open_api_job_modify_req)
        print("The response of SlurmdbApi->post_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->post_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_api_job_modify_req** | [**OpenAPIJobModifyReq**](OpenAPIJobModifyReq.md)| Job update description | [optional] 

### Return type

[**OpenAPIJobModifyResp**](OpenAPIJobModifyResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job update results |  -  |
**0** | Job update results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_qos**
> OpenAPIResp post_qos(description=description, include_deleted_qos=include_deleted_qos, id=id, name=name, preempt_mode=preempt_mode, open_api_slurmdbd_qos_resp=open_api_slurmdbd_qos_resp)

Add or update QOSs

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_resp import OpenAPIResp
from slurpy.v0045.asyncio.models.open_api_slurmdbd_qos_resp import OpenAPISlurmdbdQosResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    description = 'description_example' # str | CSV description list (optional)
    include_deleted_qos = 'include_deleted_qos_example' # str |  (optional)
    id = 'id_example' # str | CSV QOS id list (optional)
    name = 'name_example' # str | CSV QOS name list (optional)
    preempt_mode = 'preempt_mode_example' # str | PreemptMode used when jobs in this QOS are preempted (optional)
    open_api_slurmdbd_qos_resp = slurpy.v0045.asyncio.OpenAPISlurmdbdQosResp() # OpenAPISlurmdbdQosResp | Description of QOS to add or update (optional)

    try:
        # Add or update QOSs
        api_response = await api_instance.post_qos(description=description, include_deleted_qos=include_deleted_qos, id=id, name=name, preempt_mode=preempt_mode, open_api_slurmdbd_qos_resp=open_api_slurmdbd_qos_resp)
        print("The response of SlurmdbApi->post_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->post_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| CSV description list | [optional] 
 **include_deleted_qos** | **str**|  | [optional] 
 **id** | **str**| CSV QOS id list | [optional] 
 **name** | **str**| CSV QOS name list | [optional] 
 **preempt_mode** | **str**| PreemptMode used when jobs in this QOS are preempted | [optional] 
 **open_api_slurmdbd_qos_resp** | [**OpenAPISlurmdbdQosResp**](OpenAPISlurmdbdQosResp.md)| Description of QOS to add or update | [optional] 

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
**200** | QOS update response |  -  |
**0** | QOS update response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tres**
> OpenAPIResp post_tres(open_api_tres_resp=open_api_tres_resp)

Add TRES

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_resp import OpenAPIResp
from slurpy.v0045.asyncio.models.open_api_tres_resp import OpenAPITresResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    open_api_tres_resp = slurpy.v0045.asyncio.OpenAPITresResp() # OpenAPITresResp | TRES descriptions. Only works in developer mode. (optional)

    try:
        # Add TRES
        api_response = await api_instance.post_tres(open_api_tres_resp=open_api_tres_resp)
        print("The response of SlurmdbApi->post_tres:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->post_tres: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_api_tres_resp** | [**OpenAPITresResp**](OpenAPITresResp.md)| TRES descriptions. Only works in developer mode. | [optional] 

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
**200** | TRES update result |  -  |
**0** | TRES update result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users**
> OpenAPIResp post_users(open_api_users_resp=open_api_users_resp)

Update users

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_resp import OpenAPIResp
from slurpy.v0045.asyncio.models.open_api_users_resp import OpenAPIUsersResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    open_api_users_resp = slurpy.v0045.asyncio.OpenAPIUsersResp() # OpenAPIUsersResp | add or update user (optional)

    try:
        # Update users
        api_response = await api_instance.post_users(open_api_users_resp=open_api_users_resp)
        print("The response of SlurmdbApi->post_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->post_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_api_users_resp** | [**OpenAPIUsersResp**](OpenAPIUsersResp.md)| add or update user | [optional] 

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
**200** | Status of user update request |  -  |
**0** | Status of user update request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_association**
> OpenAPIUsersAddCondRespStr post_users_association(update_time=update_time, flags=flags, open_api_users_add_cond_resp=open_api_users_add_cond_resp)

Add users with conditional association

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_users_add_cond_resp import OpenAPIUsersAddCondResp
from slurpy.v0045.asyncio.models.open_api_users_add_cond_resp_str import OpenAPIUsersAddCondRespStr
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    update_time = 'update_time_example' # str | Query partitions updated more recently than this time (UNIX timestamp) (optional)
    flags = 'flags_example' # str | Query flags (optional)
    open_api_users_add_cond_resp = slurpy.v0045.asyncio.OpenAPIUsersAddCondResp() # OpenAPIUsersAddCondResp | Create users with conditional association (optional)

    try:
        # Add users with conditional association
        api_response = await api_instance.post_users_association(update_time=update_time, flags=flags, open_api_users_add_cond_resp=open_api_users_add_cond_resp)
        print("The response of SlurmdbApi->post_users_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->post_users_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Query partitions updated more recently than this time (UNIX timestamp) | [optional] 
 **flags** | **str**| Query flags | [optional] 
 **open_api_users_add_cond_resp** | [**OpenAPIUsersAddCondResp**](OpenAPIUsersAddCondResp.md)| Create users with conditional association | [optional] 

### Return type

[**OpenAPIUsersAddCondRespStr**](OpenAPIUsersAddCondRespStr.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add list of users with conditional association |  -  |
**0** | Add list of users with conditional association |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_wckeys**
> OpenAPIResp post_wckeys(cluster=cluster, id=id, name=name, only_defaults=only_defaults, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted, open_api_wckey_resp=open_api_wckey_resp)

Add or update wckeys

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045.asyncio
from slurpy.v0045.asyncio.models.open_api_resp import OpenAPIResp
from slurpy.v0045.asyncio.models.open_api_wckey_resp import OpenAPIWckeyResp
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
    api_instance = slurpy.v0045.asyncio.SlurmdbApi(api_client)
    cluster = 'cluster_example' # str | CSV cluster name list (optional)
    id = 'id_example' # str | CSV ID list (optional)
    name = 'name_example' # str | CSV name list (optional)
    only_defaults = 'only_defaults_example' # str | Only query defaults (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    user = 'user_example' # str | CSV user list (optional)
    with_usage = 'with_usage_example' # str | Include usage (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted WCKeys (optional)
    open_api_wckey_resp = slurpy.v0045.asyncio.OpenAPIWckeyResp() # OpenAPIWckeyResp | wckeys description (optional)

    try:
        # Add or update wckeys
        api_response = await api_instance.post_wckeys(cluster=cluster, id=id, name=name, only_defaults=only_defaults, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted, open_api_wckey_resp=open_api_wckey_resp)
        print("The response of SlurmdbApi->post_wckeys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->post_wckeys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| CSV cluster name list | [optional] 
 **id** | **str**| CSV ID list | [optional] 
 **name** | **str**| CSV name list | [optional] 
 **only_defaults** | **str**| Only query defaults | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **user** | **str**| CSV user list | [optional] 
 **with_usage** | **str**| Include usage | [optional] 
 **with_deleted** | **str**| Include deleted WCKeys | [optional] 
 **open_api_wckey_resp** | [**OpenAPIWckeyResp**](OpenAPIWckeyResp.md)| wckeys description | [optional] 

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
**200** | Result of wckey addition or update request |  -  |
**0** | Result of wckey addition or update request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

