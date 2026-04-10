# Mentionee


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Mentioned target. | 
**index** | **int** | Index position of the user mention for a character in text, with the first character being at position 0. | 
**length** | **int** | The length of the text of the mentioned user. For a mention @example, 8 is the length. | 

## Example

```python
from linebot.v3.webhooks.models.mentionee import Mentionee

# TODO update the JSON string below
json = "{}"
# create an instance of Mentionee from a JSON string
mentionee_instance = Mentionee.from_json(json)
# print the JSON string representation of the object
print Mentionee.to_json()

# convert the object into a dict
mentionee_dict = mentionee_instance.to_dict()
# create an instance of Mentionee from a dict
mentionee_form_dict = mentionee.from_dict(mentionee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


