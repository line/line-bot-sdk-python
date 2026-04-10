# AccountLinkEvent

Event object for when a user has linked their LINE account with a provider's service account. You can reply to account link events.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reply_token** | **str** | Reply token used to send reply message to this event. This property won&#39;t be included if linking the account has failed. | [optional] 
**link** | [**LinkContent**](LinkContent.md) |  | 

## Example

```python
from linebot.v3.webhooks.models.account_link_event import AccountLinkEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AccountLinkEvent from a JSON string
account_link_event_instance = AccountLinkEvent.from_json(json)
# print the JSON string representation of the object
print AccountLinkEvent.to_json()

# convert the object into a dict
account_link_event_dict = account_link_event_instance.to_dict()
# create an instance of AccountLinkEvent from a dict
account_link_event_form_dict = account_link_event.from_dict(account_link_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


