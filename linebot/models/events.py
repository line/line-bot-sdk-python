# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

"""linebot.models.events module."""

from __future__ import unicode_literals

from abc import ABCMeta

from future.utils import with_metaclass

from linebot.models.base import Base
from linebot.models.messages import (
    TextMessage,
    ImageMessage,
    VideoMessage,
    AudioMessage,
    LocationMessage,
    StickerMessage,
    FileMessage
)
from linebot.models.sources import SourceUser, SourceGroup, SourceRoom
from linebot.models.things import (
    DeviceUnlink,
    DeviceLink,
    ScenarioResult,
)
from linebot.models.things import Things  # noqa, backward compatibility


class Event(with_metaclass(ABCMeta, Base)):
    """Abstract Base Class of Webhook Event.

    https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects
    """

    def __init__(self, mode=None, timestamp=None, source=None, **kwargs):
        """__init__ method.

        :param str mode: Channel state
        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param kwargs:
        """
        super(Event, self).__init__(**kwargs)

        self.type = None
        self.mode = mode
        self.timestamp = timestamp
        self.source = self.get_or_new_from_json_dict_with_types(
            source, {
                'user': SourceUser,
                'group': SourceGroup,
                'room': SourceRoom,
            }
        )


class MessageEvent(Event):
    """Webhook MessageEvent.

    https://developers.line.biz/en/reference/messaging-api/#message-event

    Event object which contains the sent message.
    The message field contains a message object which corresponds with the message type.
    You can reply to message events.
    """

    def __init__(self, mode=None, timestamp=None, source=None, reply_token=None, message=None,
                 **kwargs):
        """__init__ method.

        :param str mode: Channel state
        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param str reply_token: Reply token
        :param message: Message object
        :type message: T <= :py:class:`linebot.models.messages.Message`
        :param kwargs:
        """
        super(MessageEvent, self).__init__(
            mode=mode, timestamp=timestamp, source=source, **kwargs
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
                'sticker': StickerMessage,
                'file': FileMessage
            }
        )


