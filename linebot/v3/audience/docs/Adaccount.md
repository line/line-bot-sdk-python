# Adaccount

Adaccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Ad account name. | [optional] 

## Example

```python
from linebot.v3.audience.models.adaccount import Adaccount

# TODO update the JSON string below
json = "{}"
# create an instance of Adaccount from a JSON string
adaccount_instance = Adaccount.from_json(json)
# print the JSON string representation of the object
print Adaccount.to_json()

# convert the object into a dict
adaccount_dict = adaccount_instance.to_dict()
# create an instance of Adaccount from a dict
adaccount_form_dict = adaccount.from_dict(adaccount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


