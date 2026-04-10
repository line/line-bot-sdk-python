# CreateImpBasedAudienceGroupResponse

Create audience for impression-based retargeting

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience_group_id** | **int** | The audience ID. | [optional] 
**type** | [**AudienceGroupType**](AudienceGroupType.md) |  | [optional] 
**description** | **str** | The audience&#39;s name. | [optional] 
**created** | **int** | When the audience was created (in UNIX time). | [optional] 
**request_id** | **str** | The request ID that was specified when the audience was created. | [optional] 

## Example

```python
from linebot.v3.audience.models.create_imp_based_audience_group_response import CreateImpBasedAudienceGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateImpBasedAudienceGroupResponse from a JSON string
create_imp_based_audience_group_response_instance = CreateImpBasedAudienceGroupResponse.from_json(json)
# print the JSON string representation of the object
print CreateImpBasedAudienceGroupResponse.to_json()

# convert the object into a dict
create_imp_based_audience_group_response_dict = create_imp_based_audience_group_response_instance.to_dict()
# create an instance of CreateImpBasedAudienceGroupResponse from a dict
create_imp_based_audience_group_response_form_dict = create_imp_based_audience_group_response.from_dict(create_imp_based_audience_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


