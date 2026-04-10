# TextMessageV2


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**substitution** | [**Dict[str, SubstitutionObject]**](SubstitutionObject.md) | A mapping that specifies substitutions for parts enclosed in {} within the &#x60;text&#x60; field. | [optional] 
**quote_token** | **str** | Quote token of the message you want to quote. | [optional] 

## Example

```python
from linebot.v3.messaging.models.text_message_v2 import TextMessageV2

# TODO update the JSON string below
json = "{}"
# create an instance of TextMessageV2 from a JSON string
text_message_v2_instance = TextMessageV2.from_json(json)
# print the JSON string representation of the object
print TextMessageV2.to_json()

# convert the object into a dict
text_message_v2_dict = text_message_v2_instance.to_dict()
# create an instance of TextMessageV2 from a dict
text_message_v2_form_dict = text_message_v2.from_dict(text_message_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


