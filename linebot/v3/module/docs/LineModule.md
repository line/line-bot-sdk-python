# linebot.v3.module.LineModule

All URIs are relative to *https://api.line.me*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acquire_chat_control**](LineModule.md#acquire_chat_control) | **POST** /v2/bot/chat/{chatId}/control/acquire | 
[**detach_module**](LineModule.md#detach_module) | **POST** /v2/bot/channel/detach | 
[**get_modules**](LineModule.md#get_modules) | **GET** /v2/bot/list | 
[**release_chat_control**](LineModule.md#release_chat_control) | **POST** /v2/bot/chat/{chatId}/control/release | 


# **acquire_chat_control**
> acquire_chat_control(chat_id, acquire_chat_control_request=acquire_chat_control_request)



If the Standby Channel wants to take the initiative (Chat Control), it calls the Acquire Control API. The channel that was previously an Active Channel will automatically switch to a Standby Channel. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.module
from linebot.v3.module.models.acquire_chat_control_request import AcquireChatControlRequest
from linebot.v3.module.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.module.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.module.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.module.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.module.LineModule(api_client)
    chat_id = 'chat_id_example' # str | The `userId`, `roomId`, or `groupId`
    acquire_chat_control_request = linebot.v3.module.AcquireChatControlRequest() # AcquireChatControlRequest |  (optional)

    try:
        api_instance.acquire_chat_control(chat_id, acquire_chat_control_request=acquire_chat_control_request)
    except Exception as e:
        print("Exception when calling LineModule->acquire_chat_control: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_id** | **str**| The &#x60;userId&#x60;, &#x60;roomId&#x60;, or &#x60;groupId&#x60; | 
 **acquire_chat_control_request** | [**AcquireChatControlRequest**](AcquireChatControlRequest.md)|  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_module**
> detach_module(detach_module_request=detach_module_request)



The module channel admin calls the Detach API to detach the module channel from a LINE Official Account.

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.module
from linebot.v3.module.models.detach_module_request import DetachModuleRequest
from linebot.v3.module.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.module.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.module.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.module.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.module.LineModule(api_client)
    detach_module_request = linebot.v3.module.DetachModuleRequest() # DetachModuleRequest |  (optional)

    try:
        api_instance.detach_module(detach_module_request=detach_module_request)
    except Exception as e:
        print("Exception when calling LineModule->detach_module: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **detach_module_request** | [**DetachModuleRequest**](DetachModuleRequest.md)|  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_modules**
> GetModulesResponse get_modules(start=start, limit=limit)



Gets a list of basic information about the bots of multiple LINE Official Accounts that have attached module channels.

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.module
from linebot.v3.module.models.get_modules_response import GetModulesResponse
from linebot.v3.module.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.module.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.module.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.module.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.module.LineModule(api_client)
    start = 'start_example' # str | Value of the continuation token found in the next property of the JSON object returned in the response. If you can't get all basic information about the bots in one request, include this parameter to get the remaining array.  (optional)
    limit = 100 # int | Specify the maximum number of bots that you get basic information from. The default value is 100. Max value: 100  (optional) (default to 100)

    try:
        api_response = api_instance.get_modules(start=start, limit=limit)
        print("The response of LineModule->get_modules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LineModule->get_modules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **str**| Value of the continuation token found in the next property of the JSON object returned in the response. If you can&#39;t get all basic information about the bots in one request, include this parameter to get the remaining array.  | [optional] 
 **limit** | **int**| Specify the maximum number of bots that you get basic information from. The default value is 100. Max value: 100  | [optional] [default to 100]

### Return type

[**GetModulesResponse**](GetModulesResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_chat_control**
> release_chat_control(chat_id)



To return the initiative (Chat Control) of Active Channel to Primary Channel, call the Release Control API. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.module
from linebot.v3.module.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.module.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.module.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.module.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.module.LineModule(api_client)
    chat_id = 'chat_id_example' # str | The `userId`, `roomId`, or `groupId`

    try:
        api_instance.release_chat_control(chat_id)
    except Exception as e:
        print("Exception when calling LineModule->release_chat_control: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_id** | **str**| The &#x60;userId&#x60;, &#x60;roomId&#x60;, or &#x60;groupId&#x60; | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

