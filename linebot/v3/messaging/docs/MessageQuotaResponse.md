# MessageQuotaResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**QuotaType**](QuotaType.md) |  | 
**value** | **int** | The target limit for sending messages in the current month. This property is returned when the &#x60;type&#x60; property has a value of &#x60;limited&#x60;.  | [optional] 

## Example

```python
from linebot.v3.messaging.models.message_quota_response import MessageQuotaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessageQuotaResponse from a JSON string
message_quota_response_instance = MessageQuotaResponse.from_json(json)
# print the JSON string representation of the object
print MessageQuotaResponse.to_json()

# convert the object into a dict
message_quota_response_dict = message_quota_response_instance.to_dict()
# create an instance of MessageQuotaResponse from a dict
message_quota_response_form_dict = message_quota_response.from_dict(message_quota_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


