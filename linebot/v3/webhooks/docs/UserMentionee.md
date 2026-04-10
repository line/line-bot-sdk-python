# UserMentionee

Mentioned target is user

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | User ID of the mentioned user. Only included if mention.mentions[].type is user and the user consents to the LINE Official Account obtaining their user profile information. | [optional] 
**is_self** | **bool** | Whether the mentioned user is the bot that receives the webhook. | [optional] 

## Example

```python
from linebot.v3.webhooks.models.user_mentionee import UserMentionee

# TODO update the JSON string below
json = "{}"
# create an instance of UserMentionee from a JSON string
user_mentionee_instance = UserMentionee.from_json(json)
# print the JSON string representation of the object
print UserMentionee.to_json()

# convert the object into a dict
user_mentionee_dict = user_mentionee_instance.to_dict()
# create an instance of UserMentionee from a dict
user_mentionee_form_dict = user_mentionee.from_dict(user_mentionee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


