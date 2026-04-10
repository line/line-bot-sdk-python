# LocationMessageContent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title | [optional] 
**address** | **str** | Address | [optional] 
**latitude** | **float** | Latitude | 
**longitude** | **float** | Longitude | 
**mark_as_read_token** | **str** | Token used to mark the message as read.  | [optional] 

## Example

```python
from linebot.v3.webhooks.models.location_message_content import LocationMessageContent

# TODO update the JSON string below
json = "{}"
# create an instance of LocationMessageContent from a JSON string
location_message_content_instance = LocationMessageContent.from_json(json)
# print the JSON string representation of the object
print LocationMessageContent.to_json()

# convert the object into a dict
location_message_content_dict = location_message_content_instance.to_dict()
# create an instance of LocationMessageContent from a dict
location_message_content_form_dict = location_message_content.from_dict(location_message_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


