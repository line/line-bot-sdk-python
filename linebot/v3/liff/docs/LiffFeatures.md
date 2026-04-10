# LiffFeatures


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ble** | **bool** | &#x60;true&#x60; if the LIFF app supports Bluetooth® Low Energy for LINE Things. &#x60;false&#x60; otherwise.  | [optional] 
**qr_code** | **bool** | &#x60;true&#x60; to use the 2D code reader in the LIFF app. false otherwise. The default value is &#x60;false&#x60;.  | [optional] [default to False]

## Example

```python
from linebot.v3.liff.models.liff_features import LiffFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of LiffFeatures from a JSON string
liff_features_instance = LiffFeatures.from_json(json)
# print the JSON string representation of the object
print LiffFeatures.to_json()

# convert the object into a dict
liff_features_dict = liff_features_instance.to_dict()
# create an instance of LiffFeatures from a dict
liff_features_form_dict = liff_features.from_dict(liff_features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


