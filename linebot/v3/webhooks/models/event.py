# coding: utf-8

"""
    Webhook Type Definition

    Webhook event definition of the LINE Messaging API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json
import linebot.v3.webhooks.models


from typing import Optional, Union
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr
from linebot.v3.webhooks.models.delivery_context import DeliveryContext
from linebot.v3.webhooks.models.event_mode import EventMode
from linebot.v3.webhooks.models.source import Source

class Event(BaseModel):
    """
    Webhook event
    """
    type: StrictStr = Field(..., description="Type of the event")
    source: Optional[Source] = None
    timestamp: StrictInt = Field(..., description="Time of the event in milliseconds.")
    mode: EventMode = Field(...)
    webhook_event_id: StrictStr = Field(..., alias="webhookEventId", description="Webhook Event ID. An ID that uniquely identifies a webhook event. This is a string in ULID format.")
    delivery_context: DeliveryContext = Field(..., alias="deliveryContext")

    __properties = ["type", "source", "timestamp", "mode", "webhookEventId", "deliveryContext"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    # JSON field name that stores the object type
    __discriminator_property_name = 'type'

    # discriminator mappings
    __discriminator_value_class_map = {
        'accountLink': 'AccountLinkEvent',
        'activated': 'ActivatedEvent',
        'beacon': 'BeaconEvent',
        'botResumed': 'BotResumedEvent',
        'botSuspended': 'BotSuspendedEvent',
        'deactivated': 'DeactivatedEvent',
        'delivery': 'PnpDeliveryCompletionEvent',
        'follow': 'FollowEvent',
        'join': 'JoinEvent',
        'leave': 'LeaveEvent',
        'memberJoined': 'MemberJoinedEvent',
        'memberLeft': 'MemberLeftEvent',
        'membership': 'MembershipEvent',
        'message': 'MessageEvent',
        'module': 'ModuleEvent',
        'postback': 'PostbackEvent',
        'things': 'ThingsEvent',
        'unfollow': 'UnfollowEvent',
        'unsend': 'UnsendEvent',
        'videoPlayComplete': 'VideoPlayCompleteEvent'
    }

    @classmethod
    def get_discriminator_value(cls, obj: dict) -> str:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Union(AccountLinkEvent, ActivatedEvent, BeaconEvent, BotResumedEvent, BotSuspendedEvent, DeactivatedEvent, FollowEvent, JoinEvent, LeaveEvent, MemberJoinedEvent, MemberLeftEvent, MembershipEvent, MessageEvent, ModuleEvent, PnpDeliveryCompletionEvent, PostbackEvent, ThingsEvent, UnfollowEvent, UnsendEvent, VideoPlayCompleteEvent):
        """Create an instance of Event from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic.v1 by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic.v1 by calling `to_dict()` of delivery_context
        if self.delivery_context:
            _dict['deliveryContext'] = self.delivery_context.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Union(AccountLinkEvent, ActivatedEvent, BeaconEvent, BotResumedEvent, BotSuspendedEvent, DeactivatedEvent, FollowEvent, JoinEvent, LeaveEvent, MemberJoinedEvent, MemberLeftEvent, MembershipEvent, MessageEvent, ModuleEvent, PnpDeliveryCompletionEvent, PostbackEvent, ThingsEvent, UnfollowEvent, UnsendEvent, VideoPlayCompleteEvent):
        """Create an instance of Event from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = getattr(linebot.v3.webhooks.models, object_type)
            return klass.from_dict(obj)
        else:
            raise ValueError("Event failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

