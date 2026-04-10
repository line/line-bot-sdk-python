# FlexBoxLinearGradient


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**angle** | **str** |  | [optional] 
**start_color** | **str** |  | [optional] 
**end_color** | **str** |  | [optional] 
**center_color** | **str** |  | [optional] 
**center_position** | **str** |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.flex_box_linear_gradient import FlexBoxLinearGradient

# TODO update the JSON string below
json = "{}"
# create an instance of FlexBoxLinearGradient from a JSON string
flex_box_linear_gradient_instance = FlexBoxLinearGradient.from_json(json)
# print the JSON string representation of the object
print FlexBoxLinearGradient.to_json()

# convert the object into a dict
flex_box_linear_gradient_dict = flex_box_linear_gradient_instance.to_dict()
# create an instance of FlexBoxLinearGradient from a dict
flex_box_linear_gradient_form_dict = flex_box_linear_gradient.from_dict(flex_box_linear_gradient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


