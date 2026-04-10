# GetSharedAudienceGroupsResponse

Gets data for more than one audience.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience_groups** | [**List[AudienceGroup]**](AudienceGroup.md) | An array of audience data. If there are no audiences that match the specified filter, an empty array will be returned. | [optional] 
**has_next_page** | **bool** | true when this is not the last page. | [optional] 
**total_count** | **int** | The total number of audiences that can be returned with the specified filter. | [optional] 
**read_write_audience_group_total_count** | **int** | Of the audiences you can get with the specified filter, the number of audiences with the update permission set to READ_WRITE. | [optional] 
**page** | **int** | The current page number. | [optional] 
**size** | **int** | The maximum number of audiences on the current page. | [optional] 

## Example

```python
from linebot.v3.audience.models.get_shared_audience_groups_response import GetSharedAudienceGroupsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSharedAudienceGroupsResponse from a JSON string
get_shared_audience_groups_response_instance = GetSharedAudienceGroupsResponse.from_json(json)
# print the JSON string representation of the object
print GetSharedAudienceGroupsResponse.to_json()

# convert the object into a dict
get_shared_audience_groups_response_dict = get_shared_audience_groups_response_instance.to_dict()
# create an instance of GetSharedAudienceGroupsResponse from a dict
get_shared_audience_groups_response_form_dict = get_shared_audience_groups_response.from_dict(get_shared_audience_groups_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


