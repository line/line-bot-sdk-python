# RichMenuBatchUnlinkAllOperation

Unlink the rich menu from all users linked to the rich menu.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from linebot.v3.messaging.models.rich_menu_batch_unlink_all_operation import RichMenuBatchUnlinkAllOperation

# TODO update the JSON string below
json = "{}"
# create an instance of RichMenuBatchUnlinkAllOperation from a JSON string
rich_menu_batch_unlink_all_operation_instance = RichMenuBatchUnlinkAllOperation.from_json(json)
# print the JSON string representation of the object
print RichMenuBatchUnlinkAllOperation.to_json()

# convert the object into a dict
rich_menu_batch_unlink_all_operation_dict = rich_menu_batch_unlink_all_operation_instance.to_dict()
# create an instance of RichMenuBatchUnlinkAllOperation from a dict
rich_menu_batch_unlink_all_operation_form_dict = rich_menu_batch_unlink_all_operation.from_dict(rich_menu_batch_unlink_all_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


