# linebot.v3.shop.Shop

All URIs are relative to *https://api.line.me*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mission_sticker_v3**](Shop.md#mission_sticker_v3) | **POST** /shop/v3/mission | 


# **mission_sticker_v3**
> mission_sticker_v3(mission_sticker_request)



Sends a mission sticker.

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.shop
from linebot.v3.shop.models.mission_sticker_request import MissionStickerRequest
from linebot.v3.shop.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.shop.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.shop.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.shop.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.shop.Shop(api_client)
    mission_sticker_request = linebot.v3.shop.MissionStickerRequest() # MissionStickerRequest | 

    try:
        api_instance.mission_sticker_v3(mission_sticker_request)
    except Exception as e:
        print("Exception when calling Shop->mission_sticker_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mission_sticker_request** | [**MissionStickerRequest**](MissionStickerRequest.md)|  | 

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
**200** | Returns status code 200 and an empty response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

