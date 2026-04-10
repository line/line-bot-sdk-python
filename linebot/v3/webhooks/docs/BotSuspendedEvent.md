# BotSuspendedEvent

This event indicates that the LINE Official Account has been suspended (Suspend). Sent to the webhook URL server of the module channel.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from linebot.v3.webhooks.models.bot_suspended_event import BotSuspendedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of BotSuspendedEvent from a JSON string
bot_suspended_event_instance = BotSuspendedEvent.from_json(json)
# print the JSON string representation of the object
print BotSuspendedEvent.to_json()

# convert the object into a dict
bot_suspended_event_dict = bot_suspended_event_instance.to_dict()
# create an instance of BotSuspendedEvent from a dict
bot_suspended_event_form_dict = bot_suspended_event.from_dict(bot_suspended_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


