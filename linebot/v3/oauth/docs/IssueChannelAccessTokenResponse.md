# IssueChannelAccessTokenResponse

Issued channel access token

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Channel access token.  | 
**expires_in** | **int** | Amount of time in seconds from issue to expiration of the channel access token | 
**token_type** | **str** | A token type. | [default to 'Bearer']
**key_id** | **str** | Unique key ID for identifying the channel access token. | 

## Example

```python
from linebot.v3.oauth.models.issue_channel_access_token_response import IssueChannelAccessTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IssueChannelAccessTokenResponse from a JSON string
issue_channel_access_token_response_instance = IssueChannelAccessTokenResponse.from_json(json)
# print the JSON string representation of the object
print IssueChannelAccessTokenResponse.to_json()

# convert the object into a dict
issue_channel_access_token_response_dict = issue_channel_access_token_response_instance.to_dict()
# create an instance of IssueChannelAccessTokenResponse from a dict
issue_channel_access_token_response_form_dict = issue_channel_access_token_response.from_dict(issue_channel_access_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


