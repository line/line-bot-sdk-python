# linebot.v3.audience.ManageAudienceBlob

All URIs are relative to *https://api.line.me*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_ids_to_audience**](ManageAudienceBlob.md#add_user_ids_to_audience) | **PUT** /v2/bot/audienceGroup/upload/byFile | 
[**create_audience_for_uploading_user_ids**](ManageAudienceBlob.md#create_audience_for_uploading_user_ids) | **POST** /v2/bot/audienceGroup/upload/byFile | 


# **add_user_ids_to_audience**
> add_user_ids_to_audience(file, audience_group_id=audience_group_id, upload_description=upload_description)



Add user IDs or Identifiers for Advertisers (IFAs) to an audience for uploading user IDs (by file).

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.audience
from linebot.v3.audience.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.audience.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.audience.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.audience.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.audience.ManageAudienceBlob(api_client)
    file = None # bytearray | A text file with one user ID or IFA entered per line. Specify text/plain as Content-Type. Max file number: 1 Max number: 1,500,000 
    audience_group_id = 56 # int | The audience ID. (optional)
    upload_description = 'upload_description_example' # str | The description to register with the job (optional)

    try:
        api_instance.add_user_ids_to_audience(file, audience_group_id=audience_group_id, upload_description=upload_description)
    except Exception as e:
        print("Exception when calling ManageAudienceBlob->add_user_ids_to_audience: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| A text file with one user ID or IFA entered per line. Specify text/plain as Content-Type. Max file number: 1 Max number: 1,500,000  | 
 **audience_group_id** | **int**| The audience ID. | [optional] 
 **upload_description** | **str**| The description to register with the job | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_audience_for_uploading_user_ids**
> CreateAudienceGroupResponse create_audience_for_uploading_user_ids(file, description=description, is_ifa_audience=is_ifa_audience, upload_description=upload_description)



Create audience for uploading user IDs (by file).

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.audience
from linebot.v3.audience.models.create_audience_group_response import CreateAudienceGroupResponse
from linebot.v3.audience.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.audience.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.audience.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.audience.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.audience.ManageAudienceBlob(api_client)
    file = None # bytearray | A text file with one user ID or IFA entered per line. Specify text/plain as Content-Type. Max file number: 1 Max number: 1,500,000 
    description = 'description_example' # str | The audience's name. This is case-insensitive, meaning AUDIENCE and audience are considered identical. Max character limit: 120  (optional)
    is_ifa_audience = True # bool | To specify recipients by IFAs: set `true`. To specify recipients by user IDs: set `false` or omit isIfaAudience property.  (optional)
    upload_description = 'upload_description_example' # str | The description to register for the job (in `jobs[].description`).  (optional)

    try:
        api_response = api_instance.create_audience_for_uploading_user_ids(file, description=description, is_ifa_audience=is_ifa_audience, upload_description=upload_description)
        print("The response of ManageAudienceBlob->create_audience_for_uploading_user_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManageAudienceBlob->create_audience_for_uploading_user_ids: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| A text file with one user ID or IFA entered per line. Specify text/plain as Content-Type. Max file number: 1 Max number: 1,500,000  | 
 **description** | **str**| The audience&#39;s name. This is case-insensitive, meaning AUDIENCE and audience are considered identical. Max character limit: 120  | [optional] 
 **is_ifa_audience** | **bool**| To specify recipients by IFAs: set &#x60;true&#x60;. To specify recipients by user IDs: set &#x60;false&#x60; or omit isIfaAudience property.  | [optional] 
 **upload_description** | **str**| The description to register for the job (in &#x60;jobs[].description&#x60;).  | [optional] 

### Return type

[**CreateAudienceGroupResponse**](CreateAudienceGroupResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

