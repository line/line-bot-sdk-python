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


from typing import Optional
from pydantic.v1 import Field, StrictStr
from linebot.v3.messaging.models.flex_container import FlexContainer
from linebot.v3.messaging.models.message import Message
from linebot.v3.messaging.models.quick_reply import QuickReply
from linebot.v3.messaging.models.sender import Sender

class FlexMessage(Message):
    """
    FlexMessage
    https://developers.line.biz/en/reference/messaging-api/#flex-message
    """
    alt_text: Optional[StrictStr] = Field(None, alias="altText")
    contents: Optional[FlexContainer] = None
    type: str = "flex"

    __properties = ["type", "quickReply", "sender", "altText", "contents"]

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
    def from_json(cls, json_str: str) -> FlexMessage:
        """Create an instance of FlexMessage from a JSON string"""
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
        # override the default output from pydantic.v1 by calling `to_dict()` of contents
        if self.contents:
            _dict['contents'] = self.contents.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FlexMessage:
        """Create an instance of FlexMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FlexMessage.parse_obj(obj)

        _obj = FlexMessage.parse_obj({
            "type": obj.get("type"),
            "quick_reply": QuickReply.from_dict(obj.get("quickReply")) if obj.get("quickReply") is not None else None,
            "sender": Sender.from_dict(obj.get("sender")) if obj.get("sender") is not None else None,
            "alt_text": obj.get("altText"),
            "contents": FlexContainer.from_dict(obj.get("contents")) if obj.get("contents") is not None else None
        })
        return _obj

