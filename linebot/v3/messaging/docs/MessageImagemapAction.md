# MessageImagemapAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**label** | **str** |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.message_imagemap_action import MessageImagemapAction

# TODO update the JSON string below
json = "{}"
# create an instance of MessageImagemapAction from a JSON string
message_imagemap_action_instance = MessageImagemapAction.from_json(json)
# print the JSON string representation of the object
print MessageImagemapAction.to_json()

# convert the object into a dict
message_imagemap_action_dict = message_imagemap_action_instance.to_dict()
# create an instance of MessageImagemapAction from a dict
message_imagemap_action_form_dict = message_imagemap_action.from_dict(message_imagemap_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


