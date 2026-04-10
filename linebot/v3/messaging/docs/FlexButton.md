# FlexButton


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flex** | **int** |  | [optional] 
**color** | **str** |  | [optional] 
**style** | **str** |  | [optional] 
**action** | [**Action**](Action.md) |  | 
**gravity** | **str** |  | [optional] 
**margin** | **str** |  | [optional] 
**position** | **str** |  | [optional] 
**offset_top** | **str** |  | [optional] 
**offset_bottom** | **str** |  | [optional] 
**offset_start** | **str** |  | [optional] 
**offset_end** | **str** |  | [optional] 
**height** | **str** |  | [optional] 
**adjust_mode** | **str** |  | [optional] 
**scaling** | **bool** |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.flex_button import FlexButton

# TODO update the JSON string below
json = "{}"
# create an instance of FlexButton from a JSON string
flex_button_instance = FlexButton.from_json(json)
# print the JSON string representation of the object
print FlexButton.to_json()

# convert the object into a dict
flex_button_dict = flex_button_instance.to_dict()
# create an instance of FlexButton from a dict
flex_button_form_dict = flex_button.from_dict(flex_button_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


