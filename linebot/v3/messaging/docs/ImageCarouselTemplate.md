# ImageCarouselTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | [**List[ImageCarouselColumn]**](ImageCarouselColumn.md) |  | 

## Example

```python
from linebot.v3.messaging.models.image_carousel_template import ImageCarouselTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ImageCarouselTemplate from a JSON string
image_carousel_template_instance = ImageCarouselTemplate.from_json(json)
# print the JSON string representation of the object
print ImageCarouselTemplate.to_json()

# convert the object into a dict
image_carousel_template_dict = image_carousel_template_instance.to_dict()
# create an instance of ImageCarouselTemplate from a dict
image_carousel_template_form_dict = image_carousel_template.from_dict(image_carousel_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


