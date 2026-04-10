# CarouselTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | [**List[CarouselColumn]**](CarouselColumn.md) |  | 
**image_aspect_ratio** | **str** |  | [optional] 
**image_size** | **str** |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.carousel_template import CarouselTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of CarouselTemplate from a JSON string
carousel_template_instance = CarouselTemplate.from_json(json)
# print the JSON string representation of the object
print CarouselTemplate.to_json()

# convert the object into a dict
carousel_template_dict = carousel_template_instance.to_dict()
# create an instance of CarouselTemplate from a dict
carousel_template_form_dict = carousel_template.from_dict(carousel_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


