# linebot.audience.ManageAudienceApi

All URIs are relative to *https://api.line.me*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_audience_group**](ManageAudienceApi.md#activate_audience_group) | **PUT** /v2/bot/audienceGroup/{audienceGroupId}/activate | 
[**add_audience_to_audience_group**](ManageAudienceApi.md#add_audience_to_audience_group) | **PUT** /v2/bot/audienceGroup/upload | 
[**create_audience_group**](ManageAudienceApi.md#create_audience_group) | **POST** /v2/bot/audienceGroup/upload | 
[**create_click_based_audience_group**](ManageAudienceApi.md#create_click_based_audience_group) | **POST** /v2/bot/audienceGroup/click | 
[**create_imp_based_audience_group**](ManageAudienceApi.md#create_imp_based_audience_group) | **POST** /v2/bot/audienceGroup/imp | 
[**delete_audience_group**](ManageAudienceApi.md#delete_audience_group) | **DELETE** /v2/bot/audienceGroup/{audienceGroupId} | 
[**get_audience_data**](ManageAudienceApi.md#get_audience_data) | **GET** /v2/bot/audienceGroup/{audienceGroupId} | 
[**get_audience_group_authority_level**](ManageAudienceApi.md#get_audience_group_authority_level) | **GET** /v2/bot/audienceGroup/authorityLevel | 
[**get_audience_groups**](ManageAudienceApi.md#get_audience_groups) | **GET** /v2/bot/audienceGroup/list | 
[**update_audience_group_authority_level**](ManageAudienceApi.md#update_audience_group_authority_level) | **PUT** /v2/bot/audienceGroup/authorityLevel | 
[**update_audience_group_description**](ManageAudienceApi.md#update_audience_group_description) | **PUT** /v2/bot/audienceGroup/{audienceGroupId}/updateDescription | 


# **activate_audience_group**
> activate_audience_group(audience_group_id)



Activate audience

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.audience
from linebot.audience.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.audience.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.audience.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.audience.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.audience.ManageAudienceApi(api_client)
    audience_group_id = 56 # int | The audience ID.

    try:
        api_instance.activate_audience_group(audience_group_id)
    except Exception as e:
        print("Exception when calling ManageAudienceApi->activate_audience_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_group_id** | **int**| The audience ID. | 

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
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_audience_to_audience_group**
> add_audience_to_audience_group(add_audience_to_audience_group_request)



Add user IDs or Identifiers for Advertisers (IFAs) to an audience for uploading user IDs (by JSON)

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.audience
from linebot.audience.models.add_audience_to_audience_group_request import AddAudienceToAudienceGroupRequest
from linebot.audience.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.audience.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.audience.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.audience.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.audience.ManageAudienceApi(api_client)
    add_audience_to_audience_group_request = linebot.audience.AddAudienceToAudienceGroupRequest() # AddAudienceToAudienceGroupRequest | 

    try:
        api_instance.add_audience_to_audience_group(add_audience_to_audience_group_request)
    except Exception as e:
        print("Exception when calling ManageAudienceApi->add_audience_to_audience_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_audience_to_audience_group_request** | [**AddAudienceToAudienceGroupRequest**](AddAudienceToAudienceGroupRequest.md)|  | 

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

# **create_audience_group**
> CreateAudienceGroupResponse create_audience_group(create_audience_group_request)



Create audience for uploading user IDs (by JSON)

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.audience
from linebot.audience.models.create_audience_group_request import CreateAudienceGroupRequest
from linebot.audience.models.create_audience_group_response import CreateAudienceGroupResponse
from linebot.audience.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.audience.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.audience.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.audience.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.audience.ManageAudienceApi(api_client)
    create_audience_group_request = linebot.audience.CreateAudienceGroupRequest() # CreateAudienceGroupRequest | 

    try:
        api_response = api_instance.create_audience_group(create_audience_group_request)
        print("The response of ManageAudienceApi->create_audience_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManageAudienceApi->create_audience_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_audience_group_request** | [**CreateAudienceGroupRequest**](CreateAudienceGroupRequest.md)|  | 

### Return type

[**CreateAudienceGroupResponse**](CreateAudienceGroupResponse.md)

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

# **create_click_based_audience_group**
> CreateClickBasedAudienceGroupResponse create_click_based_audience_group(create_click_based_audience_group_request)



Create audience for click-based retargeting

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.audience
from linebot.audience.models.create_click_based_audience_group_request import CreateClickBasedAudienceGroupRequest
from linebot.audience.models.create_click_based_audience_group_response import CreateClickBasedAudienceGroupResponse
from linebot.audience.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.audience.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.audience.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.audience.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.audience.ManageAudienceApi(api_client)
    create_click_based_audience_group_request = linebot.audience.CreateClickBasedAudienceGroupRequest() # CreateClickBasedAudienceGroupRequest | 

    try:
        api_response = api_instance.create_click_based_audience_group(create_click_based_audience_group_request)
        print("The response of ManageAudienceApi->create_click_based_audience_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManageAudienceApi->create_click_based_audience_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_click_based_audience_group_request** | [**CreateClickBasedAudienceGroupRequest**](CreateClickBasedAudienceGroupRequest.md)|  | 

### Return type

[**CreateClickBasedAudienceGroupResponse**](CreateClickBasedAudienceGroupResponse.md)

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

# **create_imp_based_audience_group**
> CreateImpBasedAudienceGroupResponse create_imp_based_audience_group(create_imp_based_audience_group_request)



Create audience for impression-based retargeting

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.audience
from linebot.audience.models.create_imp_based_audience_group_request import CreateImpBasedAudienceGroupRequest
from linebot.audience.models.create_imp_based_audience_group_response import CreateImpBasedAudienceGroupResponse
from linebot.audience.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.audience.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.audience.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.audience.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.audience.ManageAudienceApi(api_client)
    create_imp_based_audience_group_request = linebot.audience.CreateImpBasedAudienceGroupRequest() # CreateImpBasedAudienceGroupRequest | 

    try:
        api_response = api_instance.create_imp_based_audience_group(create_imp_based_audience_group_request)
        print("The response of ManageAudienceApi->create_imp_based_audience_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManageAudienceApi->create_imp_based_audience_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_imp_based_audience_group_request** | [**CreateImpBasedAudienceGroupRequest**](CreateImpBasedAudienceGroupRequest.md)|  | 

### Return type

[**CreateImpBasedAudienceGroupResponse**](CreateImpBasedAudienceGroupResponse.md)

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

# **delete_audience_group**
> delete_audience_group(audience_group_id)



Delete audience

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.audience
from linebot.audience.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.audience.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.audience.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.audience.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.audience.ManageAudienceApi(api_client)
    audience_group_id = 56 # int | The audience ID.

    try:
        api_instance.delete_audience_group(audience_group_id)
    except Exception as e:
        print("Exception when calling ManageAudienceApi->delete_audience_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_group_id** | **int**| The audience ID. | 

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

# **get_audience_data**
> GetAudienceDataResponse get_audience_data(audience_group_id)



Gets audience data.

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.audience
from linebot.audience.models.get_audience_data_response import GetAudienceDataResponse
from linebot.audience.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.audience.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.audience.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.audience.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.audience.ManageAudienceApi(api_client)
    audience_group_id = 56 # int | The audience ID.

    try:
        api_response = api_instance.get_audience_data(audience_group_id)
        print("The response of ManageAudienceApi->get_audience_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManageAudienceApi->get_audience_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_group_id** | **int**| The audience ID. | 

### Return type

[**GetAudienceDataResponse**](GetAudienceDataResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audience_group_authority_level**
> GetAudienceGroupAuthorityLevelResponse get_audience_group_authority_level()



Get the authority level of the audience

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.audience
from linebot.audience.models.get_audience_group_authority_level_response import GetAudienceGroupAuthorityLevelResponse
from linebot.audience.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.audience.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.audience.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.audience.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.audience.ManageAudienceApi(api_client)

    try:
        api_response = api_instance.get_audience_group_authority_level()
        print("The response of ManageAudienceApi->get_audience_group_authority_level:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManageAudienceApi->get_audience_group_authority_level: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAudienceGroupAuthorityLevelResponse**](GetAudienceGroupAuthorityLevelResponse.md)

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

# **get_audience_groups**
> GetAudienceGroupsResponse get_audience_groups(page, description, status, size, includes_external_public_groups, create_route)



Gets data for more than one audience.

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.audience
from linebot.audience.models.audience_group_create_route import AudienceGroupCreateRoute
from linebot.audience.models.audience_group_status import AudienceGroupStatus
from linebot.audience.models.get_audience_groups_response import GetAudienceGroupsResponse
from linebot.audience.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.audience.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.audience.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.audience.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.audience.ManageAudienceApi(api_client)
    page = 56 # int | The page to return when getting (paginated) results. Must be 1 or higher.
    description = 'description_example' # str | The name of the audience(s) to return. You can search for partial matches. This is case-insensitive, meaning AUDIENCE and audience are considered identical. If omitted, the name of the audience(s) will not be used as a search criterion. 
    status = linebot.audience.AudienceGroupStatus() # AudienceGroupStatus | The status of the audience(s) to return. If omitted, the status of the audience(s) will not be used as a search criterion. 
    size = 20 # int | The number of audiences per page. Default: 20 Max: 40 
    includes_external_public_groups = true # bool | true (default): Get public audiences created in all channels linked to the same bot. false: Get audiences created in the same channel. 
    create_route = linebot.audience.AudienceGroupCreateRoute() # AudienceGroupCreateRoute | How the audience was created. If omitted, all audiences are included.  `OA_MANAGER`: Return only audiences created with LINE Official Account Manager (opens new window). `MESSAGING_API`: Return only audiences created with Messaging API. 

    try:
        api_response = api_instance.get_audience_groups(page, description, status, size, includes_external_public_groups, create_route)
        print("The response of ManageAudienceApi->get_audience_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManageAudienceApi->get_audience_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page to return when getting (paginated) results. Must be 1 or higher. | 
 **description** | **str**| The name of the audience(s) to return. You can search for partial matches. This is case-insensitive, meaning AUDIENCE and audience are considered identical. If omitted, the name of the audience(s) will not be used as a search criterion.  | 
 **status** | [**AudienceGroupStatus**](.md)| The status of the audience(s) to return. If omitted, the status of the audience(s) will not be used as a search criterion.  | 
 **size** | **int**| The number of audiences per page. Default: 20 Max: 40  | 
 **includes_external_public_groups** | **bool**| true (default): Get public audiences created in all channels linked to the same bot. false: Get audiences created in the same channel.  | 
 **create_route** | [**AudienceGroupCreateRoute**](.md)| How the audience was created. If omitted, all audiences are included.  &#x60;OA_MANAGER&#x60;: Return only audiences created with LINE Official Account Manager (opens new window). &#x60;MESSAGING_API&#x60;: Return only audiences created with Messaging API.  | 

### Return type

[**GetAudienceGroupsResponse**](GetAudienceGroupsResponse.md)

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

# **update_audience_group_authority_level**
> update_audience_group_authority_level(update_audience_group_authority_level_request)



Change the authority level of the audience

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.audience
from linebot.audience.models.update_audience_group_authority_level_request import UpdateAudienceGroupAuthorityLevelRequest
from linebot.audience.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.audience.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.audience.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.audience.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.audience.ManageAudienceApi(api_client)
    update_audience_group_authority_level_request = linebot.audience.UpdateAudienceGroupAuthorityLevelRequest() # UpdateAudienceGroupAuthorityLevelRequest | 

    try:
        api_instance.update_audience_group_authority_level(update_audience_group_authority_level_request)
    except Exception as e:
        print("Exception when calling ManageAudienceApi->update_audience_group_authority_level: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_audience_group_authority_level_request** | [**UpdateAudienceGroupAuthorityLevelRequest**](UpdateAudienceGroupAuthorityLevelRequest.md)|  | 

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

# **update_audience_group_description**
> update_audience_group_description(audience_group_id, update_audience_group_description_request)



Renames an existing audience.

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.audience
from linebot.audience.models.update_audience_group_description_request import UpdateAudienceGroupDescriptionRequest
from linebot.audience.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.audience.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.audience.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.audience.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.audience.ManageAudienceApi(api_client)
    audience_group_id = 56 # int | The audience ID.
    update_audience_group_description_request = linebot.audience.UpdateAudienceGroupDescriptionRequest() # UpdateAudienceGroupDescriptionRequest | 

    try:
        api_instance.update_audience_group_description(audience_group_id, update_audience_group_description_request)
    except Exception as e:
        print("Exception when calling ManageAudienceApi->update_audience_group_description: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_group_id** | **int**| The audience ID. | 
 **update_audience_group_description_request** | [**UpdateAudienceGroupDescriptionRequest**](UpdateAudienceGroupDescriptionRequest.md)|  | 

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

