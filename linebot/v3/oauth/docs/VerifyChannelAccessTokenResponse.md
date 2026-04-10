# VerifyChannelAccessTokenResponse

Verification result

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | The channel ID for which the channel access token was issued. | 
**expires_in** | **int** | Number of seconds before the channel access token expires. | 
**scope** | **str** | Permissions granted to the channel access token. | [optional] 

## Example

```python
from linebot.v3.oauth.models.verify_channel_access_token_response import VerifyChannelAccessTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyChannelAccessTokenResponse from a JSON string
verify_channel_access_token_response_instance = VerifyChannelAccessTokenResponse.from_json(json)
# print the JSON string representation of the object
print VerifyChannelAccessTokenResponse.to_json()

# convert the object into a dict
verify_channel_access_token_response_dict = verify_channel_access_token_response_instance.to_dict()
# create an instance of VerifyChannelAccessTokenResponse from a dict
verify_channel_access_token_response_form_dict = verify_channel_access_token_response.from_dict(verify_channel_access_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


