# RedeliveryRecipient


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.redelivery_recipient import RedeliveryRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of RedeliveryRecipient from a JSON string
redelivery_recipient_instance = RedeliveryRecipient.from_json(json)
# print the JSON string representation of the object
print RedeliveryRecipient.to_json()

# convert the object into a dict
redelivery_recipient_dict = redelivery_recipient_instance.to_dict()
# create an instance of RedeliveryRecipient from a dict
redelivery_recipient_form_dict = redelivery_recipient.from_dict(redelivery_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


