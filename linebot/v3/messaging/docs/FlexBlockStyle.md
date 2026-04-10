# FlexBlockStyle


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background_color** | **str** |  | [optional] 
**separator** | **bool** |  | [optional] 
**separator_color** | **str** |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.flex_block_style import FlexBlockStyle

# TODO update the JSON string below
json = "{}"
# create an instance of FlexBlockStyle from a JSON string
flex_block_style_instance = FlexBlockStyle.from_json(json)
# print the JSON string representation of the object
print FlexBlockStyle.to_json()

# convert the object into a dict
flex_block_style_dict = flex_block_style_instance.to_dict()
# create an instance of FlexBlockStyle from a dict
flex_block_style_form_dict = flex_block_style.from_dict(flex_block_style_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


