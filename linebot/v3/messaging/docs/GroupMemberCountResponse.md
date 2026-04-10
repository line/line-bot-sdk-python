# GroupMemberCountResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The count of members in the group chat. The number returned excludes the LINE Official Account. | 

## Example

```python
from linebot.v3.messaging.models.group_member_count_response import GroupMemberCountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMemberCountResponse from a JSON string
group_member_count_response_instance = GroupMemberCountResponse.from_json(json)
# print the JSON string representation of the object
print GroupMemberCountResponse.to_json()

# convert the object into a dict
group_member_count_response_dict = group_member_count_response_instance.to_dict()
# create an instance of GroupMemberCountResponse from a dict
group_member_count_response_form_dict = group_member_count_response.from_dict(group_member_count_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


