# GetJoinedMembershipUsersResponse

List of users who have joined the membership

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[str]** | A list of user IDs who joined the membership. Users who have not agreed to the bot user agreement, are not following the bot, or are not active will be excluded. If there are no users in the membership, an empty list will be returned.  | 
**next** | **str** | A continuation token to get next remaining membership user IDs. Returned only when there are remaining user IDs that weren&#39;t returned in the userIds property in the previous request. The continuation token expires in 24 hours (86,400 seconds).   | [optional] 

## Example

```python
from linebot.v3.messaging.models.get_joined_membership_users_response import GetJoinedMembershipUsersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetJoinedMembershipUsersResponse from a JSON string
get_joined_membership_users_response_instance = GetJoinedMembershipUsersResponse.from_json(json)
# print the JSON string representation of the object
print GetJoinedMembershipUsersResponse.to_json()

# convert the object into a dict
get_joined_membership_users_response_dict = get_joined_membership_users_response_instance.to_dict()
# create an instance of GetJoinedMembershipUsersResponse from a dict
get_joined_membership_users_response_form_dict = get_joined_membership_users_response.from_dict(get_joined_membership_users_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


