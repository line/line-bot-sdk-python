# UnsendEvent

Event object for when the user unsends a message.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unsend** | [**UnsendDetail**](UnsendDetail.md) |  | 

## Example

```python
from linebot.v3.webhooks.models.unsend_event import UnsendEvent

# TODO update the JSON string below
json = "{}"
# create an instance of UnsendEvent from a JSON string
unsend_event_instance = UnsendEvent.from_json(json)
# print the JSON string representation of the object
print UnsendEvent.to_json()

# convert the object into a dict
unsend_event_dict = unsend_event_instance.to_dict()
# create an instance of UnsendEvent from a dict
unsend_event_form_dict = unsend_event.from_dict(unsend_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


