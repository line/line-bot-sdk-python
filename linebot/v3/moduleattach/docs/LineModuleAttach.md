# linebot.v3.moduleattach.LineModuleAttach

All URIs are relative to *https://manager.line.biz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_module**](LineModuleAttach.md#attach_module) | **POST** /module/auth/v1/token | 


# **attach_module**
> AttachModuleResponse attach_module(grant_type=grant_type, code=code, redirect_uri=redirect_uri, code_verifier=code_verifier, client_id=client_id, client_secret=client_secret, region=region, basic_search_id=basic_search_id, scope=scope, brand_type=brand_type)



Attach by operation of the module channel provider

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import linebot.v3.moduleattach
from linebot.v3.moduleattach.models.attach_module_response import AttachModuleResponse
from linebot.v3.moduleattach.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://manager.line.biz
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.moduleattach.Configuration(
    host = "https://manager.line.biz"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = linebot.v3.moduleattach.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with linebot.v3.moduleattach.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.moduleattach.LineModuleAttach(api_client)
    grant_type = 'grant_type_example' # str | authorization_code (optional)
    code = 'code_example' # str | Authorization code received from the LINE Platform. (optional)
    redirect_uri = 'redirect_uri_example' # str | Specify the redirect_uri specified in the URL for authentication and authorization. (optional)
    code_verifier = 'code_verifier_example' # str | Specify when using PKCE (Proof Key for Code Exchange) defined in the OAuth 2.0 extension specification as a countermeasure against authorization code interception attacks. (optional)
    client_id = 'client_id_example' # str | Instead of using Authorization header, you can use this parameter to specify the channel ID of the module channel. You can find the channel ID of the module channel in the LINE Developers Console.  (optional)
    client_secret = 'client_secret_example' # str | Instead of using Authorization header, you can use this parameter to specify the channel secret of the module channel. You can find the channel secret of the module channel in the LINE Developers Console.  (optional)
    region = 'region_example' # str | If you specified a value for region in the URL for authentication and authorization, specify the same value.  (optional)
    basic_search_id = 'basic_search_id_example' # str | If you specified a value for basic_search_id in the URL for authentication and authorization, specify the same value. (optional)
    scope = 'scope_example' # str | If you specified a value for scope in the URL for authentication and authorization, specify the same value. (optional)
    brand_type = 'brand_type_example' # str | If you specified a value for brand_type in the URL for authentication and authorization, specify the same value. (optional)

    try:
        api_response = api_instance.attach_module(grant_type=grant_type, code=code, redirect_uri=redirect_uri, code_verifier=code_verifier, client_id=client_id, client_secret=client_secret, region=region, basic_search_id=basic_search_id, scope=scope, brand_type=brand_type)
        print("The response of LineModuleAttach->attach_module:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LineModuleAttach->attach_module: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| authorization_code | [optional] 
 **code** | **str**| Authorization code received from the LINE Platform. | [optional] 
 **redirect_uri** | **str**| Specify the redirect_uri specified in the URL for authentication and authorization. | [optional] 
 **code_verifier** | **str**| Specify when using PKCE (Proof Key for Code Exchange) defined in the OAuth 2.0 extension specification as a countermeasure against authorization code interception attacks. | [optional] 
 **client_id** | **str**| Instead of using Authorization header, you can use this parameter to specify the channel ID of the module channel. You can find the channel ID of the module channel in the LINE Developers Console.  | [optional] 
 **client_secret** | **str**| Instead of using Authorization header, you can use this parameter to specify the channel secret of the module channel. You can find the channel secret of the module channel in the LINE Developers Console.  | [optional] 
 **region** | **str**| If you specified a value for region in the URL for authentication and authorization, specify the same value.  | [optional] 
 **basic_search_id** | **str**| If you specified a value for basic_search_id in the URL for authentication and authorization, specify the same value. | [optional] 
 **scope** | **str**| If you specified a value for scope in the URL for authentication and authorization, specify the same value. | [optional] 
 **brand_type** | **str**| If you specified a value for brand_type in the URL for authentication and authorization, specify the same value. | [optional] 

### Return type

[**AttachModuleResponse**](AttachModuleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

