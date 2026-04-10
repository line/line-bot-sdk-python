# DetailedOwner

Owner of this audience group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_type** | **str** | Service name where the audience group has been created. | [optional] 
**id** | **str** | Owner ID in the service. | [optional] 
**name** | **str** | Owner account name. | [optional] 

## Example

```python
from linebot.v3.audience.models.detailed_owner import DetailedOwner

# TODO update the JSON string below
json = "{}"
# create an instance of DetailedOwner from a JSON string
detailed_owner_instance = DetailedOwner.from_json(json)
# print the JSON string representation of the object
print DetailedOwner.to_json()

# convert the object into a dict
detailed_owner_dict = detailed_owner_instance.to_dict()
# create an instance of DetailedOwner from a dict
detailed_owner_form_dict = detailed_owner.from_dict(detailed_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


