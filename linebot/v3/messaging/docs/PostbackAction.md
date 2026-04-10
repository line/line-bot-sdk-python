# PostbackAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | [optional] 
**display_text** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**input_option** | **str** |  | [optional] 
**fill_in_text** | **str** |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.postback_action import PostbackAction

# TODO update the JSON string below
json = "{}"
# create an instance of PostbackAction from a JSON string
postback_action_instance = PostbackAction.from_json(json)
# print the JSON string representation of the object
print PostbackAction.to_json()

# convert the object into a dict
postback_action_dict = postback_action_instance.to_dict()
# create an instance of PostbackAction from a dict
postback_action_form_dict = postback_action.from_dict(postback_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


