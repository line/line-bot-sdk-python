# IssueShortLivedChannelAccessTokenResponse

Issued short-lived channel access token

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | A short-lived channel access token. Valid for 30 days. Note: Channel access tokens cannot be refreshed.  | 
**expires_in** | **int** | Time until channel access token expires in seconds from time the token is issued. | 
**token_type** | **str** | Token type. The value is always &#x60;Bearer&#x60;. | [default to 'Bearer']

## Example

```python
from linebot.v3.oauth.models.issue_short_lived_channel_access_token_response import IssueShortLivedChannelAccessTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IssueShortLivedChannelAccessTokenResponse from a JSON string
issue_short_lived_channel_access_token_response_instance = IssueShortLivedChannelAccessTokenResponse.from_json(json)
# print the JSON string representation of the object
print IssueShortLivedChannelAccessTokenResponse.to_json()

# convert the object into a dict
issue_short_lived_channel_access_token_response_dict = issue_short_lived_channel_access_token_response_instance.to_dict()
# create an instance of IssueShortLivedChannelAccessTokenResponse from a dict
issue_short_lived_channel_access_token_response_form_dict = issue_short_lived_channel_access_token_response.from_dict(issue_short_lived_channel_access_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


