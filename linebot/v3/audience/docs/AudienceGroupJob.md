# AudienceGroupJob

Audience group job

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience_group_job_id** | **int** | A job ID. | [optional] 
**audience_group_id** | **int** | An audience ID. | [optional] 
**description** | **str** | The job&#39;s description. | [optional] 
**type** | [**AudienceGroupJobType**](AudienceGroupJobType.md) |  | [optional] 
**job_status** | [**AudienceGroupJobStatus**](AudienceGroupJobStatus.md) |  | [optional] 
**failed_type** | [**AudienceGroupJobFailedType**](AudienceGroupJobFailedType.md) |  | [optional] 
**audience_count** | **int** | The number of accounts (recipients) that were added or removed. | [optional] 
**created** | **int** | When the job was created (in UNIX time). | [optional] 

## Example

```python
from linebot.v3.audience.models.audience_group_job import AudienceGroupJob

# TODO update the JSON string below
json = "{}"
# create an instance of AudienceGroupJob from a JSON string
audience_group_job_instance = AudienceGroupJob.from_json(json)
# print the JSON string representation of the object
print AudienceGroupJob.to_json()

# convert the object into a dict
audience_group_job_dict = audience_group_job_instance.to_dict()
# create an instance of AudienceGroupJob from a dict
audience_group_job_form_dict = audience_group_job.from_dict(audience_group_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


