# RichMenuBatchUnlinkOperation

Unlink the rich menu for all users linked to the rich menu specified in the `from` property.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** |  | 

## Example

```python
from linebot.v3.messaging.models.rich_menu_batch_unlink_operation import RichMenuBatchUnlinkOperation

# TODO update the JSON string below
json = "{}"
# create an instance of RichMenuBatchUnlinkOperation from a JSON string
rich_menu_batch_unlink_operation_instance = RichMenuBatchUnlinkOperation.from_json(json)
# print the JSON string representation of the object
print RichMenuBatchUnlinkOperation.to_json()

# convert the object into a dict
rich_menu_batch_unlink_operation_dict = rich_menu_batch_unlink_operation_instance.to_dict()
# create an instance of RichMenuBatchUnlinkOperation from a dict
rich_menu_batch_unlink_operation_form_dict = rich_menu_batch_unlink_operation.from_dict(rich_menu_batch_unlink_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


