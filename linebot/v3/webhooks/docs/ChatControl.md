# ChatControl


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expire_at** | **int** |  | 

## Example

```python
from linebot.v3.webhooks.models.chat_control import ChatControl

# TODO update the JSON string below
json = "{}"
# create an instance of ChatControl from a JSON string
chat_control_instance = ChatControl.from_json(json)
# print the JSON string representation of the object
print ChatControl.to_json()

# convert the object into a dict
chat_control_dict = chat_control_instance.to_dict()
# create an instance of ChatControl from a dict
chat_control_form_dict = chat_control.from_dict(chat_control_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


