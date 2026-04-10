# TemplateMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alt_text** | **str** |  | 
**template** | [**Template**](Template.md) |  | 

## Example

```python
from linebot.v3.messaging.models.template_message import TemplateMessage

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateMessage from a JSON string
template_message_instance = TemplateMessage.from_json(json)
# print the JSON string representation of the object
print TemplateMessage.to_json()

# convert the object into a dict
template_message_dict = template_message_instance.to_dict()
# create an instance of TemplateMessage from a dict
template_message_form_dict = template_message.from_dict(template_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


