# SubscriptionPeriodTile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_period** | **str** | Subscription period. Possible values: &#x60;within7days&#x60;, &#x60;within90days&#x60;, &#x60;unknown&#x60; etc. | [optional] 
**percentage** | **float** | Percentage. Possible values: [0.0,100.0] e.g. 0, 2.9, 37.6. | [optional] 

## Example

```python
from linebot.v3.insight.models.subscription_period_tile import SubscriptionPeriodTile

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPeriodTile from a JSON string
subscription_period_tile_instance = SubscriptionPeriodTile.from_json(json)
# print the JSON string representation of the object
print SubscriptionPeriodTile.to_json()

# convert the object into a dict
subscription_period_tile_dict = subscription_period_tile_instance.to_dict()
# create an instance of SubscriptionPeriodTile from a dict
subscription_period_tile_form_dict = subscription_period_tile.from_dict(subscription_period_tile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


