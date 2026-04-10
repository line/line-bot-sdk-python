# FlexVideo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**preview_url** | **str** |  | 
**alt_content** | [**FlexComponent**](FlexComponent.md) |  | 
**aspect_ratio** | **str** |  | [optional] 
**action** | [**Action**](Action.md) |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.flex_video import FlexVideo

# TODO update the JSON string below
json = "{}"
# create an instance of FlexVideo from a JSON string
flex_video_instance = FlexVideo.from_json(json)
# print the JSON string representation of the object
print FlexVideo.to_json()

# convert the object into a dict
flex_video_dict = flex_video_instance.to_dict()
# create an instance of FlexVideo from a dict
flex_video_form_dict = flex_video.from_dict(flex_video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


