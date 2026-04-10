# CreateAudienceGroupRequest

Create audience for uploading user IDs (by JSON)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The audience&#39;s name. This is case-insensitive, meaning AUDIENCE and audience are considered identical. Max character limit: 120  | [optional] 
**is_ifa_audience** | **bool** | To specify recipients by IFAs: set true. To specify recipients by user IDs: set false or omit isIfaAudience property.  | [optional] 
**upload_description** | **str** | The description to register for the job (in jobs[].description).  | [optional] 
**audiences** | [**List[Audience]**](Audience.md) | An array of user IDs or IFAs. Max number: 10,000  | [optional] 

## Example

```python
from linebot.v3.audience.models.create_audience_group_request import CreateAudienceGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAudienceGroupRequest from a JSON string
create_audience_group_request_instance = CreateAudienceGroupRequest.from_json(json)
# print the JSON string representation of the object
print CreateAudienceGroupRequest.to_json()

# convert the object into a dict
create_audience_group_request_dict = create_audience_group_request_instance.to_dict()
# create an instance of CreateAudienceGroupRequest from a dict
create_audience_group_request_form_dict = create_audience_group_request.from_dict(create_audience_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


