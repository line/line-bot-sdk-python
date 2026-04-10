# FlexSpan


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 
**size** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**weight** | **str** |  | [optional] 
**style** | **str** |  | [optional] 
**decoration** | **str** |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.flex_span import FlexSpan

# TODO update the JSON string below
json = "{}"
# create an instance of FlexSpan from a JSON string
flex_span_instance = FlexSpan.from_json(json)
# print the JSON string representation of the object
print FlexSpan.to_json()

# convert the object into a dict
flex_span_dict = flex_span_instance.to_dict()
# create an instance of FlexSpan from a dict
flex_span_form_dict = flex_span.from_dict(flex_span_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


