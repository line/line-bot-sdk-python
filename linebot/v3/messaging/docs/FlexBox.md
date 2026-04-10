# FlexBox


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**layout** | **str** |  | 
**flex** | **int** |  | [optional] 
**contents** | [**List[FlexComponent]**](FlexComponent.md) |  | 
**spacing** | **str** |  | [optional] 
**margin** | **str** |  | [optional] 
**position** | **str** |  | [optional] 
**offset_top** | **str** |  | [optional] 
**offset_bottom** | **str** |  | [optional] 
**offset_start** | **str** |  | [optional] 
**offset_end** | **str** |  | [optional] 
**background_color** | **str** |  | [optional] 
**border_color** | **str** |  | [optional] 
**border_width** | **str** |  | [optional] 
**corner_radius** | **str** |  | [optional] 
**width** | **str** |  | [optional] 
**max_width** | **str** |  | [optional] 
**height** | **str** |  | [optional] 
**max_height** | **str** |  | [optional] 
**padding_all** | **str** |  | [optional] 
**padding_top** | **str** |  | [optional] 
**padding_bottom** | **str** |  | [optional] 
**padding_start** | **str** |  | [optional] 
**padding_end** | **str** |  | [optional] 
**action** | [**Action**](Action.md) |  | [optional] 
**justify_content** | **str** |  | [optional] 
**align_items** | **str** |  | [optional] 
**background** | [**FlexBoxBackground**](FlexBoxBackground.md) |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.flex_box import FlexBox

# TODO update the JSON string below
json = "{}"
# create an instance of FlexBox from a JSON string
flex_box_instance = FlexBox.from_json(json)
# print the JSON string representation of the object
print FlexBox.to_json()

# convert the object into a dict
flex_box_dict = flex_box_instance.to_dict()
# create an instance of FlexBox from a dict
flex_box_form_dict = flex_box.from_dict(flex_box_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


