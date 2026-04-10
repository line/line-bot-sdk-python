# RoomMemberCountResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The count of members in the multi-person chat. The number returned excludes the LINE Official Account. | 

## Example

```python
from linebot.v3.messaging.models.room_member_count_response import RoomMemberCountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoomMemberCountResponse from a JSON string
room_member_count_response_instance = RoomMemberCountResponse.from_json(json)
# print the JSON string representation of the object
print RoomMemberCountResponse.to_json()

# convert the object into a dict
room_member_count_response_dict = room_member_count_response_instance.to_dict()
# create an instance of RoomMemberCountResponse from a dict
room_member_count_response_form_dict = room_member_count_response.from_dict(room_member_count_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


