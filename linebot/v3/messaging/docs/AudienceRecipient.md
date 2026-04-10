# AudienceRecipient


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience_group_id** | **int** |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.audience_recipient import AudienceRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of AudienceRecipient from a JSON string
audience_recipient_instance = AudienceRecipient.from_json(json)
# print the JSON string representation of the object
print AudienceRecipient.to_json()

# convert the object into a dict
audience_recipient_dict = audience_recipient_instance.to_dict()
# create an instance of AudienceRecipient from a dict
audience_recipient_form_dict = audience_recipient.from_dict(audience_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


