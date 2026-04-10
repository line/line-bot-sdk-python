# Emoji


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | [optional] 
**product_id** | **str** |  | [optional] 
**emoji_id** | **str** |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.emoji import Emoji

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


