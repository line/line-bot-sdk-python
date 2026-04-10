# FlexMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alt_text** | **str** |  | 
**contents** | [**FlexContainer**](FlexContainer.md) |  | 

## Example

```python
from linebot.v3.messaging.models.flex_message import FlexMessage

# TODO update the JSON string below
json = "{}"
# create an instance of FlexMessage from a JSON string
flex_message_instance = FlexMessage.from_json(json)
# print the JSON string representation of the object
print FlexMessage.to_json()

# convert the object into a dict
flex_message_dict = flex_message_instance.to_dict()
# create an instance of FlexMessage from a dict
flex_message_form_dict = flex_message.from_dict(flex_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


