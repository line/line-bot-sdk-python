# FlexBubbleStyles


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | [**FlexBlockStyle**](FlexBlockStyle.md) |  | [optional] 
**hero** | [**FlexBlockStyle**](FlexBlockStyle.md) |  | [optional] 
**body** | [**FlexBlockStyle**](FlexBlockStyle.md) |  | [optional] 
**footer** | [**FlexBlockStyle**](FlexBlockStyle.md) |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.flex_bubble_styles import FlexBubbleStyles

# TODO update the JSON string below
json = "{}"
# create an instance of FlexBubbleStyles from a JSON string
flex_bubble_styles_instance = FlexBubbleStyles.from_json(json)
# print the JSON string representation of the object
print FlexBubbleStyles.to_json()

# convert the object into a dict
flex_bubble_styles_dict = flex_bubble_styles_instance.to_dict()
# create an instance of FlexBubbleStyles from a dict
flex_bubble_styles_form_dict = flex_bubble_styles.from_dict(flex_bubble_styles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


