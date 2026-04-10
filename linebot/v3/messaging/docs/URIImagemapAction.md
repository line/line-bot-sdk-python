# URIImagemapAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_uri** | **str** |  | 
**label** | **str** |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.uri_imagemap_action import URIImagemapAction

# TODO update the JSON string below
json = "{}"
# create an instance of URIImagemapAction from a JSON string
uri_imagemap_action_instance = URIImagemapAction.from_json(json)
# print the JSON string representation of the object
print URIImagemapAction.to_json()

# convert the object into a dict
uri_imagemap_action_dict = uri_imagemap_action_instance.to_dict()
# create an instance of URIImagemapAction from a dict
uri_imagemap_action_form_dict = uri_imagemap_action.from_dict(uri_imagemap_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


