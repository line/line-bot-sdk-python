# RoomUserProfileResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | User&#39;s display name | 
**user_id** | **str** | User ID | 
**picture_url** | **str** | Profile image URL. &#x60;https&#x60; image URL. Not included in the response if the user doesn&#39;t have a profile image. | [optional] 

## Example

```python
from linebot.v3.messaging.models.room_user_profile_response import RoomUserProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoomUserProfileResponse from a JSON string
room_user_profile_response_instance = RoomUserProfileResponse.from_json(json)
# print the JSON string representation of the object
print RoomUserProfileResponse.to_json()

# convert the object into a dict
room_user_profile_response_dict = room_user_profile_response_instance.to_dict()
# create an instance of RoomUserProfileResponse from a dict
room_user_profile_response_form_dict = room_user_profile_response.from_dict(room_user_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


