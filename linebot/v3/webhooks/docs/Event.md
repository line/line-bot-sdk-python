# Event

Webhook event

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the event | 
**source** | [**Source**](Source.md) |  | [optional] 
**timestamp** | **int** | Time of the event in milliseconds. | 
**mode** | [**EventMode**](EventMode.md) |  | 
**webhook_event_id** | **str** | Webhook Event ID. An ID that uniquely identifies a webhook event. This is a string in ULID format. | 
**delivery_context** | [**DeliveryContext**](DeliveryContext.md) |  | 

## Example

```python
from linebot.v3.webhooks.models.event import Event

# TODO update the JSON string below
json = "{}"
# create an instance of Event from a JSON string
event_instance = Event.from_json(json)
# print the JSON string representation of the object
print Event.to_json()

# convert the object into a dict
event_dict = event_instance.to_dict()
# create an instance of Event from a dict
event_form_dict = event.from_dict(event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


