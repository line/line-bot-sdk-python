# UpdateAudienceGroupDescriptionRequest

Rename an audience

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The audience&#39;s name. This is case-insensitive, meaning AUDIENCE and audience are considered identical. Max character limit: 120  | [optional] 

## Example

```python
from linebot.v3.audience.models.update_audience_group_description_request import UpdateAudienceGroupDescriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAudienceGroupDescriptionRequest from a JSON string
update_audience_group_description_request_instance = UpdateAudienceGroupDescriptionRequest.from_json(json)
# print the JSON string representation of the object
print UpdateAudienceGroupDescriptionRequest.to_json()

# convert the object into a dict
update_audience_group_description_request_dict = update_audience_group_description_request_instance.to_dict()
# create an instance of UpdateAudienceGroupDescriptionRequest from a dict
update_audience_group_description_request_form_dict = update_audience_group_description_request.from_dict(update_audience_group_description_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


