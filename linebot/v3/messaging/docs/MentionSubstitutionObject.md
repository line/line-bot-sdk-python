# MentionSubstitutionObject

An object representing a mention substitution.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mentionee** | [**MentionTarget**](MentionTarget.md) |  | 

## Example

```python
from linebot.v3.messaging.models.mention_substitution_object import MentionSubstitutionObject

# TODO update the JSON string below
json = "{}"
# create an instance of MentionSubstitutionObject from a JSON string
mention_substitution_object_instance = MentionSubstitutionObject.from_json(json)
# print the JSON string representation of the object
print MentionSubstitutionObject.to_json()

# convert the object into a dict
mention_substitution_object_dict = mention_substitution_object_instance.to_dict()
# create an instance of MentionSubstitutionObject from a dict
mention_substitution_object_form_dict = mention_substitution_object.from_dict(mention_substitution_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


