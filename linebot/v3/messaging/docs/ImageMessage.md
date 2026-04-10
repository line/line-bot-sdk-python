# ImageMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_content_url** | **str** |  | 
**preview_image_url** | **str** |  | 

## Example

```python
from linebot.v3.messaging.models.image_message import ImageMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ImageMessage from a JSON string
image_message_instance = ImageMessage.from_json(json)
# print the JSON string representation of the object
print ImageMessage.to_json()

# convert the object into a dict
image_message_dict = image_message_instance.to_dict()
# create an instance of ImageMessage from a dict
image_message_form_dict = image_message.from_dict(image_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


