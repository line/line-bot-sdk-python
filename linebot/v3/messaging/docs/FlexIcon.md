# FlexIcon


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**size** | **str** |  | [optional] 
**aspect_ratio** | **str** |  | [optional] 
**margin** | **str** |  | [optional] 
**position** | **str** |  | [optional] 
**offset_top** | **str** |  | [optional] 
**offset_bottom** | **str** |  | [optional] 
**offset_start** | **str** |  | [optional] 
**offset_end** | **str** |  | [optional] 
**scaling** | **bool** |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.flex_icon import FlexIcon

# TODO update the JSON string below
json = "{}"
# create an instance of FlexIcon from a JSON string
flex_icon_instance = FlexIcon.from_json(json)
# print the JSON string representation of the object
print FlexIcon.to_json()

# convert the object into a dict
flex_icon_dict = flex_icon_instance.to_dict()
# create an instance of FlexIcon from a dict
flex_icon_form_dict = flex_icon.from_dict(flex_icon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


