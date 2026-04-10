# RichMenuBulkUnlinkRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[str]** | Array of user IDs. Found in the &#x60;source&#x60; object of webhook event objects. Do not use the LINE ID used in LINE. | 

## Example

```python
from linebot.v3.messaging.models.rich_menu_bulk_unlink_request import RichMenuBulkUnlinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RichMenuBulkUnlinkRequest from a JSON string
rich_menu_bulk_unlink_request_instance = RichMenuBulkUnlinkRequest.from_json(json)
# print the JSON string representation of the object
print RichMenuBulkUnlinkRequest.to_json()

# convert the object into a dict
rich_menu_bulk_unlink_request_dict = rich_menu_bulk_unlink_request_instance.to_dict()
# create an instance of RichMenuBulkUnlinkRequest from a dict
rich_menu_bulk_unlink_request_form_dict = rich_menu_bulk_unlink_request.from_dict(rich_menu_bulk_unlink_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


