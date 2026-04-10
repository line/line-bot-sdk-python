# DeactivatedEvent

This event indicates that the module channel has been switched to Standby Channel by calling Acquire Control API or Release Control API. Sent to the webhook URL server of the module channel.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from linebot.v3.webhooks.models.deactivated_event import DeactivatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DeactivatedEvent from a JSON string
deactivated_event_instance = DeactivatedEvent.from_json(json)
# print the JSON string representation of the object
print DeactivatedEvent.to_json()

# convert the object into a dict
deactivated_event_dict = deactivated_event_instance.to_dict()
# create an instance of DeactivatedEvent from a dict
deactivated_event_form_dict = deactivated_event.from_dict(deactivated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


