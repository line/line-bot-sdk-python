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
from pydantic import BaseModel
from linebot.messaging.models.action import Action
from linebot.messaging.models.rich_menu_bounds import RichMenuBounds

class RichMenuArea(BaseModel):
    """
    Rich menu area
    """
    bounds: Optional[RichMenuBounds] = None
    action: Optional[Action] = None

    __properties = ["bounds", "action"]

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
    def from_json(cls, json_str: str) -> RichMenuArea:
        """Create an instance of RichMenuArea from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of bounds
        if self.bounds:
            _dict['bounds'] = self.bounds.to_dict()
        # override the default output from pydantic by calling `to_dict()` of action
        if self.action:
            _dict['action'] = self.action.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RichMenuArea:
        """Create an instance of RichMenuArea from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RichMenuArea.parse_obj(obj)

        _obj = RichMenuArea.parse_obj({
            "bounds": RichMenuBounds.from_dict(obj.get("bounds")) if obj.get("bounds") is not None else None,
            "action": Action.from_dict(obj.get("action")) if obj.get("action") is not None else None
        })
        return _obj

