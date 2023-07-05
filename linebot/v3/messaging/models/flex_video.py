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
from linebot.v3.messaging.models.flex_component import FlexComponent

class FlexVideo(FlexComponent):
    """
    FlexVideo
    """
    url: Optional[StrictStr] = None
    preview_url: Optional[StrictStr] = Field(None, alias="previewUrl")
    alt_content: Optional[FlexComponent] = Field(None, alias="altContent")
    aspect_ratio: Optional[StrictStr] = Field(None, alias="aspectRatio")
    action: Optional[Action] = None
    type: str = "video"

    __properties = ["type", "url", "previewUrl", "altContent", "aspectRatio", "action"]

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
    def from_json(cls, json_str: str) -> FlexVideo:
        """Create an instance of FlexVideo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of alt_content
        if self.alt_content:
            _dict['altContent'] = self.alt_content.to_dict()
        # override the default output from pydantic by calling `to_dict()` of action
        if self.action:
            _dict['action'] = self.action.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FlexVideo:
        """Create an instance of FlexVideo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FlexVideo.parse_obj(obj)

        _obj = FlexVideo.parse_obj({
            "type": obj.get("type"),
            "url": obj.get("url"),
            "preview_url": obj.get("previewUrl"),
            "alt_content": FlexComponent.from_dict(obj.get("altContent")) if obj.get("altContent") is not None else None,
            "aspect_ratio": obj.get("aspectRatio"),
            "action": Action.from_dict(obj.get("action")) if obj.get("action") is not None else None
        })
        return _obj

