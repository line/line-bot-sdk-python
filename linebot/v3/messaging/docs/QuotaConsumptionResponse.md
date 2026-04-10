# QuotaConsumptionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_usage** | **int** | The number of sent messages in the current month | 

## Example

```python
from linebot.v3.messaging.models.quota_consumption_response import QuotaConsumptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaConsumptionResponse from a JSON string
quota_consumption_response_instance = QuotaConsumptionResponse.from_json(json)
# print the JSON string representation of the object
print QuotaConsumptionResponse.to_json()

# convert the object into a dict
quota_consumption_response_dict = quota_consumption_response_instance.to_dict()
# create an instance of QuotaConsumptionResponse from a dict
quota_consumption_response_form_dict = quota_consumption_response.from_dict(quota_consumption_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


