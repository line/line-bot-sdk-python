# AudioMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_content_url** | **str** |  | 
**duration** | **int** |  | 

## Example

```python
from linebot.v3.messaging.models.audio_message import AudioMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AudioMessage from a JSON string
audio_message_instance = AudioMessage.from_json(json)
# print the JSON string representation of the object
print AudioMessage.to_json()

# convert the object into a dict
audio_message_dict = audio_message_instance.to_dict()
# create an instance of AudioMessage from a dict
audio_message_form_dict = audio_message.from_dict(audio_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


