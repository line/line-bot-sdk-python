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
from pydantic import BaseModel, Field, StrictStr
from linebot.v3.messaging.models.action import Action
from linebot.v3.messaging.models.alt_uri import AltUri

class URIAction(Action):
    """
    URIAction
    """
    uri: Optional[StrictStr] = None
    alt_uri: Optional[AltUri] = Field(None, alias="altUri")
    type: str = "uri"

    __properties = ["type", "label", "uri", "altUri"]

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
    def from_json(cls, json_str: str) -> URIAction:
        """Create an instance of URIAction from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of alt_uri
        if self.alt_uri:
            _dict['altUri'] = self.alt_uri.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> URIAction:
        """Create an instance of URIAction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return URIAction.parse_obj(obj)

        _obj = URIAction.parse_obj({
            "type": obj.get("type"),
            "label": obj.get("label"),
            "uri": obj.get("uri"),
            "alt_uri": AltUri.from_dict(obj.get("altUri")) if obj.get("altUri") is not None else None
        })
        return _obj

