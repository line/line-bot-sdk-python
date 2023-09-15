# linebot.v3.messaging.MessagingApi

All URIs are relative to *https://api.line.me*

Method | HTTP request | Description
------------- | ------------- | -------------
[**audience_match**](MessagingApi.md#audience_match) | **POST** /bot/ad/multicast/phone | 
[**broadcast**](MessagingApi.md#broadcast) | **POST** /v2/bot/message/broadcast | 
[**cancel_default_rich_menu**](MessagingApi.md#cancel_default_rich_menu) | **DELETE** /v2/bot/user/all/richmenu | 
[**create_rich_menu**](MessagingApi.md#create_rich_menu) | **POST** /v2/bot/richmenu | 
[**create_rich_menu_alias**](MessagingApi.md#create_rich_menu_alias) | **POST** /v2/bot/richmenu/alias | 
[**delete_rich_menu**](MessagingApi.md#delete_rich_menu) | **DELETE** /v2/bot/richmenu/{richMenuId} | 
[**delete_rich_menu_alias**](MessagingApi.md#delete_rich_menu_alias) | **DELETE** /v2/bot/richmenu/alias/{richMenuAliasId} | 
[**get_ad_phone_message_statistics**](MessagingApi.md#get_ad_phone_message_statistics) | **GET** /v2/bot/message/delivery/ad_phone | 
[**get_aggregation_unit_name_list**](MessagingApi.md#get_aggregation_unit_name_list) | **GET** /v2/bot/message/aggregation/list | 
[**get_aggregation_unit_usage**](MessagingApi.md#get_aggregation_unit_usage) | **GET** /v2/bot/message/aggregation/info | 
[**get_bot_info**](MessagingApi.md#get_bot_info) | **GET** /v2/bot/info | 
[**get_default_rich_menu_id**](MessagingApi.md#get_default_rich_menu_id) | **GET** /v2/bot/user/all/richmenu | 
[**get_followers**](MessagingApi.md#get_followers) | **GET** /v2/bot/followers/ids | 
[**get_group_member_count**](MessagingApi.md#get_group_member_count) | **GET** /v2/bot/group/{groupId}/members/count | 
[**get_group_member_profile**](MessagingApi.md#get_group_member_profile) | **GET** /v2/bot/group/{groupId}/member/{userId} | 
[**get_group_members_ids**](MessagingApi.md#get_group_members_ids) | **GET** /v2/bot/group/{groupId}/members/ids | 
[**get_group_summary**](MessagingApi.md#get_group_summary) | **GET** /v2/bot/group/{groupId}/summary | 
[**get_message_quota**](MessagingApi.md#get_message_quota) | **GET** /v2/bot/message/quota | 
[**get_message_quota_consumption**](MessagingApi.md#get_message_quota_consumption) | **GET** /v2/bot/message/quota/consumption | 
[**get_narrowcast_progress**](MessagingApi.md#get_narrowcast_progress) | **GET** /v2/bot/message/progress/narrowcast | 
[**get_number_of_sent_broadcast_messages**](MessagingApi.md#get_number_of_sent_broadcast_messages) | **GET** /v2/bot/message/delivery/broadcast | 
[**get_number_of_sent_multicast_messages**](MessagingApi.md#get_number_of_sent_multicast_messages) | **GET** /v2/bot/message/delivery/multicast | 
[**get_number_of_sent_push_messages**](MessagingApi.md#get_number_of_sent_push_messages) | **GET** /v2/bot/message/delivery/push | 
[**get_number_of_sent_reply_messages**](MessagingApi.md#get_number_of_sent_reply_messages) | **GET** /v2/bot/message/delivery/reply | 
[**get_pnp_message_statistics**](MessagingApi.md#get_pnp_message_statistics) | **GET** /v2/bot/message/delivery/pnp | 
[**get_profile**](MessagingApi.md#get_profile) | **GET** /v2/bot/profile/{userId} | 
[**get_rich_menu**](MessagingApi.md#get_rich_menu) | **GET** /v2/bot/richmenu/{richMenuId} | 
[**get_rich_menu_alias**](MessagingApi.md#get_rich_menu_alias) | **GET** /v2/bot/richmenu/alias/{richMenuAliasId} | 
[**get_rich_menu_alias_list**](MessagingApi.md#get_rich_menu_alias_list) | **GET** /v2/bot/richmenu/alias/list | 
[**get_rich_menu_batch_progress**](MessagingApi.md#get_rich_menu_batch_progress) | **GET** /v2/bot/richmenu/progress/batch | 
[**get_rich_menu_id_of_user**](MessagingApi.md#get_rich_menu_id_of_user) | **GET** /v2/bot/user/{userId}/richmenu | 
[**get_rich_menu_list**](MessagingApi.md#get_rich_menu_list) | **GET** /v2/bot/richmenu/list | 
[**get_room_member_count**](MessagingApi.md#get_room_member_count) | **GET** /v2/bot/room/{roomId}/members/count | 
[**get_room_member_profile**](MessagingApi.md#get_room_member_profile) | **GET** /v2/bot/room/{roomId}/member/{userId} | 
[**get_room_members_ids**](MessagingApi.md#get_room_members_ids) | **GET** /v2/bot/room/{roomId}/members/ids | 
[**get_webhook_endpoint**](MessagingApi.md#get_webhook_endpoint) | **GET** /v2/bot/channel/webhook/endpoint | 
[**issue_link_token**](MessagingApi.md#issue_link_token) | **POST** /v2/bot/user/{userId}/linkToken | 
[**leave_group**](MessagingApi.md#leave_group) | **POST** /v2/bot/group/{groupId}/leave | 
[**leave_room**](MessagingApi.md#leave_room) | **POST** /v2/bot/room/{roomId}/leave | 
[**link_rich_menu_id_to_user**](MessagingApi.md#link_rich_menu_id_to_user) | **POST** /v2/bot/user/{userId}/richmenu/{richMenuId} | 
[**link_rich_menu_id_to_users**](MessagingApi.md#link_rich_menu_id_to_users) | **POST** /v2/bot/richmenu/bulk/link | 
[**mark_messages_as_read**](MessagingApi.md#mark_messages_as_read) | **POST** /v2/bot/message/markAsRead | 
[**multicast**](MessagingApi.md#multicast) | **POST** /v2/bot/message/multicast | 
[**narrowcast**](MessagingApi.md#narrowcast) | **POST** /v2/bot/message/narrowcast | 
[**push_message**](MessagingApi.md#push_message) | **POST** /v2/bot/message/push | 
[**push_messages_by_phone**](MessagingApi.md#push_messages_by_phone) | **POST** /bot/pnp/push | 
[**reply_message**](MessagingApi.md#reply_message) | **POST** /v2/bot/message/reply | 
[**rich_menu_batch**](MessagingApi.md#rich_menu_batch) | **POST** /v2/bot/richmenu/batch | 
[**set_default_rich_menu**](MessagingApi.md#set_default_rich_menu) | **POST** /v2/bot/user/all/richmenu/{richMenuId} | 
[**set_webhook_endpoint**](MessagingApi.md#set_webhook_endpoint) | **PUT** /v2/bot/channel/webhook/endpoint | 
[**test_webhook_endpoint**](MessagingApi.md#test_webhook_endpoint) | **POST** /v2/bot/channel/webhook/test | 
[**unlink_rich_menu_id_from_user**](MessagingApi.md#unlink_rich_menu_id_from_user) | **DELETE** /v2/bot/user/{userId}/richmenu | 
[**unlink_rich_menu_id_from_users**](MessagingApi.md#unlink_rich_menu_id_from_users) | **POST** /v2/bot/richmenu/bulk/unlink | 
[**update_rich_menu_alias**](MessagingApi.md#update_rich_menu_alias) | **POST** /v2/bot/richmenu/alias/{richMenuAliasId} | 
[**validate_broadcast**](MessagingApi.md#validate_broadcast) | **POST** /v2/bot/message/validate/broadcast | 
[**validate_multicast**](MessagingApi.md#validate_multicast) | **POST** /v2/bot/message/validate/multicast | 
[**validate_narrowcast**](MessagingApi.md#validate_narrowcast) | **POST** /v2/bot/message/validate/narrowcast | 
[**validate_push**](MessagingApi.md#validate_push) | **POST** /v2/bot/message/validate/push | 
[**validate_reply**](MessagingApi.md#validate_reply) | **POST** /v2/bot/message/validate/reply | 
[**validate_rich_menu_batch_request**](MessagingApi.md#validate_rich_menu_batch_request) | **POST** /v2/bot/richmenu/validate/batch | 
[**validate_rich_menu_object**](MessagingApi.md#validate_rich_menu_object) | **POST** /v2/bot/richmenu/validate | 


# **audience_match**
> audience_match(audience_match_messages_request)



Send a message using phone number

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.messaging
from linebot.v3.messaging.models.audience_match_messages_request import AudienceMatchMessagesRequest
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    audience_match_messages_request = linebot.v3.messaging.AudienceMatchMessagesRequest() # AudienceMatchMessagesRequest | 

    try:
        api_instance.audience_match(audience_match_messages_request)
    except Exception as e:
        print("Exception when calling MessagingApi->audience_match: %s\n" % e)
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
> object broadcast(broadcast_request, x_line_retry_key=x_line_retry_key)



Sends a message to multiple users at any time.

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.messaging
from linebot.v3.messaging.models.broadcast_request import BroadcastRequest
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    broadcast_request = linebot.v3.messaging.BroadcastRequest() # BroadcastRequest | 
    x_line_retry_key = 'x_line_retry_key_example' # str | Retry key. Specifies the UUID in hexadecimal format (e.g., `123e4567-e89b-12d3-a456-426614174000`) generated by any method. The retry key isn't generated by LINE. Each developer must generate their own retry key.  (optional)

    try:
        api_response = api_instance.broadcast(broadcast_request, x_line_retry_key=x_line_retry_key)
        print("The response of MessagingApi->broadcast:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->broadcast: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broadcast_request** | [**BroadcastRequest**](BroadcastRequest.md)|  | 
 **x_line_retry_key** | **str**| Retry key. Specifies the UUID in hexadecimal format (e.g., &#x60;123e4567-e89b-12d3-a456-426614174000&#x60;) generated by any method. The retry key isn&#39;t generated by LINE. Each developer must generate their own retry key.  | [optional] 

### Return type

**object**

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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)

    try:
        api_instance.cancel_default_rich_menu()
    except Exception as e:
        print("Exception when calling MessagingApi->cancel_default_rich_menu: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.rich_menu_id_response import RichMenuIdResponse
from linebot.v3.messaging.models.rich_menu_request import RichMenuRequest
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    rich_menu_request = linebot.v3.messaging.RichMenuRequest() # RichMenuRequest | 

    try:
        api_response = api_instance.create_rich_menu(rich_menu_request)
        print("The response of MessagingApi->create_rich_menu:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->create_rich_menu: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.create_rich_menu_alias_request import CreateRichMenuAliasRequest
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    create_rich_menu_alias_request = linebot.v3.messaging.CreateRichMenuAliasRequest() # CreateRichMenuAliasRequest | 

    try:
        api_instance.create_rich_menu_alias(create_rich_menu_alias_request)
    except Exception as e:
        print("Exception when calling MessagingApi->create_rich_menu_alias: %s\n" % e)
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    rich_menu_id = 'rich_menu_id_example' # str | ID of a rich menu

    try:
        api_instance.delete_rich_menu(rich_menu_id)
    except Exception as e:
        print("Exception when calling MessagingApi->delete_rich_menu: %s\n" % e)
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    rich_menu_alias_id = 'rich_menu_alias_id_example' # str | Rich menu alias ID that you want to delete.

    try:
        api_instance.delete_rich_menu_alias(rich_menu_alias_id)
    except Exception as e:
        print("Exception when calling MessagingApi->delete_rich_menu_alias: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.number_of_messages_response import NumberOfMessagesResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    var_date = 'var_date_example' # str | Date the message was sent  Format: `yyyyMMdd` (e.g. `20190831`) Time Zone: UTC+9 

    try:
        api_response = api_instance.get_ad_phone_message_statistics(var_date)
        print("The response of MessagingApi->get_ad_phone_message_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->get_ad_phone_message_statistics: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.get_aggregation_unit_name_list_response import GetAggregationUnitNameListResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    limit = 'limit_example' # str | The maximum number of aggregation units you can get per request.  (optional)
    start = 'start_example' # str | Value of the continuation token found in the next property of the JSON object returned in the response. If you can't get all the aggregation units in one request, include this parameter to get the remaining array.  (optional)

    try:
        api_response = api_instance.get_aggregation_unit_name_list(limit=limit, start=start)
        print("The response of MessagingApi->get_aggregation_unit_name_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->get_aggregation_unit_name_list: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.get_aggregation_unit_usage_response import GetAggregationUnitUsageResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)

    try:
        api_response = api_instance.get_aggregation_unit_usage()
        print("The response of MessagingApi->get_aggregation_unit_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->get_aggregation_unit_usage: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.bot_info_response import BotInfoResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)

    try:
        api_response = api_instance.get_bot_info()
        print("The response of MessagingApi->get_bot_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->get_bot_info: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.rich_menu_id_response import RichMenuIdResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)

    try:
        api_response = api_instance.get_default_rich_menu_id()
        print("The response of MessagingApi->get_default_rich_menu_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->get_default_rich_menu_id: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.get_followers_response import GetFollowersResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    start = 'start_example' # str | Value of the continuation token found in the next property of the JSON object returned in the response. Include this parameter to get the next array of user IDs.  (optional)
    limit = 300 # int | The maximum number of user IDs to retrieve in a single request. (optional) (default to 300)

    try:
        api_response = api_instance.get_followers(start=start, limit=limit)
        print("The response of MessagingApi->get_followers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->get_followers: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.group_member_count_response import GroupMemberCountResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    group_id = 'group_id_example' # str | Group ID

    try:
        api_response = api_instance.get_group_member_count(group_id)
        print("The response of MessagingApi->get_group_member_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->get_group_member_count: %s\n" % e)
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
> GroupUserProfileResponse get_group_member_profile(group_id, user_id)



Get group chat member profile

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.messaging
from linebot.v3.messaging.models.group_user_profile_response import GroupUserProfileResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    group_id = 'group_id_example' # str | Group ID
    user_id = 'user_id_example' # str | User ID

    try:
        api_response = api_instance.get_group_member_profile(group_id, user_id)
        print("The response of MessagingApi->get_group_member_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->get_group_member_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Group ID | 
 **user_id** | **str**| User ID | 

### Return type

[**GroupUserProfileResponse**](GroupUserProfileResponse.md)

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
import linebot.v3.messaging
from linebot.v3.messaging.models.members_ids_response import MembersIdsResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    group_id = 'group_id_example' # str | Group ID
    start = 'start_example' # str | Value of the continuation token found in the `next` property of the JSON object returned in the response. Include this parameter to get the next array of user IDs for the members of the group.  (optional)

    try:
        api_response = api_instance.get_group_members_ids(group_id, start=start)
        print("The response of MessagingApi->get_group_members_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->get_group_members_ids: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.group_summary_response import GroupSummaryResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    group_id = 'group_id_example' # str | Group ID

    try:
        api_response = api_instance.get_group_summary(group_id)
        print("The response of MessagingApi->get_group_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->get_group_summary: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.message_quota_response import MessageQuotaResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)

    try:
        api_response = api_instance.get_message_quota()
        print("The response of MessagingApi->get_message_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->get_message_quota: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.quota_consumption_response import QuotaConsumptionResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)

    try:
        api_response = api_instance.get_message_quota_consumption()
        print("The response of MessagingApi->get_message_quota_consumption:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->get_message_quota_consumption: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.narrowcast_progress_response import NarrowcastProgressResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    request_id = 'request_id_example' # str | The narrowcast message's request ID. Each Messaging API request has a request ID.

    try:
        api_response = api_instance.get_narrowcast_progress(request_id)
        print("The response of MessagingApi->get_narrowcast_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->get_narrowcast_progress: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.number_of_messages_response import NumberOfMessagesResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    var_date = 'var_date_example' # str | Date the messages were sent  Format: yyyyMMdd (e.g. 20191231) Timezone: UTC+9 

    try:
        api_response = api_instance.get_number_of_sent_broadcast_messages(var_date)
        print("The response of MessagingApi->get_number_of_sent_broadcast_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->get_number_of_sent_broadcast_messages: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.number_of_messages_response import NumberOfMessagesResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    var_date = 'var_date_example' # str | Date the messages were sent  Format: `yyyyMMdd` (e.g. `20191231`) Timezone: UTC+9 

    try:
        api_response = api_instance.get_number_of_sent_multicast_messages(var_date)
        print("The response of MessagingApi->get_number_of_sent_multicast_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->get_number_of_sent_multicast_messages: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.number_of_messages_response import NumberOfMessagesResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    var_date = 'var_date_example' # str | Date the messages were sent  Format: `yyyyMMdd` (e.g. `20191231`) Timezone: UTC+9 

    try:
        api_response = api_instance.get_number_of_sent_push_messages(var_date)
        print("The response of MessagingApi->get_number_of_sent_push_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->get_number_of_sent_push_messages: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.number_of_messages_response import NumberOfMessagesResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    var_date = 'var_date_example' # str | Date the messages were sent  Format: `yyyyMMdd` (e.g. `20191231`) Timezone: UTC+9 

    try:
        api_response = api_instance.get_number_of_sent_reply_messages(var_date)
        print("The response of MessagingApi->get_number_of_sent_reply_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->get_number_of_sent_reply_messages: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.number_of_messages_response import NumberOfMessagesResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    var_date = 'var_date_example' # str | Date the message was sent  Format: `yyyyMMdd` (Example:`20211231`) Time zone: UTC+9 

    try:
        api_response = api_instance.get_pnp_message_statistics(var_date)
        print("The response of MessagingApi->get_pnp_message_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->get_pnp_message_statistics: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.user_profile_response import UserProfileResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    user_id = 'user_id_example' # str | User ID

    try:
        api_response = api_instance.get_profile(user_id)
        print("The response of MessagingApi->get_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->get_profile: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.rich_menu_response import RichMenuResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    rich_menu_id = 'rich_menu_id_example' # str | ID of a rich menu

    try:
        api_response = api_instance.get_rich_menu(rich_menu_id)
        print("The response of MessagingApi->get_rich_menu:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->get_rich_menu: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.rich_menu_alias_response import RichMenuAliasResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    rich_menu_alias_id = 'rich_menu_alias_id_example' # str | The rich menu alias ID whose information you want to obtain.

    try:
        api_response = api_instance.get_rich_menu_alias(rich_menu_alias_id)
        print("The response of MessagingApi->get_rich_menu_alias:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->get_rich_menu_alias: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.rich_menu_alias_list_response import RichMenuAliasListResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)

    try:
        api_response = api_instance.get_rich_menu_alias_list()
        print("The response of MessagingApi->get_rich_menu_alias_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->get_rich_menu_alias_list: %s\n" % e)
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

# **get_rich_menu_batch_progress**
> RichMenuBatchProgressResponse get_rich_menu_batch_progress(request_id)



Get the status of Replace or unlink a linked rich menus in batches.

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.messaging
from linebot.v3.messaging.models.rich_menu_batch_progress_response import RichMenuBatchProgressResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    request_id = 'request_id_example' # str | A request ID used to batch control the rich menu linked to the user. Each Messaging API request has a request ID.

    try:
        api_response = api_instance.get_rich_menu_batch_progress(request_id)
        print("The response of MessagingApi->get_rich_menu_batch_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->get_rich_menu_batch_progress: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| A request ID used to batch control the rich menu linked to the user. Each Messaging API request has a request ID. | 

### Return type

[**RichMenuBatchProgressResponse**](RichMenuBatchProgressResponse.md)

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
import linebot.v3.messaging
from linebot.v3.messaging.models.rich_menu_id_response import RichMenuIdResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    user_id = 'user_id_example' # str | User ID. Found in the `source` object of webhook event objects. Do not use the LINE ID used in LINE.

    try:
        api_response = api_instance.get_rich_menu_id_of_user(user_id)
        print("The response of MessagingApi->get_rich_menu_id_of_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->get_rich_menu_id_of_user: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.rich_menu_list_response import RichMenuListResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)

    try:
        api_response = api_instance.get_rich_menu_list()
        print("The response of MessagingApi->get_rich_menu_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->get_rich_menu_list: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.room_member_count_response import RoomMemberCountResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    room_id = 'room_id_example' # str | Room ID

    try:
        api_response = api_instance.get_room_member_count(room_id)
        print("The response of MessagingApi->get_room_member_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->get_room_member_count: %s\n" % e)
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
> RoomUserProfileResponse get_room_member_profile(room_id, user_id)



Get multi-person chat member profile

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.messaging
from linebot.v3.messaging.models.room_user_profile_response import RoomUserProfileResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    room_id = 'room_id_example' # str | Room ID
    user_id = 'user_id_example' # str | User ID

    try:
        api_response = api_instance.get_room_member_profile(room_id, user_id)
        print("The response of MessagingApi->get_room_member_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->get_room_member_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **str**| Room ID | 
 **user_id** | **str**| User ID | 

### Return type

[**RoomUserProfileResponse**](RoomUserProfileResponse.md)

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
import linebot.v3.messaging
from linebot.v3.messaging.models.members_ids_response import MembersIdsResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    room_id = 'room_id_example' # str | Room ID
    start = 'start_example' # str | Value of the continuation token found in the `next` property of the JSON object returned in the response. Include this parameter to get the next array of user IDs for the members of the group.  (optional)

    try:
        api_response = api_instance.get_room_members_ids(room_id, start=start)
        print("The response of MessagingApi->get_room_members_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->get_room_members_ids: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.get_webhook_endpoint_response import GetWebhookEndpointResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)

    try:
        api_response = api_instance.get_webhook_endpoint()
        print("The response of MessagingApi->get_webhook_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->get_webhook_endpoint: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.issue_link_token_response import IssueLinkTokenResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    user_id = 'user_id_example' # str | User ID for the LINE account to be linked. Found in the `source` object of account link event objects. Do not use the LINE ID used in LINE. 

    try:
        api_response = api_instance.issue_link_token(user_id)
        print("The response of MessagingApi->issue_link_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->issue_link_token: %s\n" % e)
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    group_id = 'group_id_example' # str | Group ID

    try:
        api_instance.leave_group(group_id)
    except Exception as e:
        print("Exception when calling MessagingApi->leave_group: %s\n" % e)
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    room_id = 'room_id_example' # str | Room ID

    try:
        api_instance.leave_room(room_id)
    except Exception as e:
        print("Exception when calling MessagingApi->leave_room: %s\n" % e)
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    user_id = 'user_id_example' # str | User ID. Found in the `source` object of webhook event objects. Do not use the LINE ID used in LINE.
    rich_menu_id = 'rich_menu_id_example' # str | ID of a rich menu

    try:
        api_instance.link_rich_menu_id_to_user(user_id, rich_menu_id)
    except Exception as e:
        print("Exception when calling MessagingApi->link_rich_menu_id_to_user: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.rich_menu_bulk_link_request import RichMenuBulkLinkRequest
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    rich_menu_bulk_link_request = linebot.v3.messaging.RichMenuBulkLinkRequest() # RichMenuBulkLinkRequest | 

    try:
        api_instance.link_rich_menu_id_to_users(rich_menu_bulk_link_request)
    except Exception as e:
        print("Exception when calling MessagingApi->link_rich_menu_id_to_users: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.mark_messages_as_read_request import MarkMessagesAsReadRequest
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    mark_messages_as_read_request = {"chat":{"userId":"Uxxxxxxxxxxxxxxxxxx"}} # MarkMessagesAsReadRequest | 

    try:
        api_instance.mark_messages_as_read(mark_messages_as_read_request)
    except Exception as e:
        print("Exception when calling MessagingApi->mark_messages_as_read: %s\n" % e)
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
> object multicast(multicast_request, x_line_retry_key=x_line_retry_key)



An API that efficiently sends the same message to multiple user IDs. You can't send messages to group chats or multi-person chats.

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.messaging
from linebot.v3.messaging.models.multicast_request import MulticastRequest
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    multicast_request = linebot.v3.messaging.MulticastRequest() # MulticastRequest | 
    x_line_retry_key = 'x_line_retry_key_example' # str | Retry key. Specifies the UUID in hexadecimal format (e.g., `123e4567-e89b-12d3-a456-426614174000`) generated by any method. The retry key isn't generated by LINE. Each developer must generate their own retry key.  (optional)

    try:
        api_response = api_instance.multicast(multicast_request, x_line_retry_key=x_line_retry_key)
        print("The response of MessagingApi->multicast:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->multicast: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multicast_request** | [**MulticastRequest**](MulticastRequest.md)|  | 
 **x_line_retry_key** | **str**| Retry key. Specifies the UUID in hexadecimal format (e.g., &#x60;123e4567-e89b-12d3-a456-426614174000&#x60;) generated by any method. The retry key isn&#39;t generated by LINE. Each developer must generate their own retry key.  | [optional] 

### Return type

**object**

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
> object narrowcast(narrowcast_request, x_line_retry_key=x_line_retry_key)



Send narrowcast message

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.messaging
from linebot.v3.messaging.models.narrowcast_request import NarrowcastRequest
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    narrowcast_request = linebot.v3.messaging.NarrowcastRequest() # NarrowcastRequest | 
    x_line_retry_key = 'x_line_retry_key_example' # str | Retry key. Specifies the UUID in hexadecimal format (e.g., `123e4567-e89b-12d3-a456-426614174000`) generated by any method. The retry key isn't generated by LINE. Each developer must generate their own retry key.  (optional)

    try:
        api_response = api_instance.narrowcast(narrowcast_request, x_line_retry_key=x_line_retry_key)
        print("The response of MessagingApi->narrowcast:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->narrowcast: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **narrowcast_request** | [**NarrowcastRequest**](NarrowcastRequest.md)|  | 
 **x_line_retry_key** | **str**| Retry key. Specifies the UUID in hexadecimal format (e.g., &#x60;123e4567-e89b-12d3-a456-426614174000&#x60;) generated by any method. The retry key isn&#39;t generated by LINE. Each developer must generate their own retry key.  | [optional] 

### Return type

**object**

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
> PushMessageResponse push_message(push_message_request, x_line_retry_key=x_line_retry_key)



Sends a message to a user, group chat, or multi-person chat at any time.

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.messaging
from linebot.v3.messaging.models.push_message_request import PushMessageRequest
from linebot.v3.messaging.models.push_message_response import PushMessageResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    push_message_request = linebot.v3.messaging.PushMessageRequest() # PushMessageRequest | 
    x_line_retry_key = 'x_line_retry_key_example' # str | Retry key. Specifies the UUID in hexadecimal format (e.g., `123e4567-e89b-12d3-a456-426614174000`) generated by any method. The retry key isn't generated by LINE. Each developer must generate their own retry key.  (optional)

    try:
        api_response = api_instance.push_message(push_message_request, x_line_retry_key=x_line_retry_key)
        print("The response of MessagingApi->push_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->push_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **push_message_request** | [**PushMessageRequest**](PushMessageRequest.md)|  | 
 **x_line_retry_key** | **str**| Retry key. Specifies the UUID in hexadecimal format (e.g., &#x60;123e4567-e89b-12d3-a456-426614174000&#x60;) generated by any method. The retry key isn&#39;t generated by LINE. Each developer must generate their own retry key.  | [optional] 

### Return type

[**PushMessageResponse**](PushMessageResponse.md)

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
import linebot.v3.messaging
from linebot.v3.messaging.models.pnp_messages_request import PnpMessagesRequest
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    pnp_messages_request = linebot.v3.messaging.PnpMessagesRequest() # PnpMessagesRequest | 
    x_line_delivery_tag = 'x_line_delivery_tag_example' # str | String returned in the delivery.data property of the delivery completion event via Webhook. (optional)

    try:
        api_instance.push_messages_by_phone(pnp_messages_request, x_line_delivery_tag=x_line_delivery_tag)
    except Exception as e:
        print("Exception when calling MessagingApi->push_messages_by_phone: %s\n" % e)
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
> ReplyMessageResponse reply_message(reply_message_request)



Send reply message

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.messaging
from linebot.v3.messaging.models.reply_message_request import ReplyMessageRequest
from linebot.v3.messaging.models.reply_message_response import ReplyMessageResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    reply_message_request = linebot.v3.messaging.ReplyMessageRequest() # ReplyMessageRequest | 

    try:
        api_response = api_instance.reply_message(reply_message_request)
        print("The response of MessagingApi->reply_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->reply_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reply_message_request** | [**ReplyMessageRequest**](ReplyMessageRequest.md)|  | 

### Return type

[**ReplyMessageResponse**](ReplyMessageResponse.md)

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

# **rich_menu_batch**
> rich_menu_batch(rich_menu_batch_request)



You can use this endpoint to batch control the rich menu linked to the users using the endpoint such as Link rich menu to user.  The following operations are available:  1. Replace a rich menu with another rich menu for all users linked to a specific rich menu 2. Unlink a rich menu for all users linked to a specific rich menu 3. Unlink a rich menu for all users linked the rich menu 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.messaging
from linebot.v3.messaging.models.rich_menu_batch_request import RichMenuBatchRequest
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    rich_menu_batch_request = linebot.v3.messaging.RichMenuBatchRequest() # RichMenuBatchRequest | 

    try:
        api_instance.rich_menu_batch(rich_menu_batch_request)
    except Exception as e:
        print("Exception when calling MessagingApi->rich_menu_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rich_menu_batch_request** | [**RichMenuBatchRequest**](RichMenuBatchRequest.md)|  | 

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

# **set_default_rich_menu**
> set_default_rich_menu(rich_menu_id)



Set default rich menu

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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    rich_menu_id = 'rich_menu_id_example' # str | ID of a rich menu

    try:
        api_instance.set_default_rich_menu(rich_menu_id)
    except Exception as e:
        print("Exception when calling MessagingApi->set_default_rich_menu: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.set_webhook_endpoint_request import SetWebhookEndpointRequest
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    set_webhook_endpoint_request = linebot.v3.messaging.SetWebhookEndpointRequest() # SetWebhookEndpointRequest | 

    try:
        api_instance.set_webhook_endpoint(set_webhook_endpoint_request)
    except Exception as e:
        print("Exception when calling MessagingApi->set_webhook_endpoint: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.test_webhook_endpoint_request import TestWebhookEndpointRequest
from linebot.v3.messaging.models.test_webhook_endpoint_response import TestWebhookEndpointResponse
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    test_webhook_endpoint_request = linebot.v3.messaging.TestWebhookEndpointRequest() # TestWebhookEndpointRequest |  (optional)

    try:
        api_response = api_instance.test_webhook_endpoint(test_webhook_endpoint_request=test_webhook_endpoint_request)
        print("The response of MessagingApi->test_webhook_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->test_webhook_endpoint: %s\n" % e)
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    user_id = 'user_id_example' # str | User ID. Found in the `source` object of webhook event objects. Do not use the LINE ID used in LINE.

    try:
        api_instance.unlink_rich_menu_id_from_user(user_id)
    except Exception as e:
        print("Exception when calling MessagingApi->unlink_rich_menu_id_from_user: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.rich_menu_bulk_unlink_request import RichMenuBulkUnlinkRequest
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    rich_menu_bulk_unlink_request = linebot.v3.messaging.RichMenuBulkUnlinkRequest() # RichMenuBulkUnlinkRequest | 

    try:
        api_instance.unlink_rich_menu_id_from_users(rich_menu_bulk_unlink_request)
    except Exception as e:
        print("Exception when calling MessagingApi->unlink_rich_menu_id_from_users: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.update_rich_menu_alias_request import UpdateRichMenuAliasRequest
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    rich_menu_alias_id = 'rich_menu_alias_id_example' # str | The rich menu alias ID you want to update.
    update_rich_menu_alias_request = linebot.v3.messaging.UpdateRichMenuAliasRequest() # UpdateRichMenuAliasRequest | 

    try:
        api_instance.update_rich_menu_alias(rich_menu_alias_id, update_rich_menu_alias_request)
    except Exception as e:
        print("Exception when calling MessagingApi->update_rich_menu_alias: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.validate_message_request import ValidateMessageRequest
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    validate_message_request = linebot.v3.messaging.ValidateMessageRequest() # ValidateMessageRequest | 

    try:
        api_instance.validate_broadcast(validate_message_request)
    except Exception as e:
        print("Exception when calling MessagingApi->validate_broadcast: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.validate_message_request import ValidateMessageRequest
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    validate_message_request = linebot.v3.messaging.ValidateMessageRequest() # ValidateMessageRequest | 

    try:
        api_instance.validate_multicast(validate_message_request)
    except Exception as e:
        print("Exception when calling MessagingApi->validate_multicast: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.validate_message_request import ValidateMessageRequest
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    validate_message_request = linebot.v3.messaging.ValidateMessageRequest() # ValidateMessageRequest | 

    try:
        api_instance.validate_narrowcast(validate_message_request)
    except Exception as e:
        print("Exception when calling MessagingApi->validate_narrowcast: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.validate_message_request import ValidateMessageRequest
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    validate_message_request = linebot.v3.messaging.ValidateMessageRequest() # ValidateMessageRequest | 

    try:
        api_instance.validate_push(validate_message_request)
    except Exception as e:
        print("Exception when calling MessagingApi->validate_push: %s\n" % e)
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
import linebot.v3.messaging
from linebot.v3.messaging.models.validate_message_request import ValidateMessageRequest
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    validate_message_request = linebot.v3.messaging.ValidateMessageRequest() # ValidateMessageRequest | 

    try:
        api_instance.validate_reply(validate_message_request)
    except Exception as e:
        print("Exception when calling MessagingApi->validate_reply: %s\n" % e)
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

# **validate_rich_menu_batch_request**
> validate_rich_menu_batch_request(rich_menu_batch_request)



Validate a request body of the Replace or unlink the linked rich menus in batches endpoint.

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.messaging
from linebot.v3.messaging.models.rich_menu_batch_request import RichMenuBatchRequest
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    rich_menu_batch_request = linebot.v3.messaging.RichMenuBatchRequest() # RichMenuBatchRequest | 

    try:
        api_instance.validate_rich_menu_batch_request(rich_menu_batch_request)
    except Exception as e:
        print("Exception when calling MessagingApi->validate_rich_menu_batch_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rich_menu_batch_request** | [**RichMenuBatchRequest**](RichMenuBatchRequest.md)|  | 

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
import linebot.v3.messaging
from linebot.v3.messaging.models.rich_menu_request import RichMenuRequest
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
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    rich_menu_request = linebot.v3.messaging.RichMenuRequest() # RichMenuRequest | 

    try:
        api_instance.validate_rich_menu_object(rich_menu_request)
    except Exception as e:
        print("Exception when calling MessagingApi->validate_rich_menu_object: %s\n" % e)
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

