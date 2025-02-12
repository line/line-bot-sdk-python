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
from pydantic.v1 import BaseModel, Field, conlist
from linebot.v3.audience.models.adaccount import Adaccount
from linebot.v3.audience.models.audience_group import AudienceGroup
from linebot.v3.audience.models.audience_group_job import AudienceGroupJob

class GetAudienceDataResponse(BaseModel):
    """
    Get audience data
    https://developers.line.biz/en/reference/messaging-api/#get-audience-group
    """
    audience_group: Optional[AudienceGroup] = Field(None, alias="audienceGroup")
    jobs: Optional[conlist(AudienceGroupJob, max_items=50)] = Field(None, description="An array of jobs. This array is used to keep track of each attempt to add new user IDs or IFAs to an audience for uploading user IDs. Empty array is returned for any other type of audience. Max: 50 ")
    adaccount: Optional[Adaccount] = None

    __properties = ["audienceGroup", "jobs", "adaccount"]

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
    def from_json(cls, json_str: str) -> GetAudienceDataResponse:
        """Create an instance of GetAudienceDataResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic.v1 by calling `to_dict()` of audience_group
        if self.audience_group:
            _dict['audienceGroup'] = self.audience_group.to_dict()
        # override the default output from pydantic.v1 by calling `to_dict()` of each item in jobs (list)
        _items = []
        if self.jobs:
            for _item in self.jobs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['jobs'] = _items
        # override the default output from pydantic.v1 by calling `to_dict()` of adaccount
        if self.adaccount:
            _dict['adaccount'] = self.adaccount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetAudienceDataResponse:
        """Create an instance of GetAudienceDataResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetAudienceDataResponse.parse_obj(obj)

        _obj = GetAudienceDataResponse.parse_obj({
            "audience_group": AudienceGroup.from_dict(obj.get("audienceGroup")) if obj.get("audienceGroup") is not None else None,
            "jobs": [AudienceGroupJob.from_dict(_item) for _item in obj.get("jobs")] if obj.get("jobs") is not None else None,
            "adaccount": Adaccount.from_dict(obj.get("adaccount")) if obj.get("adaccount") is not None else None
        })
        return _obj

