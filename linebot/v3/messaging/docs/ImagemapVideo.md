# ImagemapVideo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_content_url** | **str** |  | [optional] 
**preview_image_url** | **str** |  | [optional] 
**area** | [**ImagemapArea**](ImagemapArea.md) |  | [optional] 
**external_link** | [**ImagemapExternalLink**](ImagemapExternalLink.md) |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.imagemap_video import ImagemapVideo

# TODO update the JSON string below
json = "{}"
# create an instance of ImagemapVideo from a JSON string
imagemap_video_instance = ImagemapVideo.from_json(json)
# print the JSON string representation of the object
print ImagemapVideo.to_json()

# convert the object into a dict
imagemap_video_dict = imagemap_video_instance.to_dict()
# create an instance of ImagemapVideo from a dict
imagemap_video_form_dict = imagemap_video.from_dict(imagemap_video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


