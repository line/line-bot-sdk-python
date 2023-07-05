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
from pydantic import BaseModel, Field, StrictBool, conint

class AcquireChatControlRequest(BaseModel):
    """
    Request entity of the Acquire Control API
    https://developers.line.biz/en/reference/partner-docs/#acquire-control-api
    """
    expired: Optional[StrictBool] = Field(None, description="`True`: After the time limit (ttl) has passed, the initiative (Chat Control) will return to the Primary Channel. (Default) `False`: There's no time limit and the initiative (Chat Control) doesn't change over time. ")
    ttl: Optional[conint(strict=True, le=31536000)] = Field(None, description="The time it takes for initiative (Chat Control) to return to the Primary Channel (the time that the module channel stays on the Active Channel). The value is specified in seconds. The maximum value is one year (3600 * 24 * 365). The default value is 3600 (1 hour).  * Ignored if the value of expired is false. ")

    __properties = ["expired", "ttl"]

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
    def from_json(cls, json_str: str) -> AcquireChatControlRequest:
        """Create an instance of AcquireChatControlRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AcquireChatControlRequest:
        """Create an instance of AcquireChatControlRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AcquireChatControlRequest.parse_obj(obj)

        _obj = AcquireChatControlRequest.parse_obj({
            "expired": obj.get("expired"),
            "ttl": obj.get("ttl")
        })
        return _obj

