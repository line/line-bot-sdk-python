# ChannelAccessTokenKeyIdsResponse

Channel access token key IDs

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kids** | **List[str]** | Array of channel access token key IDs. | 

## Example

```python
from linebot.v3.oauth.models.channel_access_token_key_ids_response import ChannelAccessTokenKeyIdsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelAccessTokenKeyIdsResponse from a JSON string
channel_access_token_key_ids_response_instance = ChannelAccessTokenKeyIdsResponse.from_json(json)
# print the JSON string representation of the object
print ChannelAccessTokenKeyIdsResponse.to_json()

# convert the object into a dict
channel_access_token_key_ids_response_dict = channel_access_token_key_ids_response_instance.to_dict()
# create an instance of ChannelAccessTokenKeyIdsResponse from a dict
channel_access_token_key_ids_response_form_dict = channel_access_token_key_ids_response.from_dict(channel_access_token_key_ids_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


