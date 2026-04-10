# BotInfoResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | Bot&#39;s user ID | 
**basic_id** | **str** | Bot&#39;s basic ID | 
**premium_id** | **str** | Bot&#39;s premium ID. Not included in the response if the premium ID isn&#39;t set. | [optional] 
**display_name** | **str** | Bot&#39;s display name | 
**picture_url** | **str** | Profile image URL. &#x60;https&#x60; image URL. Not included in the response if the bot doesn&#39;t have a profile image. | [optional] 
**chat_mode** | **str** | Chat settings set in the LINE Official Account Manager. One of:  &#x60;chat&#x60;: Chat is set to \&quot;On\&quot;. &#x60;bot&#x60;: Chat is set to \&quot;Off\&quot;.  | 
**mark_as_read_mode** | **str** | Automatic read setting for messages. If the chat is set to \&quot;Off\&quot;, auto is returned. If the chat is set to \&quot;On\&quot;, manual is returned.  &#x60;auto&#x60;: Auto read setting is enabled. &#x60;manual&#x60;: Auto read setting is disabled.   | 

## Example

```python
from linebot.v3.messaging.models.bot_info_response import BotInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BotInfoResponse from a JSON string
bot_info_response_instance = BotInfoResponse.from_json(json)
# print the JSON string representation of the object
print BotInfoResponse.to_json()

# convert the object into a dict
bot_info_response_dict = bot_info_response_instance.to_dict()
# create an instance of BotInfoResponse from a dict
bot_info_response_form_dict = bot_info_response.from_dict(bot_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


