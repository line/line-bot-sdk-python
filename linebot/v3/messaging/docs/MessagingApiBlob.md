# linebot.v3.messaging.MessagingApiBlob

All URIs are relative to *https://api.line.me*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_message_content**](MessagingApiBlob.md#get_message_content) | **GET** /v2/bot/message/{messageId}/content | 
[**get_message_content_preview**](MessagingApiBlob.md#get_message_content_preview) | **GET** /v2/bot/message/{messageId}/content/preview | 
[**get_message_content_transcoding_by_message_id**](MessagingApiBlob.md#get_message_content_transcoding_by_message_id) | **GET** /v2/bot/message/{messageId}/content/transcoding | 
[**get_rich_menu_image**](MessagingApiBlob.md#get_rich_menu_image) | **GET** /v2/bot/richmenu/{richMenuId}/content | 
[**set_rich_menu_image**](MessagingApiBlob.md#set_rich_menu_image) | **POST** /v2/bot/richmenu/{richMenuId}/content | 


# **get_message_content**
> bytearray get_message_content(message_id)



Download image, video, and audio data sent from users.

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.messaging
from linebot.v3.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.messaging.MessagingApiBlob(api_client)
    message_id = 'message_id_example' # str | Message ID of video or audio

    try:
        api_response = api_instance.get_message_content(message_id)
        print("The response of MessagingApiBlob->get_message_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiBlob->get_message_content: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| Message ID of video or audio | 

### Return type

**bytearray**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_content_preview**
> bytearray get_message_content_preview(message_id)



Get a preview image of the image or video

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.messaging
from linebot.v3.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.messaging.MessagingApiBlob(api_client)
    message_id = 'message_id_example' # str | Message ID of image or video

    try:
        api_response = api_instance.get_message_content_preview(message_id)
        print("The response of MessagingApiBlob->get_message_content_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiBlob->get_message_content_preview: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| Message ID of image or video | 

### Return type

**bytearray**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_content_transcoding_by_message_id**
> GetMessageContentTranscodingResponse get_message_content_transcoding_by_message_id(message_id)



Verify the preparation status of a video or audio for getting

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.messaging
from linebot.v3.messaging.models.get_message_content_transcoding_response import GetMessageContentTranscodingResponse
from linebot.v3.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.messaging.MessagingApiBlob(api_client)
    message_id = 'message_id_example' # str | Message ID of video or audio

    try:
        api_response = api_instance.get_message_content_transcoding_by_message_id(message_id)
        print("The response of MessagingApiBlob->get_message_content_transcoding_by_message_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiBlob->get_message_content_transcoding_by_message_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| Message ID of video or audio | 

### Return type

[**GetMessageContentTranscodingResponse**](GetMessageContentTranscodingResponse.md)

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

# **get_rich_menu_image**
> bytearray get_rich_menu_image(rich_menu_id)



Download rich menu image.

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.messaging
from linebot.v3.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.messaging.MessagingApiBlob(api_client)
    rich_menu_id = 'rich_menu_id_example' # str | ID of the rich menu with the image to be downloaded

    try:
        api_response = api_instance.get_rich_menu_image(rich_menu_id)
        print("The response of MessagingApiBlob->get_rich_menu_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiBlob->get_rich_menu_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rich_menu_id** | **str**| ID of the rich menu with the image to be downloaded | 

### Return type

**bytearray**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_rich_menu_image**
> set_rich_menu_image(rich_menu_id, body=body)



Upload rich menu image

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.messaging
from linebot.v3.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.messaging.MessagingApiBlob(api_client)
    rich_menu_id = 'rich_menu_id_example' # str | The ID of the rich menu to attach the image to
    body = None # bytearray |  (optional)

    try:
        api_instance.set_rich_menu_image(rich_menu_id, body=body)
    except Exception as e:
        print("Exception when calling MessagingApiBlob->set_rich_menu_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rich_menu_id** | **str**| The ID of the rich menu to attach the image to | 
 **body** | **bytearray**|  | [optional] 

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

