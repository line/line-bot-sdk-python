# ContentProvider

Provider of the media file.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Provider of the image file. | 
**original_content_url** | **str** | URL of the image file. Only included when contentProvider.type is external. | [optional] 
**preview_image_url** | **str** | URL of the preview image. Only included when contentProvider.type is external. | [optional] 

## Example

```python
from linebot.v3.webhooks.models.content_provider import ContentProvider

# TODO update the JSON string below
json = "{}"
# create an instance of ContentProvider from a JSON string
content_provider_instance = ContentProvider.from_json(json)
# print the JSON string representation of the object
print ContentProvider.to_json()

# convert the object into a dict
content_provider_dict = content_provider_instance.to_dict()
# create an instance of ContentProvider from a dict
content_provider_form_dict = content_provider.from_dict(content_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


