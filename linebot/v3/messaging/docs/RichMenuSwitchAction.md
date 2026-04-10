# RichMenuSwitchAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | [optional] 
**rich_menu_alias_id** | **str** |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.rich_menu_switch_action import RichMenuSwitchAction

# TODO update the JSON string below
json = "{}"
# create an instance of RichMenuSwitchAction from a JSON string
rich_menu_switch_action_instance = RichMenuSwitchAction.from_json(json)
# print the JSON string representation of the object
print RichMenuSwitchAction.to_json()

# convert the object into a dict
rich_menu_switch_action_dict = rich_menu_switch_action_instance.to_dict()
# create an instance of RichMenuSwitchAction from a dict
rich_menu_switch_action_form_dict = rich_menu_switch_action.from_dict(rich_menu_switch_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


