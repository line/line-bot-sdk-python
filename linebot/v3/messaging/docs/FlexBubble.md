# FlexBubble


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** |  | [optional] 
**styles** | [**FlexBubbleStyles**](FlexBubbleStyles.md) |  | [optional] 
**header** | [**FlexBox**](FlexBox.md) |  | [optional] 
**hero** | [**FlexComponent**](FlexComponent.md) |  | [optional] 
**body** | [**FlexBox**](FlexBox.md) |  | [optional] 
**footer** | [**FlexBox**](FlexBox.md) |  | [optional] 
**size** | **str** |  | [optional] 
**action** | [**Action**](Action.md) |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.flex_bubble import FlexBubble

# TODO update the JSON string below
json = "{}"
# create an instance of FlexBubble from a JSON string
flex_bubble_instance = FlexBubble.from_json(json)
# print the JSON string representation of the object
print FlexBubble.to_json()

# convert the object into a dict
flex_bubble_dict = flex_bubble_instance.to_dict()
# create an instance of FlexBubble from a dict
flex_bubble_form_dict = flex_bubble.from_dict(flex_bubble_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


