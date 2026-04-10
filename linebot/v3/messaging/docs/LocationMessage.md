# LocationMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**address** | **str** |  | 
**latitude** | **float** |  | 
**longitude** | **float** |  | 

## Example

```python
from linebot.v3.messaging.models.location_message import LocationMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LocationMessage from a JSON string
location_message_instance = LocationMessage.from_json(json)
# print the JSON string representation of the object
print LocationMessage.to_json()

# convert the object into a dict
location_message_dict = location_message_instance.to_dict()
# create an instance of LocationMessage from a dict
location_message_form_dict = location_message.from_dict(location_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


