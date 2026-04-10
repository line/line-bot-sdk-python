# StickerMessageContent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_id** | **str** | Package ID | 
**sticker_id** | **str** | Sticker ID | 
**sticker_resource_type** | **str** |  | 
**keywords** | **List[str]** | Array of up to 15 keywords describing the sticker. If a sticker has 16 or more keywords, a random selection of 15 keywords will be returned. The keyword selection is random for each event, so different keywords may be returned for the same sticker.  | [optional] 
**text** | **str** | Any text entered by the user. This property is only included for message stickers. Max character limit: 100  | [optional] 
**quote_token** | **str** | Quote token to quote this message.  | 
**quoted_message_id** | **str** | Message ID of a quoted message. Only included when the received message quotes a past message.  | [optional] 
**mark_as_read_token** | **str** | Token used to mark the message as read.   | [optional] 

## Example

```python
from linebot.v3.webhooks.models.sticker_message_content import StickerMessageContent

# TODO update the JSON string below
json = "{}"
# create an instance of StickerMessageContent from a JSON string
sticker_message_content_instance = StickerMessageContent.from_json(json)
# print the JSON string representation of the object
print StickerMessageContent.to_json()

# convert the object into a dict
sticker_message_content_dict = sticker_message_content_instance.to_dict()
# create an instance of StickerMessageContent from a dict
sticker_message_content_form_dict = sticker_message_content.from_dict(sticker_message_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


