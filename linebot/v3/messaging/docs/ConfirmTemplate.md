# ConfirmTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**actions** | [**List[Action]**](Action.md) |  | 

## Example

```python
from linebot.v3.messaging.models.confirm_template import ConfirmTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmTemplate from a JSON string
confirm_template_instance = ConfirmTemplate.from_json(json)
# print the JSON string representation of the object
print ConfirmTemplate.to_json()

# convert the object into a dict
confirm_template_dict = confirm_template_instance.to_dict()
# create an instance of ConfirmTemplate from a dict
confirm_template_form_dict = confirm_template.from_dict(confirm_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


