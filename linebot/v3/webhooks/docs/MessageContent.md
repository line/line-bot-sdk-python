# MessageContent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type | 
**id** | **str** | Message ID | 

## Example

```python
from linebot.v3.webhooks.models.message_content import MessageContent

# TODO update the JSON string below
json = "{}"
# create an instance of MessageContent from a JSON string
message_content_instance = MessageContent.from_json(json)
# print the JSON string representation of the object
print MessageContent.to_json()

# convert the object into a dict
message_content_dict = message_content_instance.to_dict()
# create an instance of MessageContent from a dict
message_content_form_dict = message_content.from_dict(message_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


