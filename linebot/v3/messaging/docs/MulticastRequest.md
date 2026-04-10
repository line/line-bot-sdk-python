# MulticastRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[Message]**](Message.md) | Messages to send | 
**to** | **List[str]** | Array of user IDs. Use userId values which are returned in webhook event objects. Do not use LINE IDs found on LINE. | 
**notification_disabled** | **bool** | &#x60;true&#x60;: The user doesn’t receive a push notification when a message is sent. &#x60;false&#x60;: The user receives a push notification when the message is sent (unless they have disabled push notifications in LINE and/or their device). The default value is false.  | [optional] [default to False]
**custom_aggregation_units** | **List[str]** | Name of aggregation unit. Case-sensitive. | [optional] 

## Example

```python
from linebot.v3.messaging.models.multicast_request import MulticastRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MulticastRequest from a JSON string
multicast_request_instance = MulticastRequest.from_json(json)
# print the JSON string representation of the object
print MulticastRequest.to_json()

# convert the object into a dict
multicast_request_dict = multicast_request_instance.to_dict()
# create an instance of MulticastRequest from a dict
multicast_request_form_dict = multicast_request.from_dict(multicast_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


