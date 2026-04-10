# Limit

Limit of the Narrowcast

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max** | **int** | The maximum number of narrowcast messages to send. Use this parameter to limit the number of narrowcast messages sent. The recipients will be chosen at random.  | [optional] 
**up_to_remaining_quota** | **bool** | If true, the message will be sent within the maximum number of deliverable messages. The default value is &#x60;false&#x60;.  Targets will be selected at random.  | [optional] [default to False]
**forbid_partial_delivery** | **bool** | This option prevents messages from being delivered to only a subset of the target audience. If true, the narrowcast request success but fails asynchronously. You can check whether message delivery was canceled by retrieving the narrowcast message progress.  This property can be set to true only if upToRemainingQuota is set to true.  | [optional] [default to False]

## Example

```python
from linebot.v3.messaging.models.limit import Limit

# TODO update the JSON string below
json = "{}"
# create an instance of Limit from a JSON string
limit_instance = Limit.from_json(json)
# print the JSON string representation of the object
print Limit.to_json()

# convert the object into a dict
limit_dict = limit_instance.to_dict()
# create an instance of Limit from a dict
limit_form_dict = limit.from_dict(limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


