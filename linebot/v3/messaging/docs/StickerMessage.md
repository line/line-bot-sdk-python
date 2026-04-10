# StickerMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_id** | **str** |  | 
**sticker_id** | **str** |  | 
**quote_token** | **str** | Quote token of the message you want to quote. | [optional] 

## Example

```python
from linebot.v3.messaging.models.sticker_message import StickerMessage

# TODO update the JSON string below
json = "{}"
# create an instance of StickerMessage from a JSON string
sticker_message_instance = StickerMessage.from_json(json)
# print the JSON string representation of the object
print StickerMessage.to_json()

# convert the object into a dict
sticker_message_dict = sticker_message_instance.to_dict()
# create an instance of StickerMessage from a dict
sticker_message_form_dict = sticker_message.from_dict(sticker_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


