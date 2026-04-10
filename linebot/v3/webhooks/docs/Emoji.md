# Emoji


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Index position for a character in text, with the first character being at position 0. | 
**length** | **int** | The length of the LINE emoji string. For LINE emoji (hello), 7 is the length. | 
**product_id** | **str** | Product ID for a LINE emoji set. | 
**emoji_id** | **str** | ID for a LINE emoji inside a set. | 

## Example

```python
from linebot.v3.webhooks.models.emoji import Emoji

# TODO update the JSON string below
json = "{}"
# create an instance of Emoji from a JSON string
emoji_instance = Emoji.from_json(json)
# print the JSON string representation of the object
print Emoji.to_json()

# convert the object into a dict
emoji_dict = emoji_instance.to_dict()
# create an instance of Emoji from a dict
emoji_form_dict = emoji.from_dict(emoji_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


