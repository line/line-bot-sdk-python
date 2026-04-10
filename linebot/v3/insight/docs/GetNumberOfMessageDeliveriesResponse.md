# GetNumberOfMessageDeliveriesResponse

Get number of message deliveries

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status of the counting process. | [optional] 
**broadcast** | **int** | Number of messages sent to all of this LINE Official Account&#39;s friends (broadcast messages). | [optional] 
**targeting** | **int** | Number of messages sent to some of this LINE Official Account&#39;s friends, based on specific attributes (targeted messages). | [optional] 
**auto_response** | **int** | Number of auto-response messages sent. | [optional] 
**welcome_response** | **int** | Number of greeting messages sent. | [optional] 
**chat** | **int** | Number of messages sent from LINE Official Account Manager [Chat screen](https://www.linebiz.com/jp/manual/OfficialAccountManager/chats/) (only available in Japanese). | [optional] 
**api_broadcast** | **int** | Number of broadcast messages sent with the &#x60;Send broadcast message&#x60; Messaging API operation. | [optional] 
**api_push** | **int** | Number of push messages sent with the &#x60;Send push message&#x60; Messaging API operation. | [optional] 
**api_multicast** | **int** | Number of multicast messages sent with the &#x60;Send multicast message&#x60; Messaging API operation. | [optional] 
**api_narrowcast** | **int** | Number of narrowcast messages sent with the &#x60;Send narrowcast message&#x60; Messaging API operation. | [optional] 
**api_reply** | **int** | Number of replies sent with the &#x60;Send reply message&#x60; Messaging API operation. | [optional] 

## Example

```python
from linebot.v3.insight.models.get_number_of_message_deliveries_response import GetNumberOfMessageDeliveriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetNumberOfMessageDeliveriesResponse from a JSON string
get_number_of_message_deliveries_response_instance = GetNumberOfMessageDeliveriesResponse.from_json(json)
# print the JSON string representation of the object
print GetNumberOfMessageDeliveriesResponse.to_json()

# convert the object into a dict
get_number_of_message_deliveries_response_dict = get_number_of_message_deliveries_response_instance.to_dict()
# create an instance of GetNumberOfMessageDeliveriesResponse from a dict
get_number_of_message_deliveries_response_form_dict = get_number_of_message_deliveries_response.from_dict(get_number_of_message_deliveries_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


