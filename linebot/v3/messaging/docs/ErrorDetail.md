# ErrorDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Details of the error. Not included in the response under certain situations. | [optional] 
**var_property** | **str** | Location of where the error occurred. Returns the JSON field name or query parameter name of the request. Not included in the response under certain situations. | [optional] 

## Example

```python
from linebot.v3.messaging.models.error_detail import ErrorDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorDetail from a JSON string
error_detail_instance = ErrorDetail.from_json(json)
# print the JSON string representation of the object
print ErrorDetail.to_json()

# convert the object into a dict
error_detail_dict = error_detail_instance.to_dict()
# create an instance of ErrorDetail from a dict
error_detail_form_dict = error_detail.from_dict(error_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


