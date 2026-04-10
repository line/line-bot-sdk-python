# NarrowcastRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[Message]**](Message.md) | List of Message objects. | 
**recipient** | [**Recipient**](Recipient.md) |  | [optional] 
**filter** | [**Filter**](Filter.md) |  | [optional] 
**limit** | [**Limit**](Limit.md) |  | [optional] 
**notification_disabled** | **bool** | &#x60;true&#x60;: The user doesn’t receive a push notification when a message is sent. &#x60;false&#x60;: The user receives a push notification when the message is sent (unless they have disabled push notifications in LINE and/or their device). The default value is false.  | [optional] [default to False]

## Example

```python
from linebot.v3.messaging.models.narrowcast_request import NarrowcastRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NarrowcastRequest from a JSON string
narrowcast_request_instance = NarrowcastRequest.from_json(json)
# print the JSON string representation of the object
print NarrowcastRequest.to_json()

# convert the object into a dict
narrowcast_request_dict = narrowcast_request_instance.to_dict()
# create an instance of NarrowcastRequest from a dict
narrowcast_request_form_dict = narrowcast_request.from_dict(narrowcast_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


