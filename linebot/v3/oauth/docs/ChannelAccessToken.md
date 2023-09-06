# linebot.v3.oauth.ChannelAccessToken

All URIs are relative to *https://api.line.me*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gets_all_valid_channel_access_token_key_ids**](ChannelAccessToken.md#gets_all_valid_channel_access_token_key_ids) | **GET** /oauth2/v2.1/tokens/kid | 
[**issue_channel_token**](ChannelAccessToken.md#issue_channel_token) | **POST** /v2/oauth/accessToken | 
[**issue_channel_token_by_jwt**](ChannelAccessToken.md#issue_channel_token_by_jwt) | **POST** /oauth2/v2.1/token | 
[**issue_stateless_channel_token**](ChannelAccessToken.md#issue_stateless_channel_token) | **POST** /oauth2/v3/token | 
[**revoke_channel_token**](ChannelAccessToken.md#revoke_channel_token) | **POST** /v2/oauth/revoke | 
[**revoke_channel_token_by_jwt**](ChannelAccessToken.md#revoke_channel_token_by_jwt) | **POST** /oauth2/v2.1/revoke | 
[**verify_channel_token**](ChannelAccessToken.md#verify_channel_token) | **POST** /v2/oauth/verify | 
[**verify_channel_token_by_jwt**](ChannelAccessToken.md#verify_channel_token_by_jwt) | **GET** /oauth2/v2.1/verify | 


# **gets_all_valid_channel_access_token_key_ids**
> ChannelAccessTokenKeyIdsResponse gets_all_valid_channel_access_token_key_ids(client_assertion_type, client_assertion)



Gets all valid channel access token key IDs.

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.oauth
from linebot.v3.oauth.models.channel_access_token_key_ids_response import ChannelAccessTokenKeyIdsResponse
from linebot.v3.oauth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.oauth.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.oauth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.oauth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.oauth.ChannelAccessToken(api_client)
    client_assertion_type = 'client_assertion_type_example' # str | `urn:ietf:params:oauth:client-assertion-type:jwt-bearer`
    client_assertion = 'client_assertion_example' # str | A JSON Web Token (JWT) (opens new window)the client needs to create and sign with the private key.

    try:
        api_response = api_instance.gets_all_valid_channel_access_token_key_ids(client_assertion_type, client_assertion)
        print("The response of ChannelAccessToken->gets_all_valid_channel_access_token_key_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelAccessToken->gets_all_valid_channel_access_token_key_ids: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_assertion_type** | **str**| &#x60;urn:ietf:params:oauth:client-assertion-type:jwt-bearer&#x60; | 
 **client_assertion** | **str**| A JSON Web Token (JWT) (opens new window)the client needs to create and sign with the private key. | 

### Return type

[**ChannelAccessTokenKeyIdsResponse**](ChannelAccessTokenKeyIdsResponse.md)

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

# **issue_channel_token**
> IssueShortLivedChannelAccessTokenResponse issue_channel_token(grant_type=grant_type, client_id=client_id, client_secret=client_secret)



Issue short-lived channel access token

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.oauth
from linebot.v3.oauth.models.issue_short_lived_channel_access_token_response import IssueShortLivedChannelAccessTokenResponse
from linebot.v3.oauth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.oauth.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.oauth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.oauth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.oauth.ChannelAccessToken(api_client)
    grant_type = 'grant_type_example' # str | `client_credentials` (optional)
    client_id = 'client_id_example' # str | Channel ID. (optional)
    client_secret = 'client_secret_example' # str | Channel secret. (optional)

    try:
        api_response = api_instance.issue_channel_token(grant_type=grant_type, client_id=client_id, client_secret=client_secret)
        print("The response of ChannelAccessToken->issue_channel_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelAccessToken->issue_channel_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| &#x60;client_credentials&#x60; | [optional] 
 **client_id** | **str**| Channel ID. | [optional] 
 **client_secret** | **str**| Channel secret. | [optional] 

### Return type

[**IssueShortLivedChannelAccessTokenResponse**](IssueShortLivedChannelAccessTokenResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_channel_token_by_jwt**
> IssueChannelAccessTokenResponse issue_channel_token_by_jwt(grant_type=grant_type, client_assertion_type=client_assertion_type, client_assertion=client_assertion)



Issues a channel access token that allows you to specify a desired expiration date. This method lets you use JWT assertion for authentication.

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.oauth
from linebot.v3.oauth.models.issue_channel_access_token_response import IssueChannelAccessTokenResponse
from linebot.v3.oauth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.oauth.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.oauth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.oauth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.oauth.ChannelAccessToken(api_client)
    grant_type = 'grant_type_example' # str | client_credentials (optional)
    client_assertion_type = 'client_assertion_type_example' # str | urn:ietf:params:oauth:client-assertion-type:jwt-bearer (optional)
    client_assertion = 'client_assertion_example' # str | A JSON Web Token the client needs to create and sign with the private key of the Assertion Signing Key. (optional)

    try:
        api_response = api_instance.issue_channel_token_by_jwt(grant_type=grant_type, client_assertion_type=client_assertion_type, client_assertion=client_assertion)
        print("The response of ChannelAccessToken->issue_channel_token_by_jwt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelAccessToken->issue_channel_token_by_jwt: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| client_credentials | [optional] 
 **client_assertion_type** | **str**| urn:ietf:params:oauth:client-assertion-type:jwt-bearer | [optional] 
 **client_assertion** | **str**| A JSON Web Token the client needs to create and sign with the private key of the Assertion Signing Key. | [optional] 

### Return type

[**IssueChannelAccessTokenResponse**](IssueChannelAccessTokenResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_stateless_channel_token**
> IssueStatelessChannelAccessTokenResponse issue_stateless_channel_token(grant_type, client_assertion_type, client_assertion, client_id, client_secret)



Issues a new stateless channel access token, which doesn't have max active token limit unlike the other token types. The newly issued token is only valid for 15 minutes but can not be revoked until it naturally expires. 

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.oauth
from linebot.v3.oauth.models.issue_stateless_channel_access_token_response import IssueStatelessChannelAccessTokenResponse
from linebot.v3.oauth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.oauth.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.oauth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.oauth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.oauth.ChannelAccessToken(api_client)
    grant_type = 'grant_type_example' # str | `client_credentials`
    client_assertion_type = 'client_assertion_type_example' # str | URL-encoded value of `urn:ietf:params:oauth:client-assertion-type:jwt-bearer`
    client_assertion = 'client_assertion_example' # str | A JSON Web Token the client needs to create and sign with the private key of the Assertion Signing Key.
    client_id = 'client_id_example' # str | Channel ID.
    client_secret = 'client_secret_example' # str | Channel secret.

    try:
        api_response = api_instance.issue_stateless_channel_token(grant_type, client_assertion_type, client_assertion, client_id, client_secret)
        print("The response of ChannelAccessToken->issue_stateless_channel_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelAccessToken->issue_stateless_channel_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| &#x60;client_credentials&#x60; | 
 **client_assertion_type** | **str**| URL-encoded value of &#x60;urn:ietf:params:oauth:client-assertion-type:jwt-bearer&#x60; | 
 **client_assertion** | **str**| A JSON Web Token the client needs to create and sign with the private key of the Assertion Signing Key. | 
 **client_id** | **str**| Channel ID. | 
 **client_secret** | **str**| Channel secret. | 

### Return type

[**IssueStatelessChannelAccessTokenResponse**](IssueStatelessChannelAccessTokenResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_channel_token**
> revoke_channel_token(access_token=access_token)



Revoke short-lived or long-lived channel access token

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.oauth
from linebot.v3.oauth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.oauth.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.oauth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.oauth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.oauth.ChannelAccessToken(api_client)
    access_token = 'access_token_example' # str | Channel access token (optional)

    try:
        api_instance.revoke_channel_token(access_token=access_token)
    except Exception as e:
        print("Exception when calling ChannelAccessToken->revoke_channel_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Channel access token | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_channel_token_by_jwt**
> revoke_channel_token_by_jwt(client_id=client_id, client_secret=client_secret, access_token=access_token)



Revoke channel access token v2.1

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.oauth
from linebot.v3.oauth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.oauth.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.oauth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.oauth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.oauth.ChannelAccessToken(api_client)
    client_id = 'client_id_example' # str | Channel ID (optional)
    client_secret = 'client_secret_example' # str | Channel Secret (optional)
    access_token = 'access_token_example' # str | Channel access token (optional)

    try:
        api_instance.revoke_channel_token_by_jwt(client_id=client_id, client_secret=client_secret, access_token=access_token)
    except Exception as e:
        print("Exception when calling ChannelAccessToken->revoke_channel_token_by_jwt: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| Channel ID | [optional] 
 **client_secret** | **str**| Channel Secret | [optional] 
 **access_token** | **str**| Channel access token | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_channel_token**
> VerifyChannelAccessTokenResponse verify_channel_token(access_token=access_token)



Verify the validity of short-lived and long-lived channel access tokens

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.oauth
from linebot.v3.oauth.models.verify_channel_access_token_response import VerifyChannelAccessTokenResponse
from linebot.v3.oauth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.oauth.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.oauth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.oauth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.oauth.ChannelAccessToken(api_client)
    access_token = 'access_token_example' # str | A short-lived or long-lived channel access token. (optional)

    try:
        api_response = api_instance.verify_channel_token(access_token=access_token)
        print("The response of ChannelAccessToken->verify_channel_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelAccessToken->verify_channel_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| A short-lived or long-lived channel access token. | [optional] 

### Return type

[**VerifyChannelAccessTokenResponse**](VerifyChannelAccessTokenResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_channel_token_by_jwt**
> VerifyChannelAccessTokenResponse verify_channel_token_by_jwt(access_token)



You can verify whether a Channel access token with a user-specified expiration (Channel Access Token v2.1) is valid.

### Example

* Bearer Authentication (Bearer):
```python
import time
import os
import linebot.v3.oauth
from linebot.v3.oauth.models.verify_channel_access_token_response import VerifyChannelAccessTokenResponse
from linebot.v3.oauth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.line.me
# See configuration.py for a list of all supported configuration parameters.
configuration = linebot.v3.oauth.Configuration(
    host = "https://api.line.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = linebot.v3.oauth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with linebot.v3.oauth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linebot.v3.oauth.ChannelAccessToken(api_client)
    access_token = 'access_token_example' # str | Channel access token with a user-specified expiration (Channel Access Token v2.1).

    try:
        api_response = api_instance.verify_channel_token_by_jwt(access_token)
        print("The response of ChannelAccessToken->verify_channel_token_by_jwt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelAccessToken->verify_channel_token_by_jwt: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Channel access token with a user-specified expiration (Channel Access Token v2.1). | 

### Return type

[**VerifyChannelAccessTokenResponse**](VerifyChannelAccessTokenResponse.md)

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

