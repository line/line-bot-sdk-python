# RichMenuBatchOperation

Rich menu operation object represents the batch operation to the rich menu linked to the user.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of operation to the rich menu linked to the user. One of link, unlink, or unlinkAll. | 

## Example

```python
from linebot.v3.messaging.models.rich_menu_batch_operation import RichMenuBatchOperation

# TODO update the JSON string below
json = "{}"
# create an instance of RichMenuBatchOperation from a JSON string
rich_menu_batch_operation_instance = RichMenuBatchOperation.from_json(json)
# print the JSON string representation of the object
print RichMenuBatchOperation.to_json()

# convert the object into a dict
rich_menu_batch_operation_dict = rich_menu_batch_operation_instance.to_dict()
# create an instance of RichMenuBatchOperation from a dict
rich_menu_batch_operation_form_dict = rich_menu_batch_operation.from_dict(rich_menu_batch_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


