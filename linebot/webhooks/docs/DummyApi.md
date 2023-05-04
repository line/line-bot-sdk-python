# linebot.webhooks.DummyApi

All URIs are relative to *https://example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**callback**](DummyApi.md#callback) | **POST** /callback | 


# **callback**
> str callback(callback_request)



This is the dummy endpoint to generate the model classes

### Example

```python
import time
import os
import linebot.webhooks
from linebot.webhooks.models.callback_request import CallbackRequest
from linebot.webhooks.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.webhooks.Configuration(
    host = "https://example.com"
)


# Enter a context with an instance of the API client
with linebot.webhooks.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.webhooks.DummyApi(api_client)
    callback_request = linebot.webhooks.CallbackRequest() # CallbackRequest | 

    try:
        api_response = api_instance.callback(callback_request)
        print("The response of DummyApi->callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DummyApi->callback: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **callback_request** | [**CallbackRequest**](CallbackRequest.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

