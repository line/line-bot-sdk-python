# GetAudienceDataResponse

Get audience data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience_group** | [**AudienceGroup**](AudienceGroup.md) |  | [optional] 
**jobs** | [**List[AudienceGroupJob]**](AudienceGroupJob.md) | An array of jobs. This array is used to keep track of each attempt to add new user IDs or IFAs to an audience for uploading user IDs. Empty array is returned for any other type of audience. Max: 50  | [optional] 
**adaccount** | [**Adaccount**](Adaccount.md) |  | [optional] 

## Example

```python
from linebot.v3.audience.models.get_audience_data_response import GetAudienceDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAudienceDataResponse from a JSON string
get_audience_data_response_instance = GetAudienceDataResponse.from_json(json)
# print the JSON string representation of the object
print GetAudienceDataResponse.to_json()

# convert the object into a dict
get_audience_data_response_dict = get_audience_data_response_instance.to_dict()
# create an instance of GetAudienceDataResponse from a dict
get_audience_data_response_form_dict = get_audience_data_response.from_dict(get_audience_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


