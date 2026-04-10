# BeaconContent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hwid** | **str** | Hardware ID of the beacon that was detected | 
**type** | **str** | Type of beacon event. | 
**dm** | **str** | Device message of beacon that was detected. | [optional] 

## Example

```python
from linebot.v3.webhooks.models.beacon_content import BeaconContent

# TODO update the JSON string below
json = "{}"
# create an instance of BeaconContent from a JSON string
beacon_content_instance = BeaconContent.from_json(json)
# print the JSON string representation of the object
print BeaconContent.to_json()

# convert the object into a dict
beacon_content_dict = beacon_content_instance.to_dict()
# create an instance of BeaconContent from a dict
beacon_content_form_dict = beacon_content.from_dict(beacon_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


