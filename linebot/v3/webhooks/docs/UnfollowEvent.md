# UnfollowEvent

Event object for when your LINE Official Account is blocked.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from linebot.v3.webhooks.models.unfollow_event import UnfollowEvent

# TODO update the JSON string below
json = "{}"
# create an instance of UnfollowEvent from a JSON string
unfollow_event_instance = UnfollowEvent.from_json(json)
# print the JSON string representation of the object
print UnfollowEvent.to_json()

# convert the object into a dict
unfollow_event_dict = unfollow_event_instance.to_dict()
# create an instance of UnfollowEvent from a dict
unfollow_event_form_dict = unfollow_event.from_dict(unfollow_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


