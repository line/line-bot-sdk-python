# GroupSummaryResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | Group ID | 
**group_name** | **str** | Group name | 
**picture_url** | **str** | Group icon URL. Not included in the response if the user doesn&#39;t set a group profile icon. | [optional] 

## Example

```python
from linebot.v3.messaging.models.group_summary_response import GroupSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSummaryResponse from a JSON string
group_summary_response_instance = GroupSummaryResponse.from_json(json)
# print the JSON string representation of the object
print GroupSummaryResponse.to_json()

# convert the object into a dict
group_summary_response_dict = group_summary_response_instance.to_dict()
# create an instance of GroupSummaryResponse from a dict
group_summary_response_form_dict = group_summary_response.from_dict(group_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


