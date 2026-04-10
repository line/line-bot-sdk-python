# ImagemapExternalLink


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_uri** | **str** |  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.imagemap_external_link import ImagemapExternalLink

# TODO update the JSON string below
json = "{}"
# create an instance of ImagemapExternalLink from a JSON string
imagemap_external_link_instance = ImagemapExternalLink.from_json(json)
# print the JSON string representation of the object
print ImagemapExternalLink.to_json()

# convert the object into a dict
imagemap_external_link_dict = imagemap_external_link_instance.to_dict()
# create an instance of ImagemapExternalLink from a dict
imagemap_external_link_form_dict = imagemap_external_link.from_dict(imagemap_external_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


