# ImagemapMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_url** | **str** |  | 
**alt_text** | **str** |  | 
**base_size** | [**ImagemapBaseSize**](ImagemapBaseSize.md) |  | 
**actions** | [**List[ImagemapAction]**](ImagemapAction.md) |  | 
**video** | [**ImagemapVideo**](ImagemapVideo.md) |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.imagemap_message import ImagemapMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ImagemapMessage from a JSON string
imagemap_message_instance = ImagemapMessage.from_json(json)
# print the JSON string representation of the object
print ImagemapMessage.to_json()

# convert the object into a dict
imagemap_message_dict = imagemap_message_instance.to_dict()
# create an instance of ImagemapMessage from a dict
imagemap_message_form_dict = imagemap_message.from_dict(imagemap_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


