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
from pydantic import BaseModel, Field
from linebot.audience.models.audience_group_authority_level import AudienceGroupAuthorityLevel

class GetAudienceGroupAuthorityLevelResponse(BaseModel):
    """
    Get the authority level of the audience
    https://developers.line.biz/en/reference/messaging-api/#get-authority-level
    """
    authority_level: Optional[AudienceGroupAuthorityLevel] = Field(None, alias="authorityLevel")

    __properties = ["authorityLevel"]

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
    def from_json(cls, json_str: str) -> GetAudienceGroupAuthorityLevelResponse:
        """Create an instance of GetAudienceGroupAuthorityLevelResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetAudienceGroupAuthorityLevelResponse:
        """Create an instance of GetAudienceGroupAuthorityLevelResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetAudienceGroupAuthorityLevelResponse.parse_obj(obj)

        _obj = GetAudienceGroupAuthorityLevelResponse.parse_obj({
            "authority_level": obj.get("authorityLevel")
        })
        return _obj

