# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .base import Base
from .messages import (
    TextMessage,
    ImageMessage,
    VideoMessage,
    AudioMessage,
    LocationMessage,
    StickerMessage
)
from .sources import SourceUser, SourceGroup, SourceRoom


class Event(Base):
    """Webhook Event

    https://devdocs.line.me/en/#webhook-event-object
    """

    def __init__(self, timestamp=None, source=None, **kwargs):
        super(Event, self).__init__(**kwargs)

        self.type = None
        self.timestamp = timestamp
        self.source = self.get_or_new_from_json_dict_with_types(
            source, {
                'user': SourceUser,
                'group': SourceGroup,
                'room': SourceRoom,
            }
        )


class MessageEvent(Event):
    def __init__(
            self, timestamp=None, source=None, reply_token=None,
            message=None, **kwargs
    ):
        """MessageEvent

        https://devdocs.line.me/en/#message-event

        Event object which contains the sent message.
        The message field contains a message object which corresponds with the message type.
        You can reply to message events.

        Args:
            timestamp: Time of the event in milliseconds
            source: Source object which contains the source of the event
            reply_token: Token for replying to this event
            message: Contents of the message
            **kwargs:
        """
        super(MessageEvent, self).__init__(
            timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'message'
        self.reply_token = reply_token
        self.message = self.get_or_new_from_json_dict_with_types(
            message, {
                'text': TextMessage,
                'image': ImageMessage,
                'video': VideoMessage,
                'audio': AudioMessage,
                'location': LocationMessage,
                'sticker': StickerMessage
            }
        )


class FollowEvent(Event):
    def __init__(
            self, timestamp=None, source=None, reply_token=None, **kwargs
    ):
        """FollowEvent

        https://devdocs.line.me/en/#follow-event

        Event object for when your account is added as a friend (or unblocked). You can reply to follow events.

        Args:
            timestamp: Time of the event in milliseconds
            source: Source object which contains the source of the event
            reply_token: Token for replying to this event
            **kwargs:
        """
        super(FollowEvent, self).__init__(
            timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'follow'
        self.reply_token = reply_token


class UnfollowEvent(Event):
    def __init__(self, timestamp=None, source=None, **kwargs):
        """UnfollowEvent

        https://devdocs.line.me/en/#unfollow-event

        Event object for when your account is blocked.

        Args:
            timestamp: Time of the event in milliseconds
            source: Source object which contains the source of the event
            **kwargs:
        """
        super(UnfollowEvent, self).__init__(
            timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'unfollow'


class JoinEvent(Event):
    def __init__(
            self, timestamp=None, source=None, reply_token=None, **kwargs
    ):
        """JoinEvent

        https://devdocs.line.me/en/#join-event

        Event object for when your account joins a group or talk room. You can reply to join events.

        Args:
            timestamp: Time of the event in milliseconds
            source: Source object which contains the source of the event
            reply_token: Token for replying to this event
            **kwargs:
        """
        super(JoinEvent, self).__init__(
            timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'join'
        self.reply_token = reply_token


class LeaveEvent(Event):
    def __init__(self, timestamp=None, source=None, **kwargs):
        """LeaveEvent

        https://devdocs.line.me/en/#leave-event

        Event object for when your account leaves a group.

        Args:
            timestamp: Time of the event in milliseconds
            source: Source object which contains the source of the event
            **kwargs:
        """
        super(LeaveEvent, self).__init__(
            timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'leave'


class PostbackEvent(Event):
    def __init__(
            self, timestamp=None, source=None,
            reply_token=None, postback=None, **kwargs
    ):
        """PostbackEvent

        https://devdocs.line.me/en/#postback-event

        Event object for when a user performs an action on a template message which initiates a postback.
        You can reply to postback events.

        Args:
            timestamp: Time of the event in milliseconds
            source: Source object which contains the source of the event
            reply_token: Token for replying to this event
            postback: Postback data
            **kwargs:
        """
        super(PostbackEvent, self).__init__(
            timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'postback'
        self.reply_token = reply_token
        self.postback = self.get_or_new_from_json_dict(
            postback, Postback
        )


class BeaconEvent(Event):
    def __init__(
            self, timestamp=None, source=None, reply_token=None,
            beacon=None, **kwargs
    ):
        """BeaconEvent

        https://devdocs.line.me/en/#beacon-event

        Event object for when a user detects a LINE Beacon. You can reply to beacon events.

        Args:
            timestamp: Time of the event in milliseconds
            source: Source object which contains the source of the event
            reply_token: Token for replying to this event
            beacon: Beacon object
            **kwargs:
        """
        super(BeaconEvent, self).__init__(
            timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'beacon'
        self.reply_token = reply_token
        self.beacon = self.get_or_new_from_json_dict(
            beacon, Beacon
        )


class Postback(Base):
    def __init__(self, data=None, **kwargs):
        """Postback

        https://devdocs.line.me/en/#postback-event

        Args:
            data: Postback data
            **kwargs:
        """
        super(Postback, self).__init__(**kwargs)

        self.data = data


class Beacon(Base):
    """Beacon

    https://devdocs.line.me/en/#beacon-event
    """

    def __init__(self, type=None, hwid=None, **kwargs):
        """Beacon

        https://devdocs.line.me/en/#beacon-event

        Args:
            type: Type of beacon event
            hwid: Hardware ID of the beacon that was detected
            **kwargs:
        """
        super(Beacon, self).__init__(**kwargs)

        self.type = type
        self.hwid = hwid
