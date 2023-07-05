# coding: utf-8

"""
    LINE Messaging API

    This document describes LINE Messaging API.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, constr, validator
from linebot.v3.messaging.models.message import Message

class MulticastRequest(BaseModel):
    """
    MulticastRequest
    https://developers.line.biz/en/reference/messaging-api/#send-multicast-message
    """
    messages: conlist(Message, max_items=5, min_items=1) = Field(..., description="Messages to send")
    to: conlist(StrictStr, max_items=500, min_items=1) = Field(..., description="Array of user IDs. Use userId values which are returned in webhook event objects. Do not use LINE IDs found on LINE.")
    notification_disabled: Optional[StrictBool] = Field(False, alias="notificationDisabled", description="`true`: The user doesn’t receive a push notification when a message is sent. `false`: The user receives a push notification when the message is sent (unless they have disabled push notifications in LINE and/or their device). The default value is false. ")
    custom_aggregation_units: Optional[conlist(constr(strict=True, max_length=30, min_length=1), max_items=1)] = Field(None, alias="customAggregationUnits", description="Name of aggregation unit. Case-sensitive.")

    __properties = ["messages", "to", "notificationDisabled", "customAggregationUnits"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> MulticastRequest:
        """Create an instance of MulticastRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in messages (list)
        _items = []
        if self.messages:
            for _item in self.messages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['messages'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MulticastRequest:
        """Create an instance of MulticastRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MulticastRequest.parse_obj(obj)

        _obj = MulticastRequest.parse_obj({
            "messages": [Message.from_dict(_item) for _item in obj.get("messages")] if obj.get("messages") is not None else None,
            "to": obj.get("to"),
            "notification_disabled": obj.get("notificationDisabled") if obj.get("notificationDisabled") is not None else False,
            "custom_aggregation_units": obj.get("customAggregationUnits")
        })
        return _obj

