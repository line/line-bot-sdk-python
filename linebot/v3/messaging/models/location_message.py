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


from typing import Optional, Union
from pydantic.v1 import BaseModel, StrictFloat, StrictInt, StrictStr
from linebot.v3.messaging.models.message import Message
from linebot.v3.messaging.models.quick_reply import QuickReply
from linebot.v3.messaging.models.sender import Sender

class LocationMessage(Message):
    """
    LocationMessage
    """
    title: Optional[StrictStr] = None
    address: Optional[StrictStr] = None
    latitude: Optional[Union[StrictFloat, StrictInt]] = None
    longitude: Optional[Union[StrictFloat, StrictInt]] = None
    type: str = "location"

    __properties = ["type", "quickReply", "sender", "title", "address", "latitude", "longitude"]

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
    def from_json(cls, json_str: str) -> LocationMessage:
        """Create an instance of LocationMessage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic.v1 by calling `to_dict()` of quick_reply
        if self.quick_reply:
            _dict['quickReply'] = self.quick_reply.to_dict()
        # override the default output from pydantic.v1 by calling `to_dict()` of sender
        if self.sender:
            _dict['sender'] = self.sender.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LocationMessage:
        """Create an instance of LocationMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LocationMessage.parse_obj(obj)

        _obj = LocationMessage.parse_obj({
            "type": obj.get("type"),
            "quick_reply": QuickReply.from_dict(obj.get("quickReply")) if obj.get("quickReply") is not None else None,
            "sender": Sender.from_dict(obj.get("sender")) if obj.get("sender") is not None else None,
            "title": obj.get("title"),
            "address": obj.get("address"),
            "latitude": obj.get("latitude"),
            "longitude": obj.get("longitude")
        })
        return _obj

