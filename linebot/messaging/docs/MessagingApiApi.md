# linebot.messaging.MessagingApiApi

All URIs are relative to *https://api.line.me*

Method | HTTP request | Description
------------- | ------------- | -------------
[**audience_match**](MessagingApiApi.md#audience_match) | **POST** /bot/ad/multicast/phone | 
[**broadcast**](MessagingApiApi.md#broadcast) | **POST** /v2/bot/message/broadcast | 
[**cancel_default_rich_menu**](MessagingApiApi.md#cancel_default_rich_menu) | **DELETE** /v2/bot/user/all/richmenu | 
[**create_rich_menu**](MessagingApiApi.md#create_rich_menu) | **POST** /v2/bot/richmenu | 
[**create_rich_menu_alias**](MessagingApiApi.md#create_rich_menu_alias) | **POST** /v2/bot/richmenu/alias | 
[**delete_rich_menu**](MessagingApiApi.md#delete_rich_menu) | **DELETE** /v2/bot/richmenu/{richMenuId} | 
[**delete_rich_menu_alias**](MessagingApiApi.md#delete_rich_menu_alias) | **DELETE** /v2/bot/richmenu/alias/{richMenuAliasId} | 
[**get_ad_phone_message_statistics**](MessagingApiApi.md#get_ad_phone_message_statistics) | **GET** /v2/bot/message/delivery/ad_phone | 
[**get_aggregation_unit_name_list**](MessagingApiApi.md#get_aggregation_unit_name_list) | **GET** /v2/bot/message/aggregation/list | 
[**get_aggregation_unit_usage**](MessagingApiApi.md#get_aggregation_unit_usage) | **GET** /v2/bot/message/aggregation/info | 
[**get_bot_info**](MessagingApiApi.md#get_bot_info) | **GET** /v2/bot/info | 
[**get_default_rich_menu_id**](MessagingApiApi.md#get_default_rich_menu_id) | **GET** /v2/bot/user/all/richmenu | 
[**get_followers**](MessagingApiApi.md#get_followers) | **GET** /v2/bot/followers/ids | 
[**get_group_member_count**](MessagingApiApi.md#get_group_member_count) | **GET** /v2/bot/group/{groupId}/members/count | 
[**get_group_member_profile**](MessagingApiApi.md#get_group_member_profile) | **GET** /v2/bot/group/{groupId}/member/{userId} | 
[**get_group_members_ids**](MessagingApiApi.md#get_group_members_ids) | **GET** /v2/bot/group/{groupId}/members/ids | 
[**get_group_summary**](MessagingApiApi.md#get_group_summary) | **GET** /v2/bot/group/{groupId}/summary | 
[**get_message_quota**](MessagingApiApi.md#get_message_quota) | **GET** /v2/bot/message/quota | 
[**get_message_quota_consumption**](MessagingApiApi.md#get_message_quota_consumption) | **GET** /v2/bot/message/quota/consumption | 
[**get_narrowcast_progress**](MessagingApiApi.md#get_narrowcast_progress) | **GET** /v2/bot/message/progress/narrowcast | 
[**get_number_of_sent_broadcast_messages**](MessagingApiApi.md#get_number_of_sent_broadcast_messages) | **GET** /v2/bot/message/delivery/broadcast | 
[**get_number_of_sent_multicast_messages**](MessagingApiApi.md#get_number_of_sent_multicast_messages) | **GET** /v2/bot/message/delivery/multicast | 
[**get_number_of_sent_push_messages**](MessagingApiApi.md#get_number_of_sent_push_messages) | **GET** /v2/bot/message/delivery/push | 
[**get_number_of_sent_reply_messages**](MessagingApiApi.md#get_number_of_sent_reply_messages) | **GET** /v2/bot/message/delivery/reply | 
[**get_pnp_message_statistics**](MessagingApiApi.md#get_pnp_message_statistics) | **GET** /v2/bot/message/delivery/pnp | 
[**get_profile**](MessagingApiApi.md#get_profile) | **GET** /v2/bot/profile/{userId} | 
[**get_rich_menu**](MessagingApiApi.md#get_rich_menu) | **GET** /v2/bot/richmenu/{richMenuId} | 
[**get_rich_menu_alias**](MessagingApiApi.md#get_rich_menu_alias) | **GET** /v2/bot/richmenu/alias/{richMenuAliasId} | 
[**get_rich_menu_alias_list**](MessagingApiApi.md#get_rich_menu_alias_list) | **GET** /v2/bot/richmenu/alias/list | 
[**get_rich_menu_id_of_user**](MessagingApiApi.md#get_rich_menu_id_of_user) | **GET** /v2/bot/user/{userId}/richmenu | 
[**get_rich_menu_list**](MessagingApiApi.md#get_rich_menu_list) | **GET** /v2/bot/richmenu/list | 
[**get_room_member_count**](MessagingApiApi.md#get_room_member_count) | **GET** /v2/bot/room/{roomId}/members/count | 
[**get_room_member_profile**](MessagingApiApi.md#get_room_member_profile) | **GET** /v2/bot/room/{roomId}/member/{userId} | 
[**get_room_members_ids**](MessagingApiApi.md#get_room_members_ids) | **GET** /v2/bot/room/{roomId}/members/ids | 
[**get_webhook_endpoint**](MessagingApiApi.md#get_webhook_endpoint) | **GET** /v2/bot/channel/webhook/endpoint | 
[**issue_link_token**](MessagingApiApi.md#issue_link_token) | **POST** /v2/bot/user/{userId}/linkToken | 
[**leave_group**](MessagingApiApi.md#leave_group) | **POST** /v2/bot/group/{groupId}/leave | 
[**leave_room**](MessagingApiApi.md#leave_room) | **POST** /v2/bot/room/{roomId}/leave | 
[**link_rich_menu_id_to_user**](MessagingApiApi.md#link_rich_menu_id_to_user) | **POST** /v2/bot/user/{userId}/richmenu/{richMenuId} | 
[**link_rich_menu_id_to_users**](MessagingApiApi.md#link_rich_menu_id_to_users) | **POST** /v2/bot/richmenu/bulk/link | 
[**mark_messages_as_read**](MessagingApiApi.md#mark_messages_as_read) | **POST** /v2/bot/message/markAsRead | 
[**multicast**](MessagingApiApi.md#multicast) | **POST** /v2/bot/message/multicast | 
[**narrowcast**](MessagingApiApi.md#narrowcast) | **POST** /v2/bot/message/narrowcast | 
[**push_message**](MessagingApiApi.md#push_message) | **POST** /v2/bot/message/push | 
[**push_messages_by_phone**](MessagingApiApi.md#push_messages_by_phone) | **POST** /bot/pnp/push | 
[**reply_message**](MessagingApiApi.md#reply_message) | **POST** /v2/bot/message/reply | 
[**set_default_rich_menu**](MessagingApiApi.md#set_default_rich_menu) | **POST** /v2/bot/user/all/richmenu/{richMenuId} | 
[**set_webhook_endpoint**](MessagingApiApi.md#set_webhook_endpoint) | **PUT** /v2/bot/channel/webhook/endpoint | 
[**test_webhook_endpoint**](MessagingApiApi.md#test_webhook_endpoint) | **POST** /v2/bot/channel/webhook/test | 
[**unlink_rich_menu_id_from_user**](MessagingApiApi.md#unlink_rich_menu_id_from_user) | **DELETE** /v2/bot/user/{userId}/richmenu | 
[**unlink_rich_menu_id_from_users**](MessagingApiApi.md#unlink_rich_menu_id_from_users) | **POST** /v2/bot/richmenu/bulk/unlink | 
[**update_rich_menu_alias**](MessagingApiApi.md#update_rich_menu_alias) | **POST** /v2/bot/richmenu/alias/{richMenuAliasId} | 
[**validate_broadcast**](MessagingApiApi.md#validate_broadcast) | **POST** /v2/bot/message/validate/broadcast | 
[**validate_multicast**](MessagingApiApi.md#validate_multicast) | **POST** /v2/bot/message/validate/multicast | 
[**validate_narrowcast**](MessagingApiApi.md#validate_narrowcast) | **POST** /v2/bot/message/validate/narrowcast | 
[**validate_push**](MessagingApiApi.md#validate_push) | **POST** /v2/bot/message/validate/push | 
[**validate_reply**](MessagingApiApi.md#validate_reply) | **POST** /v2/bot/message/validate/reply | 
[**validate_rich_menu_object**](MessagingApiApi.md#validate_rich_menu_object) | **POST** /v2/bot/richmenu/validate | 


# **audience_match**
> audience_match(audience_match_messages_request)



Send a message using phone number

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.audience_match_messages_request import AudienceMatchMessagesRequest
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    audience_match_messages_request = linebot.messaging.AudienceMatchMessagesRequest() # AudienceMatchMessagesRequest | 

    try:
        api_instance.audience_match(audience_match_messages_request)
    except Exception as e:
        print("Exception when calling MessagingApiApi->audience_match: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_match_messages_request** | [**AudienceMatchMessagesRequest**](AudienceMatchMessagesRequest.md)|  | 

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

# **broadcast**
> broadcast(broadcast_request, x_line_retry_key=x_line_retry_key)



Sends a message to multiple users at any time.

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.broadcast_request import BroadcastRequest
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    broadcast_request = linebot.messaging.BroadcastRequest() # BroadcastRequest | 
    x_line_retry_key = 'x_line_retry_key_example' # str | Retry key. Specifies the UUID in hexadecimal format (e.g., `123e4567-e89b-12d3-a456-426614174000`) generated by any method. The retry key isn't generated by LINE. Each developer must generate their own retry key.  (optional)

    try:
        api_instance.broadcast(broadcast_request, x_line_retry_key=x_line_retry_key)
    except Exception as e:
        print("Exception when calling MessagingApiApi->broadcast: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broadcast_request** | [**BroadcastRequest**](BroadcastRequest.md)|  | 
 **x_line_retry_key** | **str**| Retry key. Specifies the UUID in hexadecimal format (e.g., &#x60;123e4567-e89b-12d3-a456-426614174000&#x60;) generated by any method. The retry key isn&#39;t generated by LINE. Each developer must generate their own retry key.  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_default_rich_menu**
> cancel_default_rich_menu()



Cancel default rich menu

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)

    try:
        api_instance.cancel_default_rich_menu()
    except Exception as e:
        print("Exception when calling MessagingApiApi->cancel_default_rich_menu: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **create_rich_menu**
> RichMenuIdResponse create_rich_menu(rich_menu_request)



Create rich menu

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.rich_menu_id_response import RichMenuIdResponse
from linebot.messaging.models.rich_menu_request import RichMenuRequest
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    rich_menu_request = linebot.messaging.RichMenuRequest() # RichMenuRequest | 

    try:
        api_response = api_instance.create_rich_menu(rich_menu_request)
        print("The response of MessagingApiApi->create_rich_menu:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->create_rich_menu: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rich_menu_request** | [**RichMenuRequest**](RichMenuRequest.md)|  | 

### Return type

[**RichMenuIdResponse**](RichMenuIdResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_rich_menu_alias**
> create_rich_menu_alias(create_rich_menu_alias_request)



Create rich menu alias

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.create_rich_menu_alias_request import CreateRichMenuAliasRequest
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    create_rich_menu_alias_request = linebot.messaging.CreateRichMenuAliasRequest() # CreateRichMenuAliasRequest | 

    try:
        api_instance.create_rich_menu_alias(create_rich_menu_alias_request)
    except Exception as e:
        print("Exception when calling MessagingApiApi->create_rich_menu_alias: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_rich_menu_alias_request** | [**CreateRichMenuAliasRequest**](CreateRichMenuAliasRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rich_menu**
> delete_rich_menu(rich_menu_id)



Deletes a rich menu.

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    rich_menu_id = 'rich_menu_id_example' # str | ID of a rich menu

    try:
        api_instance.delete_rich_menu(rich_menu_id)
    except Exception as e:
        print("Exception when calling MessagingApiApi->delete_rich_menu: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rich_menu_id** | **str**| ID of a rich menu | 

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

# **delete_rich_menu_alias**
> delete_rich_menu_alias(rich_menu_alias_id)



Delete rich menu alias

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    rich_menu_alias_id = 'rich_menu_alias_id_example' # str | Rich menu alias ID that you want to delete.

    try:
        api_instance.delete_rich_menu_alias(rich_menu_alias_id)
    except Exception as e:
        print("Exception when calling MessagingApiApi->delete_rich_menu_alias: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rich_menu_alias_id** | **str**| Rich menu alias ID that you want to delete. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ad_phone_message_statistics**
> NumberOfMessagesResponse get_ad_phone_message_statistics(var_date)



Get result of message delivery using phone number

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.number_of_messages_response import NumberOfMessagesResponse
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    var_date = 'var_date_example' # str | Date the message was sent  Format: `yyyyMMdd` (e.g. `20190831`) Time Zone: UTC+9 

    try:
        api_response = api_instance.get_ad_phone_message_statistics(var_date)
        print("The response of MessagingApiApi->get_ad_phone_message_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->get_ad_phone_message_statistics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **str**| Date the message was sent  Format: &#x60;yyyyMMdd&#x60; (e.g. &#x60;20190831&#x60;) Time Zone: UTC+9  | 

### Return type

[**NumberOfMessagesResponse**](NumberOfMessagesResponse.md)

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

# **get_aggregation_unit_name_list**
> GetAggregationUnitNameListResponse get_aggregation_unit_name_list(limit=limit, start=start)



Get name list of units used this month

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.get_aggregation_unit_name_list_response import GetAggregationUnitNameListResponse
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    limit = 'limit_example' # str | The maximum number of aggregation units you can get per request.  (optional)
    start = 'start_example' # str | Value of the continuation token found in the next property of the JSON object returned in the response. If you can't get all the aggregation units in one request, include this parameter to get the remaining array.  (optional)

    try:
        api_response = api_instance.get_aggregation_unit_name_list(limit=limit, start=start)
        print("The response of MessagingApiApi->get_aggregation_unit_name_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->get_aggregation_unit_name_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| The maximum number of aggregation units you can get per request.  | [optional] 
 **start** | **str**| Value of the continuation token found in the next property of the JSON object returned in the response. If you can&#39;t get all the aggregation units in one request, include this parameter to get the remaining array.  | [optional] 

### Return type

[**GetAggregationUnitNameListResponse**](GetAggregationUnitNameListResponse.md)

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

# **get_aggregation_unit_usage**
> GetAggregationUnitUsageResponse get_aggregation_unit_usage()



Get number of units used this month

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.get_aggregation_unit_usage_response import GetAggregationUnitUsageResponse
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)

    try:
        api_response = api_instance.get_aggregation_unit_usage()
        print("The response of MessagingApiApi->get_aggregation_unit_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->get_aggregation_unit_usage: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAggregationUnitUsageResponse**](GetAggregationUnitUsageResponse.md)

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

# **get_bot_info**
> BotInfoResponse get_bot_info()



Get bot info

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.bot_info_response import BotInfoResponse
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)

    try:
        api_response = api_instance.get_bot_info()
        print("The response of MessagingApiApi->get_bot_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->get_bot_info: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**BotInfoResponse**](BotInfoResponse.md)

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

# **get_default_rich_menu_id**
> RichMenuIdResponse get_default_rich_menu_id()



Gets the ID of the default rich menu set with the Messaging API.

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.rich_menu_id_response import RichMenuIdResponse
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)

    try:
        api_response = api_instance.get_default_rich_menu_id()
        print("The response of MessagingApiApi->get_default_rich_menu_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->get_default_rich_menu_id: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**RichMenuIdResponse**](RichMenuIdResponse.md)

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

# **get_followers**
> GetFollowersResponse get_followers(start=start, limit=limit)



Get a list of users who added your LINE Official Account as a friend

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.get_followers_response import GetFollowersResponse
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    start = 'start_example' # str | Value of the continuation token found in the next property of the JSON object returned in the response. Include this parameter to get the next array of user IDs.  (optional)
    limit = 300 # int | The maximum number of user IDs to retrieve in a single request. (optional) (default to 300)

    try:
        api_response = api_instance.get_followers(start=start, limit=limit)
        print("The response of MessagingApiApi->get_followers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->get_followers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **str**| Value of the continuation token found in the next property of the JSON object returned in the response. Include this parameter to get the next array of user IDs.  | [optional] 
 **limit** | **int**| The maximum number of user IDs to retrieve in a single request. | [optional] [default to 300]

### Return type

[**GetFollowersResponse**](GetFollowersResponse.md)

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

# **get_group_member_count**
> GroupMemberCountResponse get_group_member_count(group_id)



Get number of users in a group chat

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.group_member_count_response import GroupMemberCountResponse
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    group_id = 'group_id_example' # str | Group ID

    try:
        api_response = api_instance.get_group_member_count(group_id)
        print("The response of MessagingApiApi->get_group_member_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->get_group_member_count: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Group ID | 

### Return type

[**GroupMemberCountResponse**](GroupMemberCountResponse.md)

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

# **get_group_member_profile**
> UserProfileResponse get_group_member_profile(group_id, user_id)



Get group chat member profile

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.user_profile_response import UserProfileResponse
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    group_id = 'group_id_example' # str | Group ID
    user_id = 'user_id_example' # str | User ID

    try:
        api_response = api_instance.get_group_member_profile(group_id, user_id)
        print("The response of MessagingApiApi->get_group_member_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->get_group_member_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Group ID | 
 **user_id** | **str**| User ID | 

### Return type

[**UserProfileResponse**](UserProfileResponse.md)

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

# **get_group_members_ids**
> MembersIdsResponse get_group_members_ids(group_id, start=start)



Get group chat member user IDs

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.members_ids_response import MembersIdsResponse
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    group_id = 'group_id_example' # str | Group ID
    start = 'start_example' # str | Value of the continuation token found in the `next` property of the JSON object returned in the response. Include this parameter to get the next array of user IDs for the members of the group.  (optional)

    try:
        api_response = api_instance.get_group_members_ids(group_id, start=start)
        print("The response of MessagingApiApi->get_group_members_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->get_group_members_ids: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Group ID | 
 **start** | **str**| Value of the continuation token found in the &#x60;next&#x60; property of the JSON object returned in the response. Include this parameter to get the next array of user IDs for the members of the group.  | [optional] 

### Return type

[**MembersIdsResponse**](MembersIdsResponse.md)

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

# **get_group_summary**
> GroupSummaryResponse get_group_summary(group_id)



Get group chat summary

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.group_summary_response import GroupSummaryResponse
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    group_id = 'group_id_example' # str | Group ID

    try:
        api_response = api_instance.get_group_summary(group_id)
        print("The response of MessagingApiApi->get_group_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->get_group_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Group ID | 

### Return type

[**GroupSummaryResponse**](GroupSummaryResponse.md)

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

# **get_message_quota**
> MessageQuotaResponse get_message_quota()



Gets the target limit for sending messages in the current month. The total number of the free messages and the additional messages is returned.

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.message_quota_response import MessageQuotaResponse
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)

    try:
        api_response = api_instance.get_message_quota()
        print("The response of MessagingApiApi->get_message_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->get_message_quota: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**MessageQuotaResponse**](MessageQuotaResponse.md)

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

# **get_message_quota_consumption**
> QuotaConsumptionResponse get_message_quota_consumption()



Gets the number of messages sent in the current month.

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.quota_consumption_response import QuotaConsumptionResponse
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)

    try:
        api_response = api_instance.get_message_quota_consumption()
        print("The response of MessagingApiApi->get_message_quota_consumption:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->get_message_quota_consumption: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**QuotaConsumptionResponse**](QuotaConsumptionResponse.md)

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

# **get_narrowcast_progress**
> NarrowcastProgressResponse get_narrowcast_progress(request_id)



Gets the status of a narrowcast message.

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.narrowcast_progress_response import NarrowcastProgressResponse
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    request_id = 'request_id_example' # str | The narrowcast message's request ID. Each Messaging API request has a request ID.

    try:
        api_response = api_instance.get_narrowcast_progress(request_id)
        print("The response of MessagingApiApi->get_narrowcast_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->get_narrowcast_progress: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| The narrowcast message&#39;s request ID. Each Messaging API request has a request ID. | 

### Return type

[**NarrowcastProgressResponse**](NarrowcastProgressResponse.md)

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

# **get_number_of_sent_broadcast_messages**
> NumberOfMessagesResponse get_number_of_sent_broadcast_messages(var_date)



Get number of sent broadcast messages

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.number_of_messages_response import NumberOfMessagesResponse
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    var_date = 'var_date_example' # str | Date the messages were sent  Format: yyyyMMdd (e.g. 20191231) Timezone: UTC+9 

    try:
        api_response = api_instance.get_number_of_sent_broadcast_messages(var_date)
        print("The response of MessagingApiApi->get_number_of_sent_broadcast_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->get_number_of_sent_broadcast_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **str**| Date the messages were sent  Format: yyyyMMdd (e.g. 20191231) Timezone: UTC+9  | 

### Return type

[**NumberOfMessagesResponse**](NumberOfMessagesResponse.md)

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

# **get_number_of_sent_multicast_messages**
> NumberOfMessagesResponse get_number_of_sent_multicast_messages(var_date)



Get number of sent multicast messages

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.number_of_messages_response import NumberOfMessagesResponse
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    var_date = 'var_date_example' # str | Date the messages were sent  Format: `yyyyMMdd` (e.g. `20191231`) Timezone: UTC+9 

    try:
        api_response = api_instance.get_number_of_sent_multicast_messages(var_date)
        print("The response of MessagingApiApi->get_number_of_sent_multicast_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->get_number_of_sent_multicast_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **str**| Date the messages were sent  Format: &#x60;yyyyMMdd&#x60; (e.g. &#x60;20191231&#x60;) Timezone: UTC+9  | 

### Return type

[**NumberOfMessagesResponse**](NumberOfMessagesResponse.md)

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

# **get_number_of_sent_push_messages**
> NumberOfMessagesResponse get_number_of_sent_push_messages(var_date)



Get number of sent push messages

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.number_of_messages_response import NumberOfMessagesResponse
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    var_date = 'var_date_example' # str | Date the messages were sent  Format: `yyyyMMdd` (e.g. `20191231`) Timezone: UTC+9 

    try:
        api_response = api_instance.get_number_of_sent_push_messages(var_date)
        print("The response of MessagingApiApi->get_number_of_sent_push_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->get_number_of_sent_push_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **str**| Date the messages were sent  Format: &#x60;yyyyMMdd&#x60; (e.g. &#x60;20191231&#x60;) Timezone: UTC+9  | 

### Return type

[**NumberOfMessagesResponse**](NumberOfMessagesResponse.md)

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

# **get_number_of_sent_reply_messages**
> NumberOfMessagesResponse get_number_of_sent_reply_messages(var_date)



Get number of sent reply messages

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.number_of_messages_response import NumberOfMessagesResponse
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    var_date = 'var_date_example' # str | Date the messages were sent  Format: `yyyyMMdd` (e.g. `20191231`) Timezone: UTC+9 

    try:
        api_response = api_instance.get_number_of_sent_reply_messages(var_date)
        print("The response of MessagingApiApi->get_number_of_sent_reply_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->get_number_of_sent_reply_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **str**| Date the messages were sent  Format: &#x60;yyyyMMdd&#x60; (e.g. &#x60;20191231&#x60;) Timezone: UTC+9  | 

### Return type

[**NumberOfMessagesResponse**](NumberOfMessagesResponse.md)

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

# **get_pnp_message_statistics**
> NumberOfMessagesResponse get_pnp_message_statistics(var_date)



Get number of sent LINE notification messages　

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.number_of_messages_response import NumberOfMessagesResponse
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    var_date = 'var_date_example' # str | Date the message was sent  Format: `yyyyMMdd` (Example:`20211231`) Time zone: UTC+9 

    try:
        api_response = api_instance.get_pnp_message_statistics(var_date)
        print("The response of MessagingApiApi->get_pnp_message_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->get_pnp_message_statistics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **str**| Date the message was sent  Format: &#x60;yyyyMMdd&#x60; (Example:&#x60;20211231&#x60;) Time zone: UTC+9  | 

### Return type

[**NumberOfMessagesResponse**](NumberOfMessagesResponse.md)

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

# **get_profile**
> UserProfileResponse get_profile(user_id)



Get profile

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.user_profile_response import UserProfileResponse
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    user_id = 'user_id_example' # str | User ID

    try:
        api_response = api_instance.get_profile(user_id)
        print("The response of MessagingApiApi->get_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->get_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID | 

### Return type

[**UserProfileResponse**](UserProfileResponse.md)

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

# **get_rich_menu**
> RichMenuResponse get_rich_menu(rich_menu_id)



Gets a rich menu via a rich menu ID.

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.rich_menu_response import RichMenuResponse
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    rich_menu_id = 'rich_menu_id_example' # str | ID of a rich menu

    try:
        api_response = api_instance.get_rich_menu(rich_menu_id)
        print("The response of MessagingApiApi->get_rich_menu:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->get_rich_menu: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rich_menu_id** | **str**| ID of a rich menu | 

### Return type

[**RichMenuResponse**](RichMenuResponse.md)

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

# **get_rich_menu_alias**
> RichMenuAliasResponse get_rich_menu_alias(rich_menu_alias_id)



Get rich menu alias information

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.rich_menu_alias_response import RichMenuAliasResponse
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    rich_menu_alias_id = 'rich_menu_alias_id_example' # str | The rich menu alias ID whose information you want to obtain.

    try:
        api_response = api_instance.get_rich_menu_alias(rich_menu_alias_id)
        print("The response of MessagingApiApi->get_rich_menu_alias:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->get_rich_menu_alias: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rich_menu_alias_id** | **str**| The rich menu alias ID whose information you want to obtain. | 

### Return type

[**RichMenuAliasResponse**](RichMenuAliasResponse.md)

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

# **get_rich_menu_alias_list**
> RichMenuAliasListResponse get_rich_menu_alias_list()



Get list of rich menu alias

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.rich_menu_alias_list_response import RichMenuAliasListResponse
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)

    try:
        api_response = api_instance.get_rich_menu_alias_list()
        print("The response of MessagingApiApi->get_rich_menu_alias_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->get_rich_menu_alias_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**RichMenuAliasListResponse**](RichMenuAliasListResponse.md)

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

# **get_rich_menu_id_of_user**
> RichMenuIdResponse get_rich_menu_id_of_user(user_id)



Get rich menu ID of user

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.rich_menu_id_response import RichMenuIdResponse
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    user_id = 'user_id_example' # str | User ID. Found in the `source` object of webhook event objects. Do not use the LINE ID used in LINE.

    try:
        api_response = api_instance.get_rich_menu_id_of_user(user_id)
        print("The response of MessagingApiApi->get_rich_menu_id_of_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->get_rich_menu_id_of_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID. Found in the &#x60;source&#x60; object of webhook event objects. Do not use the LINE ID used in LINE. | 

### Return type

[**RichMenuIdResponse**](RichMenuIdResponse.md)

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

# **get_rich_menu_list**
> RichMenuListResponse get_rich_menu_list()



Get rich menu list

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.rich_menu_list_response import RichMenuListResponse
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)

    try:
        api_response = api_instance.get_rich_menu_list()
        print("The response of MessagingApiApi->get_rich_menu_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->get_rich_menu_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**RichMenuListResponse**](RichMenuListResponse.md)

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

# **get_room_member_count**
> RoomMemberCountResponse get_room_member_count(room_id)



Get number of users in a multi-person chat

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.room_member_count_response import RoomMemberCountResponse
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    room_id = 'room_id_example' # str | Room ID

    try:
        api_response = api_instance.get_room_member_count(room_id)
        print("The response of MessagingApiApi->get_room_member_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->get_room_member_count: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **str**| Room ID | 

### Return type

[**RoomMemberCountResponse**](RoomMemberCountResponse.md)

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

# **get_room_member_profile**
> UserProfileResponse get_room_member_profile(room_id, user_id)



Get multi-person chat member profile

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.user_profile_response import UserProfileResponse
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    room_id = 'room_id_example' # str | Room ID
    user_id = 'user_id_example' # str | User ID

    try:
        api_response = api_instance.get_room_member_profile(room_id, user_id)
        print("The response of MessagingApiApi->get_room_member_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->get_room_member_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **str**| Room ID | 
 **user_id** | **str**| User ID | 

### Return type

[**UserProfileResponse**](UserProfileResponse.md)

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

# **get_room_members_ids**
> MembersIdsResponse get_room_members_ids(room_id, start=start)



Get multi-person chat member user IDs

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.members_ids_response import MembersIdsResponse
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    room_id = 'room_id_example' # str | Room ID
    start = 'start_example' # str | Value of the continuation token found in the `next` property of the JSON object returned in the response. Include this parameter to get the next array of user IDs for the members of the group.  (optional)

    try:
        api_response = api_instance.get_room_members_ids(room_id, start=start)
        print("The response of MessagingApiApi->get_room_members_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->get_room_members_ids: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **str**| Room ID | 
 **start** | **str**| Value of the continuation token found in the &#x60;next&#x60; property of the JSON object returned in the response. Include this parameter to get the next array of user IDs for the members of the group.  | [optional] 

### Return type

[**MembersIdsResponse**](MembersIdsResponse.md)

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

# **get_webhook_endpoint**
> GetWebhookEndpointResponse get_webhook_endpoint()



Get webhook endpoint information

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.get_webhook_endpoint_response import GetWebhookEndpointResponse
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)

    try:
        api_response = api_instance.get_webhook_endpoint()
        print("The response of MessagingApiApi->get_webhook_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->get_webhook_endpoint: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetWebhookEndpointResponse**](GetWebhookEndpointResponse.md)

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

# **issue_link_token**
> IssueLinkTokenResponse issue_link_token(user_id)



Issue link token

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.issue_link_token_response import IssueLinkTokenResponse
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    user_id = 'user_id_example' # str | User ID for the LINE account to be linked. Found in the `source` object of account link event objects. Do not use the LINE ID used in LINE. 

    try:
        api_response = api_instance.issue_link_token(user_id)
        print("The response of MessagingApiApi->issue_link_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->issue_link_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID for the LINE account to be linked. Found in the &#x60;source&#x60; object of account link event objects. Do not use the LINE ID used in LINE.  | 

### Return type

[**IssueLinkTokenResponse**](IssueLinkTokenResponse.md)

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

# **leave_group**
> leave_group(group_id)



Leave group chat

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    group_id = 'group_id_example' # str | Group ID

    try:
        api_instance.leave_group(group_id)
    except Exception as e:
        print("Exception when calling MessagingApiApi->leave_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Group ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leave_room**
> leave_room(room_id)



Leave multi-person chat

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    room_id = 'room_id_example' # str | Room ID

    try:
        api_instance.leave_room(room_id)
    except Exception as e:
        print("Exception when calling MessagingApiApi->leave_room: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **str**| Room ID | 

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

# **link_rich_menu_id_to_user**
> link_rich_menu_id_to_user(user_id, rich_menu_id)



Link rich menu to user.

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    user_id = 'user_id_example' # str | User ID. Found in the `source` object of webhook event objects. Do not use the LINE ID used in LINE.
    rich_menu_id = 'rich_menu_id_example' # str | ID of a rich menu

    try:
        api_instance.link_rich_menu_id_to_user(user_id, rich_menu_id)
    except Exception as e:
        print("Exception when calling MessagingApiApi->link_rich_menu_id_to_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID. Found in the &#x60;source&#x60; object of webhook event objects. Do not use the LINE ID used in LINE. | 
 **rich_menu_id** | **str**| ID of a rich menu | 

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

# **link_rich_menu_id_to_users**
> link_rich_menu_id_to_users(rich_menu_bulk_link_request)



Link rich menu to multiple users

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.rich_menu_bulk_link_request import RichMenuBulkLinkRequest
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    rich_menu_bulk_link_request = linebot.messaging.RichMenuBulkLinkRequest() # RichMenuBulkLinkRequest | 

    try:
        api_instance.link_rich_menu_id_to_users(rich_menu_bulk_link_request)
    except Exception as e:
        print("Exception when calling MessagingApiApi->link_rich_menu_id_to_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rich_menu_bulk_link_request** | [**RichMenuBulkLinkRequest**](RichMenuBulkLinkRequest.md)|  | 

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
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_messages_as_read**
> mark_messages_as_read(mark_messages_as_read_request)



Mark messages from users as read

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.mark_messages_as_read_request import MarkMessagesAsReadRequest
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    mark_messages_as_read_request = {"chat":{"userId":"Uxxxxxxxxxxxxxxxxxx"}} # MarkMessagesAsReadRequest | 

    try:
        api_instance.mark_messages_as_read(mark_messages_as_read_request)
    except Exception as e:
        print("Exception when calling MessagingApiApi->mark_messages_as_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mark_messages_as_read_request** | [**MarkMessagesAsReadRequest**](MarkMessagesAsReadRequest.md)|  | 

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

# **multicast**
> multicast(multicast_request, x_line_retry_key=x_line_retry_key)



An API that efficiently sends the same message to multiple user IDs. You can't send messages to group chats or multi-person chats.

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.multicast_request import MulticastRequest
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    multicast_request = linebot.messaging.MulticastRequest() # MulticastRequest | 
    x_line_retry_key = 'x_line_retry_key_example' # str | Retry key. Specifies the UUID in hexadecimal format (e.g., `123e4567-e89b-12d3-a456-426614174000`) generated by any method. The retry key isn't generated by LINE. Each developer must generate their own retry key.  (optional)

    try:
        api_instance.multicast(multicast_request, x_line_retry_key=x_line_retry_key)
    except Exception as e:
        print("Exception when calling MessagingApiApi->multicast: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multicast_request** | [**MulticastRequest**](MulticastRequest.md)|  | 
 **x_line_retry_key** | **str**| Retry key. Specifies the UUID in hexadecimal format (e.g., &#x60;123e4567-e89b-12d3-a456-426614174000&#x60;) generated by any method. The retry key isn&#39;t generated by LINE. Each developer must generate their own retry key.  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **narrowcast**
> narrowcast(narrowcast_request, x_line_retry_key=x_line_retry_key)



Send narrowcast message

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.narrowcast_request import NarrowcastRequest
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    narrowcast_request = linebot.messaging.NarrowcastRequest() # NarrowcastRequest | 
    x_line_retry_key = 'x_line_retry_key_example' # str | Retry key. Specifies the UUID in hexadecimal format (e.g., `123e4567-e89b-12d3-a456-426614174000`) generated by any method. The retry key isn't generated by LINE. Each developer must generate their own retry key.  (optional)

    try:
        api_instance.narrowcast(narrowcast_request, x_line_retry_key=x_line_retry_key)
    except Exception as e:
        print("Exception when calling MessagingApiApi->narrowcast: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **narrowcast_request** | [**NarrowcastRequest**](NarrowcastRequest.md)|  | 
 **x_line_retry_key** | **str**| Retry key. Specifies the UUID in hexadecimal format (e.g., &#x60;123e4567-e89b-12d3-a456-426614174000&#x60;) generated by any method. The retry key isn&#39;t generated by LINE. Each developer must generate their own retry key.  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **push_message**
> push_message(push_message_request, x_line_retry_key=x_line_retry_key)



Sends a message to a user, group chat, or multi-person chat at any time.

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.push_message_request import PushMessageRequest
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    push_message_request = linebot.messaging.PushMessageRequest() # PushMessageRequest | 
    x_line_retry_key = 'x_line_retry_key_example' # str | Retry key. Specifies the UUID in hexadecimal format (e.g., `123e4567-e89b-12d3-a456-426614174000`) generated by any method. The retry key isn't generated by LINE. Each developer must generate their own retry key.  (optional)

    try:
        api_instance.push_message(push_message_request, x_line_retry_key=x_line_retry_key)
    except Exception as e:
        print("Exception when calling MessagingApiApi->push_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **push_message_request** | [**PushMessageRequest**](PushMessageRequest.md)|  | 
 **x_line_retry_key** | **str**| Retry key. Specifies the UUID in hexadecimal format (e.g., &#x60;123e4567-e89b-12d3-a456-426614174000&#x60;) generated by any method. The retry key isn&#39;t generated by LINE. Each developer must generate their own retry key.  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **push_messages_by_phone**
> push_messages_by_phone(pnp_messages_request, x_line_delivery_tag=x_line_delivery_tag)



Send LINE notification message

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.pnp_messages_request import PnpMessagesRequest
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    pnp_messages_request = linebot.messaging.PnpMessagesRequest() # PnpMessagesRequest | 
    x_line_delivery_tag = 'x_line_delivery_tag_example' # str | String returned in the delivery.data property of the delivery completion event via Webhook. (optional)

    try:
        api_instance.push_messages_by_phone(pnp_messages_request, x_line_delivery_tag=x_line_delivery_tag)
    except Exception as e:
        print("Exception when calling MessagingApiApi->push_messages_by_phone: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pnp_messages_request** | [**PnpMessagesRequest**](PnpMessagesRequest.md)|  | 
 **x_line_delivery_tag** | **str**| String returned in the delivery.data property of the delivery completion event via Webhook. | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reply_message**
> reply_message(reply_message_request)



Send reply message

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.reply_message_request import ReplyMessageRequest
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    reply_message_request = linebot.messaging.ReplyMessageRequest() # ReplyMessageRequest | 

    try:
        api_instance.reply_message(reply_message_request)
    except Exception as e:
        print("Exception when calling MessagingApiApi->reply_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reply_message_request** | [**ReplyMessageRequest**](ReplyMessageRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_default_rich_menu**
> set_default_rich_menu(rich_menu_id)



Set default rich menu

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    rich_menu_id = 'rich_menu_id_example' # str | ID of a rich menu

    try:
        api_instance.set_default_rich_menu(rich_menu_id)
    except Exception as e:
        print("Exception when calling MessagingApiApi->set_default_rich_menu: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rich_menu_id** | **str**| ID of a rich menu | 

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

# **set_webhook_endpoint**
> set_webhook_endpoint(set_webhook_endpoint_request)



Set webhook endpoint URL

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.set_webhook_endpoint_request import SetWebhookEndpointRequest
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    set_webhook_endpoint_request = linebot.messaging.SetWebhookEndpointRequest() # SetWebhookEndpointRequest | 

    try:
        api_instance.set_webhook_endpoint(set_webhook_endpoint_request)
    except Exception as e:
        print("Exception when calling MessagingApiApi->set_webhook_endpoint: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_webhook_endpoint_request** | [**SetWebhookEndpointRequest**](SetWebhookEndpointRequest.md)|  | 

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

# **test_webhook_endpoint**
> TestWebhookEndpointResponse test_webhook_endpoint(test_webhook_endpoint_request=test_webhook_endpoint_request)



Test webhook endpoint

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.test_webhook_endpoint_request import TestWebhookEndpointRequest
from linebot.messaging.models.test_webhook_endpoint_response import TestWebhookEndpointResponse
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    test_webhook_endpoint_request = linebot.messaging.TestWebhookEndpointRequest() # TestWebhookEndpointRequest |  (optional)

    try:
        api_response = api_instance.test_webhook_endpoint(test_webhook_endpoint_request=test_webhook_endpoint_request)
        print("The response of MessagingApiApi->test_webhook_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApiApi->test_webhook_endpoint: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_webhook_endpoint_request** | [**TestWebhookEndpointRequest**](TestWebhookEndpointRequest.md)|  | [optional] 

### Return type

[**TestWebhookEndpointResponse**](TestWebhookEndpointResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_rich_menu_id_from_user**
> unlink_rich_menu_id_from_user(user_id)



Unlink rich menu from user

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    user_id = 'user_id_example' # str | User ID. Found in the `source` object of webhook event objects. Do not use the LINE ID used in LINE.

    try:
        api_instance.unlink_rich_menu_id_from_user(user_id)
    except Exception as e:
        print("Exception when calling MessagingApiApi->unlink_rich_menu_id_from_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID. Found in the &#x60;source&#x60; object of webhook event objects. Do not use the LINE ID used in LINE. | 

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

# **unlink_rich_menu_id_from_users**
> unlink_rich_menu_id_from_users(rich_menu_bulk_unlink_request)



Unlink rich menus from multiple users

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.rich_menu_bulk_unlink_request import RichMenuBulkUnlinkRequest
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    rich_menu_bulk_unlink_request = linebot.messaging.RichMenuBulkUnlinkRequest() # RichMenuBulkUnlinkRequest | 

    try:
        api_instance.unlink_rich_menu_id_from_users(rich_menu_bulk_unlink_request)
    except Exception as e:
        print("Exception when calling MessagingApiApi->unlink_rich_menu_id_from_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rich_menu_bulk_unlink_request** | [**RichMenuBulkUnlinkRequest**](RichMenuBulkUnlinkRequest.md)|  | 

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
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rich_menu_alias**
> update_rich_menu_alias(rich_menu_alias_id, update_rich_menu_alias_request)



Update rich menu alias

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.update_rich_menu_alias_request import UpdateRichMenuAliasRequest
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    rich_menu_alias_id = 'rich_menu_alias_id_example' # str | The rich menu alias ID you want to update.
    update_rich_menu_alias_request = linebot.messaging.UpdateRichMenuAliasRequest() # UpdateRichMenuAliasRequest | 

    try:
        api_instance.update_rich_menu_alias(rich_menu_alias_id, update_rich_menu_alias_request)
    except Exception as e:
        print("Exception when calling MessagingApiApi->update_rich_menu_alias: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rich_menu_alias_id** | **str**| The rich menu alias ID you want to update. | 
 **update_rich_menu_alias_request** | [**UpdateRichMenuAliasRequest**](UpdateRichMenuAliasRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_broadcast**
> validate_broadcast(validate_message_request)



Validate message objects of a broadcast message

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.validate_message_request import ValidateMessageRequest
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    validate_message_request = linebot.messaging.ValidateMessageRequest() # ValidateMessageRequest | 

    try:
        api_instance.validate_broadcast(validate_message_request)
    except Exception as e:
        print("Exception when calling MessagingApiApi->validate_broadcast: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_message_request** | [**ValidateMessageRequest**](ValidateMessageRequest.md)|  | 

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

# **validate_multicast**
> validate_multicast(validate_message_request)



Validate message objects of a multicast message

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.validate_message_request import ValidateMessageRequest
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    validate_message_request = linebot.messaging.ValidateMessageRequest() # ValidateMessageRequest | 

    try:
        api_instance.validate_multicast(validate_message_request)
    except Exception as e:
        print("Exception when calling MessagingApiApi->validate_multicast: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_message_request** | [**ValidateMessageRequest**](ValidateMessageRequest.md)|  | 

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

# **validate_narrowcast**
> validate_narrowcast(validate_message_request)



Validate message objects of a narrowcast message

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.validate_message_request import ValidateMessageRequest
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    validate_message_request = linebot.messaging.ValidateMessageRequest() # ValidateMessageRequest | 

    try:
        api_instance.validate_narrowcast(validate_message_request)
    except Exception as e:
        print("Exception when calling MessagingApiApi->validate_narrowcast: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_message_request** | [**ValidateMessageRequest**](ValidateMessageRequest.md)|  | 

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

# **validate_push**
> validate_push(validate_message_request)



Validate message objects of a push message

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.validate_message_request import ValidateMessageRequest
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    validate_message_request = linebot.messaging.ValidateMessageRequest() # ValidateMessageRequest | 

    try:
        api_instance.validate_push(validate_message_request)
    except Exception as e:
        print("Exception when calling MessagingApiApi->validate_push: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_message_request** | [**ValidateMessageRequest**](ValidateMessageRequest.md)|  | 

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

# **validate_reply**
> validate_reply(validate_message_request)



Validate message objects of a reply message

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.validate_message_request import ValidateMessageRequest
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    validate_message_request = linebot.messaging.ValidateMessageRequest() # ValidateMessageRequest | 

    try:
        api_instance.validate_reply(validate_message_request)
    except Exception as e:
        print("Exception when calling MessagingApiApi->validate_reply: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_message_request** | [**ValidateMessageRequest**](ValidateMessageRequest.md)|  | 

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

# **validate_rich_menu_object**
> validate_rich_menu_object(rich_menu_request)



Validate rich menu object

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.messaging
from linebot.messaging.models.rich_menu_request import RichMenuRequest
from linebot.messaging.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.messaging.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.messaging.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.messaging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.messaging.MessagingApiApi(api_client)
    rich_menu_request = linebot.messaging.RichMenuRequest() # RichMenuRequest | 

    try:
        api_instance.validate_rich_menu_object(rich_menu_request)
    except Exception as e:
        print("Exception when calling MessagingApiApi->validate_rich_menu_object: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rich_menu_request** | [**RichMenuRequest**](RichMenuRequest.md)|  | 

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
