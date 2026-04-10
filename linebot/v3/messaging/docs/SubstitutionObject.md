# SubstitutionObject

An object that defines the replacement value for a placeholder in the text.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of substitution object | 

## Example

```python
from linebot.v3.messaging.models.substitution_object import SubstitutionObject

# TODO update the JSON string below
json = "{}"
# create an instance of SubstitutionObject from a JSON string
substitution_object_instance = SubstitutionObject.from_json(json)
# print the JSON string representation of the object
print SubstitutionObject.to_json()

# convert the object into a dict
substitution_object_dict = substitution_object_instance.to_dict()
# create an instance of SubstitutionObject from a dict
substitution_object_form_dict = substitution_object.from_dict(substitution_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


