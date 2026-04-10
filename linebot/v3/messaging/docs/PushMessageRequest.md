# PushMessageRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** | ID of the receiver. | 
**messages** | [**List[Message]**](Message.md) | List of Message objects. | 
**notification_disabled** | **bool** | &#x60;true&#x60;: The user doesn’t receive a push notification when a message is sent. &#x60;false&#x60;: The user receives a push notification when the message is sent (unless they have disabled push notifications in LINE and/or their device). The default value is false.  | [optional] [default to False]
**custom_aggregation_units** | **List[str]** | List of aggregation unit name. Case-sensitive. This functions can only be used by corporate users who have submitted the required applications.  | [optional] 

## Example

```python
from linebot.v3.messaging.models.push_message_request import PushMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PushMessageRequest from a JSON string
push_message_request_instance = PushMessageRequest.from_json(json)
# print the JSON string representation of the object
print PushMessageRequest.to_json()

# convert the object into a dict
push_message_request_dict = push_message_request_instance.to_dict()
# create an instance of PushMessageRequest from a dict
push_message_request_form_dict = push_message_request.from_dict(push_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


