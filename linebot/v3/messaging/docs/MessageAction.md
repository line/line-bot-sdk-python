# MessageAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.message_action import MessageAction

# TODO update the JSON string below
json = "{}"
# create an instance of MessageAction from a JSON string
message_action_instance = MessageAction.from_json(json)
# print the JSON string representation of the object
print MessageAction.to_json()

# convert the object into a dict
message_action_dict = message_action_instance.to_dict()
# create an instance of MessageAction from a dict
message_action_form_dict = message_action.from_dict(message_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


