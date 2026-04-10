# RichMenuBatchProgressResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase** | [**RichMenuBatchProgressPhase**](RichMenuBatchProgressPhase.md) |  | 
**accepted_time** | **datetime** | The accepted time in milliseconds of the request of batch control the rich menu.  Format: ISO 8601 (e.g. 2023-06-08T10:15:30.121Z) Timezone: UTC  | 
**completed_time** | **datetime** | The completed time in milliseconds of rich menu batch control. Returned when the phase property is succeeded or failed.  Format: ISO 8601 (e.g. 2023-06-08T10:15:30.121Z) Timezone: UTC  | [optional] 

## Example

```python
from linebot.v3.messaging.models.rich_menu_batch_progress_response import RichMenuBatchProgressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RichMenuBatchProgressResponse from a JSON string
rich_menu_batch_progress_response_instance = RichMenuBatchProgressResponse.from_json(json)
# print the JSON string representation of the object
print RichMenuBatchProgressResponse.to_json()

# convert the object into a dict
rich_menu_batch_progress_response_dict = rich_menu_batch_progress_response_instance.to_dict()
# create an instance of RichMenuBatchProgressResponse from a dict
rich_menu_batch_progress_response_form_dict = rich_menu_batch_progress_response.from_dict(rich_menu_batch_progress_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


