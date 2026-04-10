# VideoPlayCompleteEvent

Event for when a user finishes viewing a video at least once with the specified trackingId sent by the LINE Official Account.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reply_token** | **str** | Reply token used to send reply message to this event | 
**video_play_complete** | [**VideoPlayComplete**](VideoPlayComplete.md) |  | 

## Example

```python
from linebot.v3.webhooks.models.video_play_complete_event import VideoPlayCompleteEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VideoPlayCompleteEvent from a JSON string
video_play_complete_event_instance = VideoPlayCompleteEvent.from_json(json)
# print the JSON string representation of the object
print VideoPlayCompleteEvent.to_json()

# convert the object into a dict
video_play_complete_event_dict = video_play_complete_event_instance.to_dict()
# create an instance of VideoPlayCompleteEvent from a dict
video_play_complete_event_form_dict = video_play_complete_event.from_dict(video_play_complete_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


