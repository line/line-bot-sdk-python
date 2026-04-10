# AcquisitionConditionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Determines how the coupon is distributed or used. | 

## Example

```python
from linebot.v3.messaging.models.acquisition_condition_request import AcquisitionConditionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AcquisitionConditionRequest from a JSON string
acquisition_condition_request_instance = AcquisitionConditionRequest.from_json(json)
# print the JSON string representation of the object
print AcquisitionConditionRequest.to_json()

# convert the object into a dict
acquisition_condition_request_dict = acquisition_condition_request_instance.to_dict()
# create an instance of AcquisitionConditionRequest from a dict
acquisition_condition_request_form_dict = acquisition_condition_request.from_dict(acquisition_condition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


