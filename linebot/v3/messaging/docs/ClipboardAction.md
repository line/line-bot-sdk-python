# ClipboardAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clipboard_text** | **str** | Text that is copied to the clipboard. Max character limit: 1000  | 

## Example

```python
from linebot.v3.messaging.models.clipboard_action import ClipboardAction

# TODO update the JSON string below
json = "{}"
# create an instance of ClipboardAction from a JSON string
clipboard_action_instance = ClipboardAction.from_json(json)
# print the JSON string representation of the object
print ClipboardAction.to_json()

# convert the object into a dict
clipboard_action_dict = clipboard_action_instance.to_dict()
# create an instance of ClipboardAction from a dict
clipboard_action_form_dict = clipboard_action.from_dict(clipboard_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


