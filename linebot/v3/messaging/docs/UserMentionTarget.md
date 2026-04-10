# UserMentionTarget


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 

## Example

```python
from linebot.v3.messaging.models.user_mention_target import UserMentionTarget

# TODO update the JSON string below
json = "{}"
# create an instance of UserMentionTarget from a JSON string
user_mention_target_instance = UserMentionTarget.from_json(json)
# print the JSON string representation of the object
print UserMentionTarget.to_json()

# convert the object into a dict
user_mention_target_dict = user_mention_target_instance.to_dict()
# create an instance of UserMentionTarget from a dict
user_mention_target_form_dict = user_mention_target.from_dict(user_mention_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


