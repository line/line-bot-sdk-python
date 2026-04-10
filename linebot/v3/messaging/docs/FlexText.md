# FlexText


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flex** | **int** |  | [optional] 
**text** | **str** |  | [optional] 
**size** | **str** |  | [optional] 
**align** | **str** |  | [optional] 
**gravity** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**weight** | **str** |  | [optional] 
**style** | **str** |  | [optional] 
**decoration** | **str** |  | [optional] 
**wrap** | **bool** |  | [optional] 
**line_spacing** | **str** |  | [optional] 
**margin** | **str** |  | [optional] 
**position** | **str** |  | [optional] 
**offset_top** | **str** |  | [optional] 
**offset_bottom** | **str** |  | [optional] 
**offset_start** | **str** |  | [optional] 
**offset_end** | **str** |  | [optional] 
**action** | [**Action**](Action.md) |  | [optional] 
**max_lines** | **int** |  | [optional] 
**contents** | [**List[FlexSpan]**](FlexSpan.md) |  | [optional] 
**adjust_mode** | **str** |  | [optional] 
**scaling** | **bool** |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.flex_text import FlexText

# TODO update the JSON string below
json = "{}"
# create an instance of FlexText from a JSON string
flex_text_instance = FlexText.from_json(json)
# print the JSON string representation of the object
print FlexText.to_json()

# convert the object into a dict
flex_text_dict = flex_text_instance.to_dict()
# create an instance of FlexText from a dict
flex_text_form_dict = flex_text.from_dict(flex_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


