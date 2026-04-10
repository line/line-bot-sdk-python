# ImagemapArea


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **int** |  | 
**y** | **int** |  | 
**width** | **int** |  | 
**height** | **int** |  | 

## Example

```python
from linebot.v3.messaging.models.imagemap_area import ImagemapArea

# TODO update the JSON string below
json = "{}"
# create an instance of ImagemapArea from a JSON string
imagemap_area_instance = ImagemapArea.from_json(json)
# print the JSON string representation of the object
print ImagemapArea.to_json()

# convert the object into a dict
imagemap_area_dict = imagemap_area_instance.to_dict()
# create an instance of ImagemapArea from a dict
imagemap_area_form_dict = imagemap_area.from_dict(imagemap_area_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


