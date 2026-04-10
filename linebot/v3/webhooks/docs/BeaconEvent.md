# BeaconEvent

Event object for when a user enters the range of a LINE Beacon. You can reply to beacon events.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reply_token** | **str** | Reply token used to send reply message to this event | 
**beacon** | [**BeaconContent**](BeaconContent.md) |  | 

## Example

```python
from linebot.v3.webhooks.models.beacon_event import BeaconEvent

# TODO update the JSON string below
json = "{}"
# create an instance of BeaconEvent from a JSON string
beacon_event_instance = BeaconEvent.from_json(json)
# print the JSON string representation of the object
print BeaconEvent.to_json()

# convert the object into a dict
beacon_event_dict = beacon_event_instance.to_dict()
# create an instance of BeaconEvent from a dict
beacon_event_form_dict = beacon_event.from_dict(beacon_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


