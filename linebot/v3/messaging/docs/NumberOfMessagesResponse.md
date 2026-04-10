# NumberOfMessagesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Aggregation process status. One of:  &#x60;ready&#x60;: The number of messages can be obtained. &#x60;unready&#x60;: We haven&#39;t finished calculating the number of sent messages for the specified in date. For example, this property is returned when the delivery date or a future date is specified. Calculation usually takes about a day. &#x60;unavailable_for_privacy&#x60;: The total number of messages on the specified day is less than 20. &#x60;out_of_service&#x60;: The specified date is earlier than the date on which we first started calculating sent messages (March 31, 2018).  | 
**success** | **int** | The number of messages delivered using the phone number on the date specified in &#x60;date&#x60;. The response has this property only when the value of &#x60;status&#x60; is &#x60;ready&#x60;.   | [optional] 

## Example

```python
from linebot.v3.messaging.models.number_of_messages_response import NumberOfMessagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NumberOfMessagesResponse from a JSON string
number_of_messages_response_instance = NumberOfMessagesResponse.from_json(json)
# print the JSON string representation of the object
print NumberOfMessagesResponse.to_json()

# convert the object into a dict
number_of_messages_response_dict = number_of_messages_response_instance.to_dict()
# create an instance of NumberOfMessagesResponse from a dict
number_of_messages_response_form_dict = number_of_messages_response.from_dict(number_of_messages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


