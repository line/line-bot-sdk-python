# RichMenuBatchLinkOperation

Replace the rich menu with the rich menu specified in the `to` property for all users linked to the rich menu specified in the `from` property.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** |  | 
**to** | **str** |  | 

## Example

```python
from linebot.v3.messaging.models.rich_menu_batch_link_operation import RichMenuBatchLinkOperation

# TODO update the JSON string below
json = "{}"
# create an instance of RichMenuBatchLinkOperation from a JSON string
rich_menu_batch_link_operation_instance = RichMenuBatchLinkOperation.from_json(json)
# print the JSON string representation of the object
print RichMenuBatchLinkOperation.to_json()

# convert the object into a dict
rich_menu_batch_link_operation_dict = rich_menu_batch_link_operation_instance.to_dict()
# create an instance of RichMenuBatchLinkOperation from a dict
rich_menu_batch_link_operation_form_dict = rich_menu_batch_link_operation.from_dict(rich_menu_batch_link_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


