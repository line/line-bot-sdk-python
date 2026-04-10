# ImageMessageContent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_provider** | [**ContentProvider**](ContentProvider.md) |  | 
**image_set** | [**ImageSet**](ImageSet.md) |  | [optional] 
**quote_token** | **str** | Quote token to quote this message.  | 
**mark_as_read_token** | **str** | Token used to mark the message as read.  | [optional] 

## Example

```python
from linebot.v3.webhooks.models.image_message_content import ImageMessageContent

# TODO update the JSON string below
json = "{}"
# create an instance of ImageMessageContent from a JSON string
image_message_content_instance = ImageMessageContent.from_json(json)
# print the JSON string representation of the object
print ImageMessageContent.to_json()

# convert the object into a dict
image_message_content_dict = image_message_content_instance.to_dict()
# create an instance of ImageMessageContent from a dict
image_message_content_form_dict = image_message_content.from_dict(image_message_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


