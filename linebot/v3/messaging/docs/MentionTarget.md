# MentionTarget


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Target to be mentioned | 

## Example

```python
from linebot.v3.messaging.models.mention_target import MentionTarget

# TODO update the JSON string below
json = "{}"
# create an instance of MentionTarget from a JSON string
mention_target_instance = MentionTarget.from_json(json)
# print the JSON string representation of the object
print MentionTarget.to_json()

# convert the object into a dict
mention_target_dict = mention_target_instance.to_dict()
# create an instance of MentionTarget from a dict
mention_target_form_dict = mention_target.from_dict(mention_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


