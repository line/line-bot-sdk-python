# AddAudienceToAudienceGroupRequest

Add user IDs or Identifiers for Advertisers (IFAs) to an audience for uploading user IDs (by JSON)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience_group_id** | **int** | The audience ID. | [optional] 
**upload_description** | **str** | The audience&#39;s name. | [optional] 
**audiences** | [**List[Audience]**](Audience.md) | An array of up to 10,000 user IDs or IFAs. | [optional] 

## Example

```python
from linebot.v3.audience.models.add_audience_to_audience_group_request import AddAudienceToAudienceGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddAudienceToAudienceGroupRequest from a JSON string
add_audience_to_audience_group_request_instance = AddAudienceToAudienceGroupRequest.from_json(json)
# print the JSON string representation of the object
print AddAudienceToAudienceGroupRequest.to_json()

# convert the object into a dict
add_audience_to_audience_group_request_dict = add_audience_to_audience_group_request_instance.to_dict()
# create an instance of AddAudienceToAudienceGroupRequest from a dict
add_audience_to_audience_group_request_form_dict = add_audience_to_audience_group_request.from_dict(add_audience_to_audience_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


