# EmojiSubstitutionObject

An object representing a emoji substitution.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** |  | 
**emoji_id** | **str** |  | 

## Example

```python
from linebot.v3.messaging.models.emoji_substitution_object import EmojiSubstitutionObject

# TODO update the JSON string below
json = "{}"
# create an instance of EmojiSubstitutionObject from a JSON string
emoji_substitution_object_instance = EmojiSubstitutionObject.from_json(json)
# print the JSON string representation of the object
print EmojiSubstitutionObject.to_json()

# convert the object into a dict
emoji_substitution_object_dict = emoji_substitution_object_instance.to_dict()
# create an instance of EmojiSubstitutionObject from a dict
emoji_substitution_object_form_dict = emoji_substitution_object.from_dict(emoji_substitution_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


