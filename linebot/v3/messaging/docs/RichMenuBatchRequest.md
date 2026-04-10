# RichMenuBatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operations** | [**List[RichMenuBatchOperation]**](RichMenuBatchOperation.md) | Array of Rich menu operation object... | 
**resume_request_key** | **str** | Key for retry. Key value is a string matching the regular expression pattern | [optional] 

## Example

```python
from linebot.v3.messaging.models.rich_menu_batch_request import RichMenuBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RichMenuBatchRequest from a JSON string
rich_menu_batch_request_instance = RichMenuBatchRequest.from_json(json)
# print the JSON string representation of the object
print RichMenuBatchRequest.to_json()

# convert the object into a dict
rich_menu_batch_request_dict = rich_menu_batch_request_instance.to_dict()
# create an instance of RichMenuBatchRequest from a dict
rich_menu_batch_request_form_dict = rich_menu_batch_request.from_dict(rich_menu_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


