# LotteryAcquisitionConditionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lottery_probability** | **int** | Probability (1-99) of winning the coupon in lottery-type campaigns. | 
**max_acquire_count** | **int** | Maximum number of coupons that can be issued in total. Use -1 to indicate no limit | 

## Example

```python
from linebot.v3.messaging.models.lottery_acquisition_condition_request import LotteryAcquisitionConditionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LotteryAcquisitionConditionRequest from a JSON string
lottery_acquisition_condition_request_instance = LotteryAcquisitionConditionRequest.from_json(json)
# print the JSON string representation of the object
print LotteryAcquisitionConditionRequest.to_json()

# convert the object into a dict
lottery_acquisition_condition_request_dict = lottery_acquisition_condition_request_instance.to_dict()
# create an instance of LotteryAcquisitionConditionRequest from a dict
lottery_acquisition_condition_request_form_dict = lottery_acquisition_condition_request.from_dict(lottery_acquisition_condition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


