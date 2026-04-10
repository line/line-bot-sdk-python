# LotteryAcquisitionConditionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lottery_probability** | **int** |  | [optional] 
**max_acquire_count** | **int** |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.lottery_acquisition_condition_response import LotteryAcquisitionConditionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LotteryAcquisitionConditionResponse from a JSON string
lottery_acquisition_condition_response_instance = LotteryAcquisitionConditionResponse.from_json(json)
# print the JSON string representation of the object
print LotteryAcquisitionConditionResponse.to_json()

# convert the object into a dict
lottery_acquisition_condition_response_dict = lottery_acquisition_condition_response_instance.to_dict()
# create an instance of LotteryAcquisitionConditionResponse from a dict
lottery_acquisition_condition_response_form_dict = lottery_acquisition_condition_response.from_dict(lottery_acquisition_condition_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


