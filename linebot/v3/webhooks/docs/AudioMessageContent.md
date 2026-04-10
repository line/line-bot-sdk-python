# AudioMessageContent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_provider** | [**ContentProvider**](ContentProvider.md) |  | 
**duration** | **int** | Length of audio file (milliseconds) | [optional] 
**mark_as_read_token** | **str** | Token used to mark the message as read.  | [optional] 

## Example

```python
from linebot.v3.webhooks.models.audio_message_content import AudioMessageContent

# TODO update the JSON string below
json = "{}"
# create an instance of AudioMessageContent from a JSON string
audio_message_content_instance = AudioMessageContent.from_json(json)
# print the JSON string representation of the object
print AudioMessageContent.to_json()

# convert the object into a dict
audio_message_content_dict = audio_message_content_instance.to_dict()
# create an instance of AudioMessageContent from a dict
audio_message_content_form_dict = audio_message_content.from_dict(audio_message_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


