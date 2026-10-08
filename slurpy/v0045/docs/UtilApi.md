# slurpy.v0045.UtilApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_hostlist**](UtilApi.md#post_hostlist) | **POST** /util/v0.0.45/hostlist | Convert an array of host names into hostlist expression
[**post_hostnames**](UtilApi.md#post_hostnames) | **POST** /util/v0.0.45/hostnames | Convert a hostlist expression into array of host names


# **post_hostlist**
> OpenAPIHostlistReqResp post_hostlist(open_api_hostnames_req_resp=open_api_hostnames_req_resp)

Convert an array of host names into hostlist expression

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045
from slurpy.v0045.models.open_api_hostlist_req_resp import OpenAPIHostlistReqResp
from slurpy.v0045.models.open_api_hostnames_req_resp import OpenAPIHostnamesReqResp
from slurpy.v0045.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.Configuration(
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
configuration = slurpy.v0045.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurpy.v0045.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.UtilApi(api_client)
    open_api_hostnames_req_resp = slurpy.v0045.OpenAPIHostnamesReqResp() # OpenAPIHostnamesReqResp | Array of host names (optional)

    try:
        # Convert an array of host names into hostlist expression
        api_response = api_instance.post_hostlist(open_api_hostnames_req_resp=open_api_hostnames_req_resp)
        print("The response of UtilApi->post_hostlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilApi->post_hostlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_api_hostnames_req_resp** | [**OpenAPIHostnamesReqResp**](OpenAPIHostnamesReqResp.md)| Array of host names | [optional] 

### Return type

[**OpenAPIHostlistReqResp**](OpenAPIHostlistReqResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hostlist expression |  -  |
**0** | Hostlist expression |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_hostnames**
> OpenAPIHostnamesReqResp post_hostnames(open_api_hostlist_req_resp=open_api_hostlist_req_resp)

Convert a hostlist expression into array of host names

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0045
from slurpy.v0045.models.open_api_hostlist_req_resp import OpenAPIHostlistReqResp
from slurpy.v0045.models.open_api_hostnames_req_resp import OpenAPIHostnamesReqResp
from slurpy.v0045.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0045.Configuration(
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
configuration = slurpy.v0045.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurpy.v0045.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0045.UtilApi(api_client)
    open_api_hostlist_req_resp = slurpy.v0045.OpenAPIHostlistReqResp() # OpenAPIHostlistReqResp | Hostlist expression (optional)

    try:
        # Convert a hostlist expression into array of host names
        api_response = api_instance.post_hostnames(open_api_hostlist_req_resp=open_api_hostlist_req_resp)
        print("The response of UtilApi->post_hostnames:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilApi->post_hostnames: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_api_hostlist_req_resp** | [**OpenAPIHostlistReqResp**](OpenAPIHostlistReqResp.md)| Hostlist expression | [optional] 

### Return type

[**OpenAPIHostnamesReqResp**](OpenAPIHostnamesReqResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of host names |  -  |
**0** | Array of host names |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

