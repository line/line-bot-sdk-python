# PnpMessagesRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[Message]**](Message.md) | Message to be sent. | 
**to** | **str** | Message destination. Specify a phone number that has been normalized to E.164 format and hashed with SHA256. | 
**notification_disabled** | **bool** | &#x60;true&#x60;: The user doesn’t receive a push notification when a message is sent. &#x60;false&#x60;: The user receives a push notification when the message is sent (unless they have disabled push notifications in LINE and/or their device). The default value is false.  | [optional] [default to False]

## Example

```python
from linebot.v3.messaging.models.pnp_messages_request import PnpMessagesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PnpMessagesRequest from a JSON string
pnp_messages_request_instance = PnpMessagesRequest.from_json(json)
# print the JSON string representation of the object
print PnpMessagesRequest.to_json()

# convert the object into a dict
pnp_messages_request_dict = pnp_messages_request_instance.to_dict()
# create an instance of PnpMessagesRequest from a dict
pnp_messages_request_form_dict = pnp_messages_request.from_dict(pnp_messages_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


