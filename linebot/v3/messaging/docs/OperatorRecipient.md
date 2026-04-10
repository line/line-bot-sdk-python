# OperatorRecipient


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[Recipient]**](Recipient.md) | Create a new recipient object by taking the logical conjunction (AND) of the specified array of recipient objects.  | [optional] 
**var_or** | [**List[Recipient]**](Recipient.md) | Create a new recipient object by taking the logical disjunction (OR) of the specified array of recipient objects.  | [optional] 
**var_not** | [**Recipient**](Recipient.md) |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.operator_recipient import OperatorRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of OperatorRecipient from a JSON string
operator_recipient_instance = OperatorRecipient.from_json(json)
# print the JSON string representation of the object
print OperatorRecipient.to_json()

# convert the object into a dict
operator_recipient_dict = operator_recipient_instance.to_dict()
# create an instance of OperatorRecipient from a dict
operator_recipient_form_dict = operator_recipient.from_dict(operator_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


