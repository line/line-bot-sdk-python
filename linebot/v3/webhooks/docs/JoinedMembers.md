# JoinedMembers


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | [**List[UserSource]**](UserSource.md) | Users who joined. Array of source user objects. | 

## Example

```python
from linebot.v3.webhooks.models.joined_members import JoinedMembers

# TODO update the JSON string below
json = "{}"
# create an instance of JoinedMembers from a JSON string
joined_members_instance = JoinedMembers.from_json(json)
# print the JSON string representation of the object
print JoinedMembers.to_json()

# convert the object into a dict
joined_members_dict = joined_members_instance.to_dict()
# create an instance of JoinedMembers from a dict
joined_members_form_dict = joined_members.from_dict(joined_members_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


