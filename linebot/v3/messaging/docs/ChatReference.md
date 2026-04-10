# ChatReference

Chat reference

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The target user ID | 

## Example

```python
from linebot.v3.messaging.models.chat_reference import ChatReference

# TODO update the JSON string below
json = "{}"
# create an instance of ChatReference from a JSON string
chat_reference_instance = ChatReference.from_json(json)
# print the JSON string representation of the object
print ChatReference.to_json()

# convert the object into a dict
chat_reference_dict = chat_reference_instance.to_dict()
# create an instance of ChatReference from a dict
chat_reference_form_dict = chat_reference.from_dict(chat_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


