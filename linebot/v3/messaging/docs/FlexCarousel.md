# FlexCarousel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contents** | [**List[FlexBubble]**](FlexBubble.md) |  | 

## Example

```python
from linebot.v3.messaging.models.flex_carousel import FlexCarousel

# TODO update the JSON string below
json = "{}"
# create an instance of FlexCarousel from a JSON string
flex_carousel_instance = FlexCarousel.from_json(json)
# print the JSON string representation of the object
print FlexCarousel.to_json()

# convert the object into a dict
flex_carousel_dict = flex_carousel_instance.to_dict()
# create an instance of FlexCarousel from a dict
flex_carousel_form_dict = flex_carousel.from_dict(flex_carousel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


