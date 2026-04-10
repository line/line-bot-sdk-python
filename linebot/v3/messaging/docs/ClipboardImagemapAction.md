# ClipboardImagemapAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clipboard_text** | **str** | Text that is copied to the clipboard. Max character limit: 1000  | 
**label** | **str** |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.clipboard_imagemap_action import ClipboardImagemapAction

# TODO update the JSON string below
json = "{}"
# create an instance of ClipboardImagemapAction from a JSON string
clipboard_imagemap_action_instance = ClipboardImagemapAction.from_json(json)
# print the JSON string representation of the object
print ClipboardImagemapAction.to_json()

# convert the object into a dict
clipboard_imagemap_action_dict = clipboard_imagemap_action_instance.to_dict()
# create an instance of ClipboardImagemapAction from a dict
clipboard_imagemap_action_form_dict = clipboard_imagemap_action.from_dict(clipboard_imagemap_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


