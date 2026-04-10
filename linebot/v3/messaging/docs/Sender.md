# Sender

Change icon and display name

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name. Certain words such as &#x60;LINE&#x60; may not be used. | [optional] 
**icon_url** | **str** | URL of the image to display as an icon when sending a message | [optional] 

## Example

```python
from linebot.v3.messaging.models.sender import Sender

# TODO update the JSON string below
json = "{}"
# create an instance of Sender from a JSON string
sender_instance = Sender.from_json(json)
# print the JSON string representation of the object
print Sender.to_json()

# convert the object into a dict
sender_dict = sender_instance.to_dict()
# create an instance of Sender from a dict
sender_form_dict = sender.from_dict(sender_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


