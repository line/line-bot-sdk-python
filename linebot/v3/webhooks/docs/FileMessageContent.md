# FileMessageContent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | File name | 
**file_size** | **int** | File size in bytes | 
**mark_as_read_token** | **str** | Token used to mark the message as read.  | [optional] 

## Example

```python
from linebot.v3.webhooks.models.file_message_content import FileMessageContent

# TODO update the JSON string below
json = "{}"
# create an instance of FileMessageContent from a JSON string
file_message_content_instance = FileMessageContent.from_json(json)
# print the JSON string representation of the object
print FileMessageContent.to_json()

# convert the object into a dict
file_message_content_dict = file_message_content_instance.to_dict()
# create an instance of FileMessageContent from a dict
file_message_content_form_dict = file_message_content.from_dict(file_message_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


