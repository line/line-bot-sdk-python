# Mention


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mentionees** | [**List[Mentionee]**](Mentionee.md) | Array of one or more mention objects. Max: 20 mentions | 

## Example

```python
from linebot.v3.webhooks.models.mention import Mention

# TODO update the JSON string below
json = "{}"
# create an instance of Mention from a JSON string
mention_instance = Mention.from_json(json)
# print the JSON string representation of the object
print Mention.to_json()

# convert the object into a dict
mention_dict = mention_instance.to_dict()
# create an instance of Mention from a dict
mention_form_dict = mention.from_dict(mention_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


