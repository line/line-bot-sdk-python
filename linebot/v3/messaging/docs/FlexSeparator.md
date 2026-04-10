# FlexSeparator


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**margin** | **str** |  | [optional] 
**color** | **str** |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.flex_separator import FlexSeparator

# TODO update the JSON string below
json = "{}"
# create an instance of FlexSeparator from a JSON string
flex_separator_instance = FlexSeparator.from_json(json)
# print the JSON string representation of the object
print FlexSeparator.to_json()

# convert the object into a dict
flex_separator_dict = flex_separator_instance.to_dict()
# create an instance of FlexSeparator from a dict
flex_separator_form_dict = flex_separator.from_dict(flex_separator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


