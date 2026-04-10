# VideoMessageContent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **int** | Length of video file (milliseconds) | [optional] 
**content_provider** | [**ContentProvider**](ContentProvider.md) |  | 
**quote_token** | **str** | Quote token to quote this message.  | 
**mark_as_read_token** | **str** | Token used to mark the message as read.  | [optional] 

## Example

```python
from linebot.v3.webhooks.models.video_message_content import VideoMessageContent

# TODO update the JSON string below
json = "{}"
# create an instance of VideoMessageContent from a JSON string
video_message_content_instance = VideoMessageContent.from_json(json)
# print the JSON string representation of the object
print VideoMessageContent.to_json()

# convert the object into a dict
video_message_content_dict = video_message_content_instance.to_dict()
# create an instance of VideoMessageContent from a dict
video_message_content_form_dict = video_message_content.from_dict(video_message_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


