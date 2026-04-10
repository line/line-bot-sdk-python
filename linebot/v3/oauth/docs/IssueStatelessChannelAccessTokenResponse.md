# IssueStatelessChannelAccessTokenResponse

Issued stateless channel access token

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | A stateless channel access token. The token is an opaque string which means its format is an implementation detail and the consumer of this token should never try to use the data parsed from the token.  | 
**expires_in** | **int** | Duration in seconds after which the issued access token expires | 
**token_type** | **str** | Token type. The value is always &#x60;Bearer&#x60;. | [default to 'Bearer']

## Example

```python
from linebot.v3.oauth.models.issue_stateless_channel_access_token_response import IssueStatelessChannelAccessTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IssueStatelessChannelAccessTokenResponse from a JSON string
issue_stateless_channel_access_token_response_instance = IssueStatelessChannelAccessTokenResponse.from_json(json)
# print the JSON string representation of the object
print IssueStatelessChannelAccessTokenResponse.to_json()

# convert the object into a dict
issue_stateless_channel_access_token_response_dict = issue_stateless_channel_access_token_response_instance.to_dict()
# create an instance of IssueStatelessChannelAccessTokenResponse from a dict
issue_stateless_channel_access_token_response_form_dict = issue_stateless_channel_access_token_response.from_dict(issue_stateless_channel_access_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


