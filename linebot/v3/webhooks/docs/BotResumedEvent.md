# BotResumedEvent

This event indicates that the LINE Official Account has returned from the suspended state. Sent to the webhook URL server of the module channel.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from linebot.v3.webhooks.models.bot_resumed_event import BotResumedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of BotResumedEvent from a JSON string
bot_resumed_event_instance = BotResumedEvent.from_json(json)
# print the JSON string representation of the object
print BotResumedEvent.to_json()

# convert the object into a dict
bot_resumed_event_dict = bot_resumed_event_instance.to_dict()
# create an instance of BotResumedEvent from a dict
bot_resumed_event_form_dict = bot_resumed_event.from_dict(bot_resumed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