class FollowEvent(Event):
    """Webhook FollowEvent.

    https://developers.line.biz/en/reference/messaging-api/#follow-event

    Event object for when your account is added as a friend (or unblocked).
    You can reply to follow events.
    """

    def __init__(self, mode=None, timestamp=None, source=None, reply_token=None, **kwargs):
        """__init__ method.

        :param str mode: Channel state
        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param str reply_token: Reply token
        :param kwargs:
        """
        super(FollowEvent, self).__init__(
            mode=mode, timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'follow'
        self.reply_token = reply_token


class UnfollowEvent(Event):
    """Webhook UnfollowEvent.

    https://developers.line.biz/en/reference/messaging-api/#unfollow-event

    Event object for when your account is blocked.
    """

    def __init__(self, mode=None, timestamp=None, source=None, **kwargs):
        """__init__ method.

        :param str mode: Channel state
        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param kwargs:
        """
        super(UnfollowEvent, self).__init__(
            mode=mode, timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'unfollow'


class JoinEvent(Event):
    """Webhook JoinEvent.

    https://developers.line.biz/en/reference/messaging-api/#join-event

    Event object for when your account joins a group or talk room.
    You can reply to join events.
    """

    def __init__(self, mode=None, timestamp=None, source=None, reply_token=None, **kwargs):
        """__init__ method.

        :param str mode: Channel state
        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param str reply_token: Reply token
        :param kwargs:
        """
        super(JoinEvent, self).__init__(
            mode=mode, timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'join'
        self.reply_token = reply_token


class LeaveEvent(Event):
    """Webhook LeaveEvent.

    https://developers.line.biz/en/reference/messaging-api/#leave-event

    Event object for when your account leaves a group.
    """

    def __init__(self, mode=None, timestamp=None, source=None, **kwargs):
        """__init__ method.

        :param str mode: Channel state
        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param kwargs:
        """
        super(LeaveEvent, self).__init__(
            mode=mode, timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'leave'


class PostbackEvent(Event):
    """Webhook PostbackEvent.

    https://developers.line.biz/en/reference/messaging-api/#postback-event

    Event object for when a user performs an action on
    a template message which initiates a postback.
    You can reply to postback events.
    """

    def __init__(self, mode=None, timestamp=None, source=None, reply_token=None, postback=None,
                 **kwargs):
        """__init__ method.

        :param str mode: Channel state
        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param str reply_token: Reply token
        :param postback: Postback object
        :type postback: :py:class:`linebot.models.events.Postback`
        :param kwargs:
        """
        super(PostbackEvent, self).__init__(
            mode=mode, timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'postback'
        self.reply_token = reply_token
        self.postback = self.get_or_new_from_json_dict(
            postback, Postback
        )


class BeaconEvent(Event):
    """Webhook BeaconEvent.

    https://developers.line.biz/en/reference/messaging-api/#beacon-event

    Event object for when a user detects a LINE Beacon. You can reply to beacon events.
    """

    def __init__(self, mode=None, timestamp=None, source=None, reply_token=None, beacon=None,
                 **kwargs):
        """__init__ method.

        :param str mode: Channel state
        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param str reply_token: Reply token
        :param beacon: Beacon object
        :type beacon: :py:class:`linebot.models.events.Beacon`
        :param kwargs:
        """
        super(BeaconEvent, self).__init__(
            mode=mode, timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'beacon'
        self.reply_token = reply_token
        self.beacon = self.get_or_new_from_json_dict(
            beacon, Beacon
        )


class MemberJoinedEvent(Event):
    """Webhook MemberJoinedEvent.

    https://developers.line.biz/en/reference/messaging-api/#member-joined-event

    Event object for when a user joins a group or room that the bot is in.

    """

    def __init__(self, mode=None, timestamp=None, source=None, reply_token=None, joined=None,
                 **kwargs):
        """__init__ method.

        :param str mode: Channel state
        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param str reply_token: Reply token
        :param joined: Joined object
        :type joined: :py:class:`linebot.models.events.Joined`
        :param kwargs:
        """
        super(MemberJoinedEvent, self).__init__(
            mode=mode, timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'memberJoined'
        self.reply_token = reply_token
        self.joined = self.get_or_new_from_json_dict(
            joined, Joined
        )


class MemberLeftEvent(Event):
    """Webhook MemberLeftEvent.

    https://developers.line.biz/en/reference/messaging-api/#member-left-event

    Event object for when a user leaves a group or room that the bot is in.

    """

    def __init__(self, mode=None, timestamp=None, source=None, left=None, **kwargs):
        """__init__ method.

        :param str mode: Channel state
        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param left: Left object
        :type left: :py:class:`linebot.models.events.Left`
        :param kwargs:
        """
        super(MemberLeftEvent, self).__init__(
            mode=mode, timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'memberLeft'
        self.left = self.get_or_new_from_json_dict(
            left, Left
        )


class AccountLinkEvent(Event):
    """Webhook AccountLinkEvent.

    https://developers.line.me/en/docs/messaging-api/reference/#account-link-event

    Event object for when a user has linked his/her LINE account with a provider's service account.
    You can reply to account link events.
    If the link token has expired or has already been used,
    no webhook event will be sent and the user will be shown an error.
    """

    def __init__(self, mode=None, timestamp=None, source=None, reply_token=None, link=None,
                 **kwargs):
        """__init__ method.

        :param str mode: Channel state
        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param str reply_token: Reply token
        :param link: Link object
        :type link: :py:class:`linebot.models.events.Link`
        :param kwargs:
        """
        super(AccountLinkEvent, self).__init__(
            mode=mode, timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'accountLink'
        self.reply_token = reply_token
        self.link = self.get_or_new_from_json_dict(
            link, Link
        )


class ThingsEvent(Event):
    """Webhook ThingsEvent.

    https://developers.line.biz/en/reference/messaging-api/#device-link-event
    https://developers.line.biz/en/reference/messaging-api/#device-unlink-event
    https://developers.line.biz/en/reference/messaging-api/#scenario-result-event

    Event sent from LINE Things Webhook service.
    """

    def __init__(self, mode=None, timestamp=None, source=None, reply_token=None, things=None,
                 **kwargs):
        """__init__ method.

        :param str mode: Channel state
        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param str reply_token: Reply token
        :param things: Things object
        :type things: T <= :py:class:`linebot.models.things.Things`
        :param kwargs:
        """
        super(ThingsEvent, self).__init__(
            mode=mode, timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'things'
        self.reply_token = reply_token
        self.things = self.get_or_new_from_json_dict_with_types(
            things, {
                'link': DeviceLink,
                'unlink': DeviceUnlink,
                'scenarioResult': ScenarioResult,
            }
        )


class Postback(Base):
    """Postback.

    https://developers.line.biz/en/reference/messaging-api/#postback-event
    """

    def __init__(self, data=None, params=None, **kwargs):
        """__init__ method.

        :param str data: Postback data
        :param dict params: JSON object with the date and time
            selected by a user through a datetime picker action.
            Only returned for postback actions via the datetime picker.
        :param kwargs:
        """
        super(Postback, self).__init__(**kwargs)

        self.data = data
        self.params = params


class Beacon(Base):
    """Beacon.

    https://developers.line.biz/en/reference/messaging-api/#beacon-event
    """

    def __init__(self, type=None, hwid=None, dm=None, **kwargs):
        """__init__ method.

        :param str type: Type of beacon event
        :param str hwid: Hardware ID of the beacon that was detected
        :param str dm: Optional. Device message of beacon which is hex string
        :param kwargs:
        """
        super(Beacon, self).__init__(**kwargs)

        self.type = type
        self.hwid = hwid
        self.dm = dm

    @property
    def device_message(self):
        """Get dm(device_message) as bytearray.

        :rtype: bytearray
        """
        return bytearray.fromhex(self.dm) if self.dm is not None else None


class Joined(Base):
    """Joined.

    https://developers.line.biz/en/reference/messaging-api/#member-joined-event
    """

    def __init__(self, members=None, **kwargs):
        """__init__ method.

        :param dict members: Member of users who joined
        :param kwargs:
        """
        super(Joined, self).__init__(**kwargs)

        self._members = members

    @property
    def members(self):
        """Get members as list of SourceUser."""
        return [SourceUser(user_id=x['userId']) for x in self._members]


class Left(Base):
    """Left.

    https://developers.line.biz/en/reference/messaging-api/#member-left-event
    """

    def __init__(self, members=None, **kwargs):
        """__init__ method.

        :param dict members: Member of users who joined
        :param kwargs:
        """
        super(Left, self).__init__(**kwargs)

        self._members = members

    @property
    def members(self):
        """Get members as list of SourceUser."""
        return [SourceUser(user_id=x['userId']) for x in self._members]


class Link(Base):
    """Link.

    https://developers.line.me/en/docs/messaging-api/reference/#link-object
    """

    def __init__(self, result=None, nonce=None, **kwargs):
        """__init__ method.

        :param str result: Indicate whether the link was successful or not.
        :param str nonce: Specified nonce when verifying the user ID.
        """
        super(Link, self).__init__(**kwargs)

        self.result = result
        self.nonce = nonce
