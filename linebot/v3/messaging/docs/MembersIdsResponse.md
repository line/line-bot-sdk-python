# MembersIdsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_ids** | **List[str]** | List of user IDs of members in the group chat. Only users of LINE for iOS and LINE for Android are included in &#x60;memberIds&#x60;. | 
**next** | **str** | A continuation token to get the next array of user IDs of the members in the group chat. Returned only when there are remaining user IDs that were not returned in &#x60;memberIds&#x60; in the original request.  | [optional] 

## Example

```python
from linebot.v3.messaging.models.members_ids_response import MembersIdsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MembersIdsResponse from a JSON string
members_ids_response_instance = MembersIdsResponse.from_json(json)
# print the JSON string representation of the object
print MembersIdsResponse.to_json()

# convert the object into a dict
members_ids_response_dict = members_ids_response_instance.to_dict()
# create an instance of MembersIdsResponse from a dict
members_ids_response_form_dict = members_ids_response.from_dict(members_ids_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


