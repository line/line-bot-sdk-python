# VideoMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_content_url** | **str** |  | 
**preview_image_url** | **str** |  | 
**tracking_id** | **str** |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.video_message import VideoMessage

# TODO update the JSON string below
json = "{}"
# create an instance of VideoMessage from a JSON string
video_message_instance = VideoMessage.from_json(json)
# print the JSON string representation of the object
print VideoMessage.to_json()

# convert the object into a dict
video_message_dict = video_message_instance.to_dict()
# create an instance of VideoMessage from a dict
video_message_form_dict = video_message.from_dict(video_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


