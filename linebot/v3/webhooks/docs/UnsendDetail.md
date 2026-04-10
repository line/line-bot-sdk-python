# UnsendDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | The message ID of the unsent message | 

## Example

```python
from linebot.v3.webhooks.models.unsend_detail import UnsendDetail

# TODO update the JSON string below
json = "{}"
# create an instance of UnsendDetail from a JSON string
unsend_detail_instance = UnsendDetail.from_json(json)
# print the JSON string representation of the object
print UnsendDetail.to_json()

# convert the object into a dict
unsend_detail_dict = unsend_detail_instance.to_dict()
# create an instance of UnsendDetail from a dict
unsend_detail_form_dict = unsend_detail.from_dict(unsend_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


