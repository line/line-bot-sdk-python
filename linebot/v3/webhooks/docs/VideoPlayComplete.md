# VideoPlayComplete


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_id** | **str** | ID used to identify a video. Returns the same value as the trackingId assigned to the video message. | 

## Example

```python
from linebot.v3.webhooks.models.video_play_complete import VideoPlayComplete

# TODO update the JSON string below
json = "{}"
# create an instance of VideoPlayComplete from a JSON string
video_play_complete_instance = VideoPlayComplete.from_json(json)
# print the JSON string representation of the object
print VideoPlayComplete.to_json()

# convert the object into a dict
video_play_complete_dict = video_play_complete_instance.to_dict()
# create an instance of VideoPlayComplete from a dict
video_play_complete_form_dict = video_play_complete.from_dict(video_play_complete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


