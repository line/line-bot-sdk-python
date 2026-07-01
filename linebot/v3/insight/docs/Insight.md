# linebot.v3.insight.Insight

All URIs are relative to *https://api.line.me*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_friends_demographics**](Insight.md#get_friends_demographics) | **GET** /v2/bot/insight/demographic | 
[**get_message_event**](Insight.md#get_message_event) | **GET** /v2/bot/insight/message/event | Get user interaction statistics
[**get_number_of_followers**](Insight.md#get_number_of_followers) | **GET** /v2/bot/insight/followers | Get number of followers
[**get_number_of_message_deliveries**](Insight.md#get_number_of_message_deliveries) | **GET** /v2/bot/insight/message/delivery | Get number of message deliveries
[**get_rich_menu_insight_daily**](Insight.md#get_rich_menu_insight_daily) | **GET** /v2/bot/insight/richmenu/{richMenuId}/daily | Get rich menu insight daily
[**get_rich_menu_insight_summary**](Insight.md#get_rich_menu_insight_summary) | **GET** /v2/bot/insight/richmenu/{richMenuId}/summary | Get rich menu insight summary
[**get_statistics_per_unit**](Insight.md#get_statistics_per_unit) | **GET** /v2/bot/insight/message/event/aggregation | 


# **get_friends_demographics**
> GetFriendsDemographicsResponse get_friends_demographics()



Retrieves the demographic attributes for a LINE Official Account's friends.You can only retrieve information about friends for LINE Official Accounts created by users in Japan (JP), Thailand (TH), Taiwan (TW) and Indonesia (ID). 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.insight
from linebot.v3.insight.models.get_friends_demographics_response import GetFriendsDemographicsResponse
from linebot.v3.insight.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.insight.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.insight.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.insight.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.insight.Insight(api_client)

    try:
        api_response = api_instance.get_friends_demographics()
        print("The response of Insight->get_friends_demographics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Insight->get_friends_demographics: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetFriendsDemographicsResponse**](GetFriendsDemographicsResponse.md)

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

# **get_message_event**
> GetMessageEventResponse get_message_event(request_id)

Get user interaction statistics

Returns statistics about how users interact with narrowcast messages or broadcast messages sent from your LINE Official Account. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.insight
from linebot.v3.insight.models.get_message_event_response import GetMessageEventResponse
from linebot.v3.insight.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.insight.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.insight.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.insight.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.insight.Insight(api_client)
    request_id = 'request_id_example' # str | Request ID of a narrowcast message or broadcast message. Each Messaging API request has a request ID. 

    try:
        # Get user interaction statistics
        api_response = api_instance.get_message_event(request_id)
        print("The response of Insight->get_message_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Insight->get_message_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| Request ID of a narrowcast message or broadcast message. Each Messaging API request has a request ID.  | 

### Return type

[**GetMessageEventResponse**](GetMessageEventResponse.md)

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

# **get_number_of_followers**
> GetNumberOfFollowersResponse get_number_of_followers(var_date=var_date)

Get number of followers

Returns the number of users who have added the LINE Official Account on or before a specified date. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.insight
from linebot.v3.insight.models.get_number_of_followers_response import GetNumberOfFollowersResponse
from linebot.v3.insight.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.insight.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.insight.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.insight.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.insight.Insight(api_client)
    var_date = 'var_date_example' # str | Date for which to retrieve the number of followers.  Format: yyyyMMdd (e.g. 20191231) Timezone: UTC+9  (optional)

    try:
        # Get number of followers
        api_response = api_instance.get_number_of_followers(var_date=var_date)
        print("The response of Insight->get_number_of_followers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Insight->get_number_of_followers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **str**| Date for which to retrieve the number of followers.  Format: yyyyMMdd (e.g. 20191231) Timezone: UTC+9  | [optional] 

### Return type

[**GetNumberOfFollowersResponse**](GetNumberOfFollowersResponse.md)

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

# **get_number_of_message_deliveries**
> GetNumberOfMessageDeliveriesResponse get_number_of_message_deliveries(var_date)

Get number of message deliveries

Returns the number of messages sent from LINE Official Account on a specified day. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.insight
from linebot.v3.insight.models.get_number_of_message_deliveries_response import GetNumberOfMessageDeliveriesResponse
from linebot.v3.insight.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.insight.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.insight.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.insight.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.insight.Insight(api_client)
    var_date = 'var_date_example' # str | Date for which to retrieve number of sent messages. - Format: yyyyMMdd (e.g. 20191231) - Timezone: UTC+9 

    try:
        # Get number of message deliveries
        api_response = api_instance.get_number_of_message_deliveries(var_date)
        print("The response of Insight->get_number_of_message_deliveries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Insight->get_number_of_message_deliveries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **str**| Date for which to retrieve number of sent messages. - Format: yyyyMMdd (e.g. 20191231) - Timezone: UTC+9  | 

### Return type

[**GetNumberOfMessageDeliveriesResponse**](GetNumberOfMessageDeliveriesResponse.md)

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

# **get_rich_menu_insight_daily**
> GetRichMenuInsightDailyResponse get_rich_menu_insight_daily(rich_menu_id, var_from, to)

Get rich menu insight daily

Gets rich menu statistics broken down by day for the specified period, for a rich menu created via the Messaging API. Returns the daily impression count for the whole rich menu and the daily click count for each tappable area. When the total number of unique clicks during the period is below the privacy threshold, only `richMenuId` is returned and the other fields are omitted. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.insight
from linebot.v3.insight.models.get_rich_menu_insight_daily_response import GetRichMenuInsightDailyResponse
from linebot.v3.insight.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.insight.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.insight.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.insight.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.insight.Insight(api_client)
    rich_menu_id = 'richmenu-0123456789abcdef0123456789abcdef' # str | ID of the rich menu created via the Messaging API.
    var_from = '20260213' # str | Start date of the aggregation period (inclusive). Must be within the most recent 3 years.  Format: yyyyMMdd (e.g. 20260213) Time zone: UTC+9 
    to = '20260215' # str | End date of the aggregation period (inclusive). The end date can be specified for up to 99 days after the start date.  Format: yyyyMMdd (e.g. 20260215) Time zone: UTC+9 

    try:
        # Get rich menu insight daily
        api_response = api_instance.get_rich_menu_insight_daily(rich_menu_id, var_from, to)
        print("The response of Insight->get_rich_menu_insight_daily:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Insight->get_rich_menu_insight_daily: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rich_menu_id** | **str**| ID of the rich menu created via the Messaging API. | 
 **var_from** | **str**| Start date of the aggregation period (inclusive). Must be within the most recent 3 years.  Format: yyyyMMdd (e.g. 20260213) Time zone: UTC+9  | 
 **to** | **str**| End date of the aggregation period (inclusive). The end date can be specified for up to 99 days after the start date.  Format: yyyyMMdd (e.g. 20260215) Time zone: UTC+9  | 

### Return type

[**GetRichMenuInsightDailyResponse**](GetRichMenuInsightDailyResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request. The `from` or `to` parameter is missing or invalid, or the aggregation period exceeds the allowed maximum. |  -  |
**404** | Not found. The specified rich menu does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rich_menu_insight_summary**
> GetRichMenuInsightSummaryResponse get_rich_menu_insight_summary(rich_menu_id, var_from, to)

Get rich menu insight summary

Gets a summary of rich menu statistics for the specified period, for a rich menu created via the Messaging API. Returns the total impression count for the whole rich menu and the click count for each tappable area, aggregated over the entire period as a single result. When the total number of unique clicks during the period is below the privacy threshold, only `richMenuId` is returned and the other fields are omitted. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.insight
from linebot.v3.insight.models.get_rich_menu_insight_summary_response import GetRichMenuInsightSummaryResponse
from linebot.v3.insight.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.insight.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.insight.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.insight.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.insight.Insight(api_client)
    rich_menu_id = 'richmenu-0123456789abcdef0123456789abcdef' # str | ID of the rich menu created via the Messaging API.
    var_from = '20260213' # str | Start date of the aggregation period (inclusive). Must be within the most recent 3 years.  Format: yyyyMMdd (e.g. 20260213) Time zone: UTC+9 
    to = '20260215' # str | End date of the aggregation period (inclusive). The end date can be specified for up to 396 days after the start date.  Format: yyyyMMdd (e.g. 20260215) Time zone: UTC+9 

    try:
        # Get rich menu insight summary
        api_response = api_instance.get_rich_menu_insight_summary(rich_menu_id, var_from, to)
        print("The response of Insight->get_rich_menu_insight_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Insight->get_rich_menu_insight_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rich_menu_id** | **str**| ID of the rich menu created via the Messaging API. | 
 **var_from** | **str**| Start date of the aggregation period (inclusive). Must be within the most recent 3 years.  Format: yyyyMMdd (e.g. 20260213) Time zone: UTC+9  | 
 **to** | **str**| End date of the aggregation period (inclusive). The end date can be specified for up to 396 days after the start date.  Format: yyyyMMdd (e.g. 20260215) Time zone: UTC+9  | 

### Return type

[**GetRichMenuInsightSummaryResponse**](GetRichMenuInsightSummaryResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request. The `from` or `to` parameter is missing or invalid, or the aggregation period exceeds the allowed maximum. |  -  |
**404** | Not found. The specified rich menu does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statistics_per_unit**
> GetStatisticsPerUnitResponse get_statistics_per_unit(custom_aggregation_unit, var_from, to)



You can check the per-unit statistics of how users interact with push messages and multicast messages sent from your LINE Official Account. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.insight
from linebot.v3.insight.models.get_statistics_per_unit_response import GetStatisticsPerUnitResponse
from linebot.v3.insight.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.insight.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.insight.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.insight.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.insight.Insight(api_client)
    custom_aggregation_unit = 'custom_aggregation_unit_example' # str | Name of aggregation unit specified when sending the message. Case-sensitive. For example, `Promotion_a` and `Promotion_A` are regarded as different unit names. 
    var_from = '20210301' # str | Start date of aggregation period.  Format: yyyyMMdd (e.g. 20210301) Time zone: UTC+9 
    to = '20210301' # str | End date of aggregation period. The end date can be specified for up to 30 days later. For example, if the start date is 20210301, the latest end date is 20210331.  Format: yyyyMMdd (e.g. 20210301) Time zone: UTC+9 

    try:
        api_response = api_instance.get_statistics_per_unit(custom_aggregation_unit, var_from, to)
        print("The response of Insight->get_statistics_per_unit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Insight->get_statistics_per_unit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_aggregation_unit** | **str**| Name of aggregation unit specified when sending the message. Case-sensitive. For example, `Promotion_a` and `Promotion_A` are regarded as different unit names.  | 
 **var_from** | **str**| Start date of aggregation period.  Format: yyyyMMdd (e.g. 20210301) Time zone: UTC+9  | 
 **to** | **str**| End date of aggregation period. The end date can be specified for up to 30 days later. For example, if the start date is 20210301, the latest end date is 20210331.  Format: yyyyMMdd (e.g. 20210301) Time zone: UTC+9  | 

### Return type

[**GetStatisticsPerUnitResponse**](GetStatisticsPerUnitResponse.md)

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


