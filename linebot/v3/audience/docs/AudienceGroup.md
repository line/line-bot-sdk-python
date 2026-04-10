# AudienceGroup

Audience group

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience_group_id** | **int** | The audience ID. | [optional] 
**type** | [**AudienceGroupType**](AudienceGroupType.md) |  | [optional] 
**description** | **str** | The audience&#39;s name. | [optional] 
**status** | [**AudienceGroupStatus**](AudienceGroupStatus.md) |  | [optional] 
**failed_type** | [**AudienceGroupFailedType**](AudienceGroupFailedType.md) |  | [optional] 
**audience_count** | **int** | The number of users included in the audience. | [optional] 
**created** | **int** | When the audience was created (in UNIX time). | [optional] 
**request_id** | **str** | The request ID that was specified when the audience was created. This is only included when &#x60;audienceGroup.type&#x60; is CLICK or IMP.  | [optional] 
**click_url** | **str** | The URL that was specified when the audience was created. This is only included when &#x60;audienceGroup.type&#x60; is CLICK and link URL is specified.  | [optional] 
**is_ifa_audience** | **bool** | The value indicating the type of account to be sent, as specified when creating the audience for uploading user IDs.  | [optional] 
**permission** | [**AudienceGroupPermission**](AudienceGroupPermission.md) |  | [optional] 
**create_route** | [**AudienceGroupCreateRoute**](AudienceGroupCreateRoute.md) |  | [optional] 

## Example

```python
from linebot.v3.audience.models.audience_group import AudienceGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AudienceGroup from a JSON string
audience_group_instance = AudienceGroup.from_json(json)
# print the JSON string representation of the object
print AudienceGroup.to_json()

# convert the object into a dict
audience_group_dict = audience_group_instance.to_dict()
# create an instance of AudienceGroup from a dict
audience_group_form_dict = audience_group.from_dict(audience_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


