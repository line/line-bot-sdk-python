# ImagemapAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**area** | [**ImagemapArea**](ImagemapArea.md) |  | 

## Example

```python
from linebot.v3.messaging.models.imagemap_action import ImagemapAction

# TODO update the JSON string below
json = "{}"
# create an instance of ImagemapAction from a JSON string
imagemap_action_instance = ImagemapAction.from_json(json)
# print the JSON string representation of the object
print ImagemapAction.to_json()

# convert the object into a dict
imagemap_action_dict = imagemap_action_instance.to_dict()
# create an instance of ImagemapAction from a dict
imagemap_action_form_dict = imagemap_action.from_dict(imagemap_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


