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

from .base import Base
from .messages import (
    TextMessage,
    ImageMessage,
    VideoMessage,
    AudioMessage,
    LocationMessage,
    StickerMessage,
    FileMessage
)
from .sources import SourceUser, SourceGroup, SourceRoom


class Event(with_metaclass(ABCMeta, Base)):
    """Abstract Base Class of Webhook Event.

    https://devdocs.line.me/en/#webhook-event-object
    """

    def __init__(self, timestamp=None, source=None, **kwargs):
        """__init__ method.

        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param kwargs:
        """
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
    """Webhook MessageEvent.

    https://devdocs.line.me/en/#message-event

    Event object which contains the sent message.
    The message field contains a message object which corresponds with the message type.
    You can reply to message events.
    """

    def __init__(self, timestamp=None, source=None, reply_token=None, message=None, **kwargs):
        """__init__ method.

        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param str reply_token: Reply token
        :param message: Message object
        :type message: T <= :py:class:`linebot.models.messages.Message`
        :param kwargs:
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
                'sticker': StickerMessage,
                'file': FileMessage
            }
        )


class FollowEvent(Event):
    """Webhook FollowEvent.

    https://devdocs.line.me/en/#follow-event

    Event object for when your account is added as a friend (or unblocked).
    You can reply to follow events.
    """

    def __init__(self, timestamp=None, source=None, reply_token=None, **kwargs):
        """__init__ method.

        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param str reply_token: Reply token
        :param kwargs:
        """
        super(FollowEvent, self).__init__(
            timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'follow'
        self.reply_token = reply_token


class UnfollowEvent(Event):
    """Webhook UnfollowEvent.

    https://devdocs.line.me/en/#unfollow-event

    Event object for when your account is blocked.
    """

    def __init__(self, timestamp=None, source=None, **kwargs):
        """__init__ method.

        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param kwargs:
        """
        super(UnfollowEvent, self).__init__(
            timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'unfollow'


class JoinEvent(Event):
    """Webhook JoinEvent.

    https://devdocs.line.me/en/#join-event

    Event object for when your account joins a group or talk room.
    You can reply to join events.
    """

    def __init__(self, timestamp=None, source=None, reply_token=None, **kwargs):
        """__init__ method.

        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param str reply_token: Reply token
        :param kwargs:
        """
        super(JoinEvent, self).__init__(
            timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'join'
        self.reply_token = reply_token


class LeaveEvent(Event):
    """Webhook LeaveEvent.

    https://devdocs.line.me/en/#leave-event

    Event object for when your account leaves a group.
    """

    def __init__(self, timestamp=None, source=None, **kwargs):
        """__init__ method.

        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param kwargs:
        """
        super(LeaveEvent, self).__init__(
            timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'leave'


class PostbackEvent(Event):
    """Webhook PostbackEvent.

    https://devdocs.line.me/en/#postback-event

    Event object for when a user performs an action on
    a template message which initiates a postback.
    You can reply to postback events.
    """

    def __init__(self, timestamp=None, source=None, reply_token=None, postback=None, **kwargs):
        """__init__ method.

        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param str reply_token: Reply token
        :param postback: Postback object
        :type postback: :py:class:`linebot.models.events.Postback`
        :param kwargs:
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
    """Webhook BeaconEvent.

    https://devdocs.line.me/en/#beacon-event

    Event object for when a user detects a LINE Beacon. You can reply to beacon events.
    """

    def __init__(self, timestamp=None, source=None, reply_token=None,
                 beacon=None, **kwargs):
        """__init__ method.

        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param str reply_token: Reply token
        :param beacon: Beacon object
        :type beacon: :py:class:`linebot.models.events.Beacon`
        :param kwargs:
        """
        super(BeaconEvent, self).__init__(
            timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'beacon'
        self.reply_token = reply_token
        self.beacon = self.get_or_new_from_json_dict(
            beacon, Beacon
        )


class AccountLinkEvent(Event):
    """Webhook AccountLinkEvent.

    https://developers.line.me/en/docs/messaging-api/reference/#account-link-event

    Event object for when a user has linked his/her LINE account with a provider's service account.
    You can reply to account link events.
    If the link token has expired or has already been used,
    no webhook event will be sent and the user will be shown an error.
    """

    def __init__(self, timestamp=None, source=None, reply_token=None, link=None, **kwargs):
        """__init__ method.

        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param str reply_token: Reply token
        :param link: Link object
        :type link: :py:class:`linebot.models.events.Link`
        :param kwargs:
        """
        super(AccountLinkEvent, self).__init__(
            timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'accountLink'
        self.reply_token = reply_token
        self.link = self.get_or_new_from_json_dict(
            link, Link
        )


class Postback(Base):
    """Postback.

    https://devdocs.line.me/en/#postback-event
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

    https://devdocs.line.me/en/#beacon-event
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
        :return:
        """
        return bytearray.fromhex(self.dm) if self.dm is not None else None


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
