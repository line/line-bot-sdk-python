# linebot.v3.liff.Liff

All URIs are relative to *https://api.line.me*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_liff_app**](Liff.md#add_liff_app) | **POST** /liff/v1/apps | 
[**delete_liff_app**](Liff.md#delete_liff_app) | **DELETE** /liff/v1/apps/{liffId} | Delete LIFF app from a channel
[**get_all_liff_apps**](Liff.md#get_all_liff_apps) | **GET** /liff/v1/apps | Get all LIFF apps
[**update_liff_app**](Liff.md#update_liff_app) | **PUT** /liff/v1/apps/{liffId} | 


# **add_liff_app**
> AddLiffAppResponse add_liff_app(add_liff_app_request)



Adding the LIFF app to a channel

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.liff
from linebot.v3.liff.models.add_liff_app_request import AddLiffAppRequest
from linebot.v3.liff.models.add_liff_app_response import AddLiffAppResponse
from linebot.v3.liff.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.liff.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.liff.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.liff.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.liff.Liff(api_client)
    add_liff_app_request = linebot.v3.liff.AddLiffAppRequest() # AddLiffAppRequest | 

    try:
        api_response = api_instance.add_liff_app(add_liff_app_request)
        print("The response of Liff->add_liff_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Liff->add_liff_app: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_liff_app_request** | [**AddLiffAppRequest**](AddLiffAppRequest.md)|  | 

### Return type

[**AddLiffAppResponse**](AddLiffAppResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | This status code means one of the following:  - The request contains an invalid value. - The maximum number of LIFF apps that can be added to the channel has been reached.  |  -  |
**401** | Authentication failed.   |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_liff_app**
> delete_liff_app(liff_id)

Delete LIFF app from a channel

Deletes a LIFF app from a channel. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.liff
from linebot.v3.liff.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.liff.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.liff.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.liff.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.liff.Liff(api_client)
    liff_id = 'liff_id_example' # str | ID of the LIFF app to be updated

    try:
        # Delete LIFF app from a channel
        api_instance.delete_liff_app(liff_id)
    except Exception as e:
        print("Exception when calling Liff->delete_liff_app: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **liff_id** | **str**| ID of the LIFF app to be updated | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication failed.  |  -  |
**404** | This status code means one of the following: - The specified LIFF app does not exist. - The specified LIFF app has been added to another channel.   |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_liff_apps**
> GetAllLiffAppsResponse get_all_liff_apps()

Get all LIFF apps

Gets information on all the LIFF apps added to the channel.

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.liff
from linebot.v3.liff.models.get_all_liff_apps_response import GetAllLiffAppsResponse
from linebot.v3.liff.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.liff.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.liff.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.liff.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.liff.Liff(api_client)

    try:
        # Get all LIFF apps
        api_response = api_instance.get_all_liff_apps()
        print("The response of Liff->get_all_liff_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Liff->get_all_liff_apps: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAllLiffAppsResponse**](GetAllLiffAppsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication failed.  |  -  |
**404** | There is no LIFF app on the channel.     |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_liff_app**
> update_liff_app(liff_id, update_liff_app_request)



Update LIFF app settings

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.liff
from linebot.v3.liff.models.update_liff_app_request import UpdateLiffAppRequest
from linebot.v3.liff.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.liff.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.liff.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.liff.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.liff.Liff(api_client)
    liff_id = 'liff_id_example' # str | ID of the LIFF app to be updated
    update_liff_app_request = linebot.v3.liff.UpdateLiffAppRequest() # UpdateLiffAppRequest | 

    try:
        api_instance.update_liff_app(liff_id, update_liff_app_request)
    except Exception as e:
        print("Exception when calling Liff->update_liff_app: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **liff_id** | **str**| ID of the LIFF app to be updated | 
 **update_liff_app_request** | [**UpdateLiffAppRequest**](UpdateLiffAppRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The request contains an invalid value.  |  -  |
**401** | Authentication failed.  |  -  |
**404** | This status code means one of the following: - The specified LIFF app does not exist. - The specified LIFF app has been added to another channel.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

