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
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conlist, validator
from linebot.v3.messaging.models.action import Action
from linebot.v3.messaging.models.flex_box_background import FlexBoxBackground
from linebot.v3.messaging.models.flex_component import FlexComponent

class FlexBox(FlexComponent):
    """
    FlexBox
    """
    layout: Optional[StrictStr] = None
    flex: Optional[StrictInt] = None
    contents: Optional[conlist(FlexComponent)] = None
    spacing: Optional[StrictStr] = None
    margin: Optional[StrictStr] = None
    position: Optional[StrictStr] = None
    offset_top: Optional[StrictStr] = Field(None, alias="offsetTop")
    offset_bottom: Optional[StrictStr] = Field(None, alias="offsetBottom")
    offset_start: Optional[StrictStr] = Field(None, alias="offsetStart")
    offset_end: Optional[StrictStr] = Field(None, alias="offsetEnd")
    background_color: Optional[StrictStr] = Field(None, alias="backgroundColor")
    border_color: Optional[StrictStr] = Field(None, alias="borderColor")
    border_width: Optional[StrictStr] = Field(None, alias="borderWidth")
    corner_radius: Optional[StrictStr] = Field(None, alias="cornerRadius")
    width: Optional[StrictStr] = None
    max_width: Optional[StrictStr] = Field(None, alias="maxWidth")
    height: Optional[StrictStr] = None
    max_height: Optional[StrictStr] = Field(None, alias="maxHeight")
    padding_all: Optional[StrictStr] = Field(None, alias="paddingAll")
    padding_top: Optional[StrictStr] = Field(None, alias="paddingTop")
    padding_bottom: Optional[StrictStr] = Field(None, alias="paddingBottom")
    padding_start: Optional[StrictStr] = Field(None, alias="paddingStart")
    padding_end: Optional[StrictStr] = Field(None, alias="paddingEnd")
    action: Optional[Action] = None
    justify_content: Optional[StrictStr] = Field(None, alias="justifyContent")
    align_items: Optional[StrictStr] = Field(None, alias="alignItems")
    background: Optional[FlexBoxBackground] = None
    type: str = "box"

    __properties = ["type", "layout", "flex", "contents", "spacing", "margin", "position", "offsetTop", "offsetBottom", "offsetStart", "offsetEnd", "backgroundColor", "borderColor", "borderWidth", "cornerRadius", "width", "maxWidth", "height", "maxHeight", "paddingAll", "paddingTop", "paddingBottom", "paddingStart", "paddingEnd", "action", "justifyContent", "alignItems", "background"]

    @validator('layout')
    def layout_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('horizontal', 'vertical', 'baseline'):
            raise ValueError("must be one of enum values ('horizontal', 'vertical', 'baseline')")
        return value

    @validator('position')
    def position_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('relative', 'absolute'):
            raise ValueError("must be one of enum values ('relative', 'absolute')")
        return value

    @validator('justify_content')
    def justify_content_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('center', 'flex-start', 'flex-end', 'space-between', 'space-around', 'space-evenly'):
            raise ValueError("must be one of enum values ('center', 'flex-start', 'flex-end', 'space-between', 'space-around', 'space-evenly')")
        return value

    @validator('align_items')
    def align_items_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('center', 'flex-start', 'flex-end'):
            raise ValueError("must be one of enum values ('center', 'flex-start', 'flex-end')")
        return value

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
    def from_json(cls, json_str: str) -> FlexBox:
        """Create an instance of FlexBox from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic.v1 by calling `to_dict()` of each item in contents (list)
        _items = []
        if self.contents:
            for _item in self.contents:
                if _item:
                    _items.append(_item.to_dict())
            _dict['contents'] = _items
        # override the default output from pydantic.v1 by calling `to_dict()` of action
        if self.action:
            _dict['action'] = self.action.to_dict()
        # override the default output from pydantic.v1 by calling `to_dict()` of background
        if self.background:
            _dict['background'] = self.background.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FlexBox:
        """Create an instance of FlexBox from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FlexBox.parse_obj(obj)

        _obj = FlexBox.parse_obj({
            "type": obj.get("type"),
            "layout": obj.get("layout"),
            "flex": obj.get("flex"),
            "contents": [FlexComponent.from_dict(_item) for _item in obj.get("contents")] if obj.get("contents") is not None else None,
            "spacing": obj.get("spacing"),
            "margin": obj.get("margin"),
            "position": obj.get("position"),
            "offset_top": obj.get("offsetTop"),
            "offset_bottom": obj.get("offsetBottom"),
            "offset_start": obj.get("offsetStart"),
            "offset_end": obj.get("offsetEnd"),
            "background_color": obj.get("backgroundColor"),
            "border_color": obj.get("borderColor"),
            "border_width": obj.get("borderWidth"),
            "corner_radius": obj.get("cornerRadius"),
            "width": obj.get("width"),
            "max_width": obj.get("maxWidth"),
            "height": obj.get("height"),
            "max_height": obj.get("maxHeight"),
            "padding_all": obj.get("paddingAll"),
            "padding_top": obj.get("paddingTop"),
            "padding_bottom": obj.get("paddingBottom"),
            "padding_start": obj.get("paddingStart"),
            "padding_end": obj.get("paddingEnd"),
            "action": Action.from_dict(obj.get("action")) if obj.get("action") is not None else None,
            "justify_content": obj.get("justifyContent"),
            "align_items": obj.get("alignItems"),
            "background": FlexBoxBackground.from_dict(obj.get("background")) if obj.get("background") is not None else None
        })
        return _obj

