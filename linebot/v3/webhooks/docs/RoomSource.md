# RoomSource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | ID of the source user. Only included in message events. Only users of LINE for iOS and LINE for Android are included in userId. | [optional] 
**room_id** | **str** | Room ID of the source multi-person chat | 

## Example

```python
from linebot.v3.webhooks.models.room_source import RoomSource

# TODO update the JSON string below
json = "{}"
# create an instance of RoomSource from a JSON string
room_source_instance = RoomSource.from_json(json)
# print the JSON string representation of the object
print RoomSource.to_json()

# convert the object into a dict
room_source_dict = room_source_instance.to_dict()
# create an instance of RoomSource from a dict
room_source_form_dict = room_source.from_dict(room_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


