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
from pydantic import BaseModel, Field, StrictStr, conlist
from linebot.v3.messaging.models.carousel_column import CarouselColumn
from linebot.v3.messaging.models.template import Template

class CarouselTemplate(Template):
    """
    CarouselTemplate
    """
    columns: Optional[conlist(CarouselColumn)] = None
    image_aspect_ratio: Optional[StrictStr] = Field(None, alias="imageAspectRatio")
    image_size: Optional[StrictStr] = Field(None, alias="imageSize")
    type: str = "carousel"

    __properties = ["type", "columns", "imageAspectRatio", "imageSize"]

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
    def from_json(cls, json_str: str) -> CarouselTemplate:
        """Create an instance of CarouselTemplate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in columns (list)
        _items = []
        if self.columns:
            for _item in self.columns:
                if _item:
                    _items.append(_item.to_dict())
            _dict['columns'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CarouselTemplate:
        """Create an instance of CarouselTemplate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CarouselTemplate.parse_obj(obj)

        _obj = CarouselTemplate.parse_obj({
            "type": obj.get("type"),
            "columns": [CarouselColumn.from_dict(_item) for _item in obj.get("columns")] if obj.get("columns") is not None else None,
            "image_aspect_ratio": obj.get("imageAspectRatio"),
            "image_size": obj.get("imageSize")
        })
        return _obj

