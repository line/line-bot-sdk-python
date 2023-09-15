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


from typing import List
from pydantic.v1 import BaseModel, Field, conlist
from linebot.v3.messaging.models.sent_message import SentMessage

class PushMessageResponse(BaseModel):
    """
    PushMessageResponse
    https://developers.line.biz/en/reference/messaging-api/#send-push-message-response
    """
    sent_messages: conlist(SentMessage, max_items=5, min_items=1) = Field(..., alias="sentMessages", description="Array of sent messages.")

    __properties = ["sentMessages"]

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
    def from_json(cls, json_str: str) -> PushMessageResponse:
        """Create an instance of PushMessageResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic.v1 by calling `to_dict()` of each item in sent_messages (list)
        _items = []
        if self.sent_messages:
            for _item in self.sent_messages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sentMessages'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PushMessageResponse:
        """Create an instance of PushMessageResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PushMessageResponse.parse_obj(obj)

        _obj = PushMessageResponse.parse_obj({
            "sent_messages": [SentMessage.from_dict(_item) for _item in obj.get("sentMessages")] if obj.get("sentMessages") is not None else None
        })
        return _obj
