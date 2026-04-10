# MissionStickerRequest

Send mission stickers (v3)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** | Destination user ID | 
**product_id** | **str** | Package ID for a set of stickers | 
**product_type** | **str** | &#x60;STICKER&#x60; | 
**send_present_message** | **bool** | &#x60;false&#x60; | 

## Example

```python
from linebot.v3.shop.models.mission_sticker_request import MissionStickerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MissionStickerRequest from a JSON string
mission_sticker_request_instance = MissionStickerRequest.from_json(json)
# print the JSON string representation of the object
print MissionStickerRequest.to_json()

# convert the object into a dict
mission_sticker_request_dict = mission_sticker_request_instance.to_dict()
# create an instance of MissionStickerRequest from a dict
mission_sticker_request_form_dict = mission_sticker_request.from_dict(mission_sticker_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


