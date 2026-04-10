# SubscriptionPeriodDemographicFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gte** | [**SubscriptionPeriodDemographic**](SubscriptionPeriodDemographic.md) |  | [optional] 
**lt** | [**SubscriptionPeriodDemographic**](SubscriptionPeriodDemographic.md) |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.subscription_period_demographic_filter import SubscriptionPeriodDemographicFilter

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPeriodDemographicFilter from a JSON string
subscription_period_demographic_filter_instance = SubscriptionPeriodDemographicFilter.from_json(json)
# print the JSON string representation of the object
print SubscriptionPeriodDemographicFilter.to_json()

# convert the object into a dict
subscription_period_demographic_filter_dict = subscription_period_demographic_filter_instance.to_dict()
# create an instance of SubscriptionPeriodDemographicFilter from a dict
subscription_period_demographic_filter_form_dict = subscription_period_demographic_filter.from_dict(subscription_period_demographic_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


