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

"""linebot.api module."""

import json

from .__about__ import __version__
from .exceptions import LineBotApiError
from .http_client import HttpClient, RequestsHttpClient
from .models import (
    Error, Profile, MemberIds, Content, RichMenuResponse, MessageQuotaResponse,
    MessageQuotaConsumptionResponse, IssueLinkTokenResponse, IssueChannelTokenResponse,
    MessageDeliveryBroadcastResponse, MessageDeliveryMulticastResponse,
    MessageDeliveryPushResponse, MessageDeliveryReplyResponse,
    InsightMessageDeliveryResponse, InsightFollowersResponse, InsightDemographicResponse,
    InsightMessageEventResponse, BroadcastResponse, NarrowcastResponse,
    MessageProgressNarrowcastResponse, BotInfo, GetWebhookResponse, TestWebhookResponse,
    AudienceGroup, ClickAudienceGroup, ImpAudienceGroup, GetAuthorityLevel, Audience,
    CreateAudienceGroup
)
from .models.responses import (
    Group, UserIds, RichMenuAliasResponse, RichMenuAliasListResponse, ChannelAccessTokens,
    IssueChannelTokenResponseV2, VerifyChannelTokenResponseV2, ValidAccessTokenKeyIDsResponse,
    InsightMessageEventOfCustomAggregationUnitResponse, AggregationInfoResponse,
    AggregationNameListResponse
)


class LineBotApi(object):
    """LineBotApi provides interface for LINE messaging API."""

    DEFAULT_API_ENDPOINT = 'https://api.line.me'
    DEFAULT_API_DATA_ENDPOINT = 'https://api-data.line.me'

    def __init__(self, channel_access_token,
                 endpoint=DEFAULT_API_ENDPOINT, data_endpoint=DEFAULT_API_DATA_ENDPOINT,
                 timeout=HttpClient.DEFAULT_TIMEOUT, http_client=RequestsHttpClient):
        """__init__ method.

        :param str channel_access_token: Your channel access token
        :param str endpoint: (optional) Default is https://api.line.me
        :param str data_endpoint: (optional) Default is https://api-data.line.me
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is linebot.http_client.HttpClient.DEFAULT_TIMEOUT
        :type timeout: float | tuple(float, float)
        :param http_client: (optional) Default is
            :py:class:`linebot.http_client.RequestsHttpClient`
        :type http_client: T <= :py:class:`linebot.http_client.HttpClient`
        """
        self.data_endpoint = data_endpoint
        self.endpoint = endpoint
        self.headers = {
            'Authorization': 'Bearer ' + channel_access_token,
            'User-Agent': 'line-bot-sdk-python/' + __version__
        }

        if http_client:
            self.http_client = http_client(timeout=timeout)
        else:
            self.http_client = RequestsHttpClient(timeout=timeout)

    def reply_message(self, reply_token, messages, notification_disabled=False, timeout=None):
        """Call reply message API.

        https://developers.line.biz/en/reference/messaging-api/#send-reply-message

        Respond to events from users, groups, and rooms.

        Webhooks are used to notify you when an event occurs.
        For events that you can respond to, a replyToken is issued for replying to messages.

        Because the replyToken becomes invalid after a certain period of time,
        responses should be sent as soon as a message is received.

        Reply tokens can only be used once.

        :param str reply_token: replyToken received via webhook
        :param messages: Messages.
            Max: 5
        :type messages: T <= :py:class:`linebot.models.send_messages.SendMessage` |
            list[T <= :py:class:`linebot.models.send_messages.SendMessage`]
        :param bool notification_disabled: (optional) True to disable push notification
            when the message is sent. The default value is False.
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        """
        if not isinstance(messages, (list, tuple)):
            messages = [messages]

        data = {
            'replyToken': reply_token,
            'messages': [message.as_json_dict() for message in messages],
            'notificationDisabled': notification_disabled,
        }

        self._post(
            '/v2/bot/message/reply', data=json.dumps(data), timeout=timeout
        )

    def push_message(
            self, to, messages,
            retry_key=None, notification_disabled=False,
            custom_aggregation_units=None, timeout=None):
        """Call push message API.

        https://developers.line.biz/en/reference/messaging-api/#send-push-message

        Send messages to users, groups, and rooms at any time.

        :param str to: ID of the receiver
        :param messages: Messages.
            Max: 5
        :type messages: T <= :py:class:`linebot.models.send_messages.SendMessage` |
            list[T <= :py:class:`linebot.models.send_messages.SendMessage`]
        :param retry_key: (optional) Arbitrarily generated UUID in hexadecimal notation.
        :param bool notification_disabled: (optional) True to disable push notification
            when the message is sent. The default value is False.
        :param custom_aggregation_units: (optional) Name of aggregation unit. Case-sensitive.
            Max unit: 1
            Max aggregation unit name length: 30 characters
            Supported character types: Half-width alphanumeric characters and underscore
        :type custom_aggregation_units: str | list[str]
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        """
        if not isinstance(messages, (list, tuple)):
            messages = [messages]

        if retry_key:
            self.headers['X-Line-Retry-Key'] = retry_key

        data = {
            'to': to,
            'messages': [message.as_json_dict() for message in messages],
            'notificationDisabled': notification_disabled,
        }

        if custom_aggregation_units is not None:
            if not isinstance(custom_aggregation_units, (list, tuple)):
                custom_aggregation_units = [custom_aggregation_units]
            data['customAggregationUnits'] = custom_aggregation_units

        self._post(
            '/v2/bot/message/push', data=json.dumps(data), timeout=timeout
        )

    def multicast(self, to, messages, retry_key=None, notification_disabled=False,
                  custom_aggregation_units=None, timeout=None):
        """Call multicast API.

        https://developers.line.biz/en/reference/messaging-api/#send-multicast-message

        Sends push messages to multiple users at any time.
        Messages cannot be sent to groups or rooms.

        :param to: IDs of the receivers
            Max: 150 users
        :type to: list[str]
        :param messages: Messages.
            Max: 5
        :type messages: T <= :py:class:`linebot.models.send_messages.SendMessage` |
            list[T <= :py:class:`linebot.models.send_messages.SendMessage`]
        :param retry_key: (optional) Arbitrarily generated UUID in hexadecimal notation.
        :param bool notification_disabled: (optional) True to disable push notification
            when the message is sent. The default value is False.
        :param custom_aggregation_units: (optional) Name of aggregation unit. Case-sensitive.
            Max unit: 1
            Max aggregation unit name length: 30 characters
            Supported character types: Half-width alphanumeric characters and underscore
        :type custom_aggregation_units: str | list[str]
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        """
        if not isinstance(messages, (list, tuple)):
            messages = [messages]

        if retry_key:
            self.headers['X-Line-Retry-Key'] = retry_key

        data = {
            'to': to,
            'messages': [message.as_json_dict() for message in messages],
            'notificationDisabled': notification_disabled,
        }

        if custom_aggregation_units is not None:
            if not isinstance(custom_aggregation_units, (list, tuple)):
                custom_aggregation_units = [custom_aggregation_units]
            data['customAggregationUnits'] = custom_aggregation_units

        self._post(
            '/v2/bot/message/multicast', data=json.dumps(data), timeout=timeout
        )

    def broadcast(self, messages, retry_key=None, notification_disabled=False, timeout=None):
        """Call broadcast API.

        https://developers.line.biz/en/reference/messaging-api/#send-broadcast-message

        Sends push messages to multiple users at any time.

        :param messages: Messages.
            Max: 5
        :type messages: T <= :py:class:`linebot.models.send_messages.SendMessage` |
            list[T <= :py:class:`linebot.models.send_messages.SendMessage`]
        :param retry_key: (optional) Arbitrarily generated UUID in hexadecimal notation.
        :param bool notification_disabled: (optional) True to disable push notification
            when the message is sent. The default value is False.
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.BroadcastResponse`
        """
        if not isinstance(messages, (list, tuple)):
            messages = [messages]

        if retry_key:
            self.headers['X-Line-Retry-Key'] = retry_key

        data = {
            'messages': [message.as_json_dict() for message in messages],
            'notificationDisabled': notification_disabled,
        }

        response = self._post(
            '/v2/bot/message/broadcast', data=json.dumps(data), timeout=timeout
        )

        return BroadcastResponse(request_id=response.headers.get('X-Line-Request-Id'))

    def narrowcast(
            self, messages,
            retry_key=None, recipient=None, filter=None, limit=None,
            notification_disabled=False, timeout=None):
        """Call narrowcast API.

        https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-message

        Sends push messages to multiple users at any time.
        Messages cannot be sent to groups or rooms.

        :param messages: Messages.
            Max: 5
        :type messages: T <= :py:class:`linebot.models.send_messages.SendMessage` |
            list[T <= :py:class:`linebot.models.send_messages.SendMessage`]
        :param retry_key: (optional) Arbitrarily generated UUID in hexadecimal notation.
        :param recipient: audience object of recipient
        :type recipient: T <= :py:class:`linebot.models.recipient.AudienceRecipient`
        :param filter: demographic filter of recipient
        :type filter: T <= :py:class:`linebot.models.filter.DemographicFilter`
        :param limit: limit on this narrowcast
        :type limit: T <= :py:class:`linebot.models.limit.Limit`
        :param bool notification_disabled: (optional) True to disable push notification
            when the message is sent. The default value is False.
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.NarrowcastResponse`
        """
        if not isinstance(messages, (list, tuple)):
            messages = [messages]

        if retry_key:
            self.headers['X-Line-Retry-Key'] = retry_key

        data = {
            'messages': [message.as_json_dict() for message in messages],
            'recipient': recipient.as_json_dict(),
            'filter': filter.as_json_dict(),
            'limit': limit.as_json_dict(),
            'notificationDisabled': notification_disabled,
        }

        response = self._post(
            '/v2/bot/message/narrowcast', data=json.dumps(data), timeout=timeout
        )

        return NarrowcastResponse(request_id=response.headers.get('X-Line-Request-Id'))

    def get_progress_status_narrowcast(self, request_id, timeout=None):
        """Get progress status of narrowcast messages sent.

        https://developers.line.biz/en/reference/messaging-api/#get-narrowcast-progress-status

        Gets the number of messages sent with the /bot/message/progress/narrowcast endpoint.

        :param str request_id: request ID of narrowcast.
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.MessageDeliveryBroadcastResponse`
        """
        response = self._get(
            '/v2/bot/message/progress/narrowcast?requestId={request_id}'.format(
                request_id=request_id),
            timeout=timeout
        )

        return MessageProgressNarrowcastResponse.new_from_json_dict(response.json)

    def get_message_delivery_broadcast(self, date, timeout=None):
        """Get number of sent broadcast messages.

        https://developers.line.biz/en/reference/messaging-api/#get-number-of-broadcast-messages

        Gets the number of messages sent with the /bot/message/broadcast endpoint.

        :param str date: Date the messages were sent. The format is `yyyyMMdd` (Timezone is UTC+9).
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.MessageDeliveryBroadcastResponse`
        """
        response = self._get(
            '/v2/bot/message/delivery/broadcast?date={date}'.format(date=date),
            timeout=timeout
        )

        return MessageDeliveryBroadcastResponse.new_from_json_dict(response.json)

    def get_message_delivery_reply(self, date, timeout=None):
        """Get number of sent reply messages.

        https://developers.line.biz/en/reference/messaging-api/#get-number-of-reply-messages

        Gets the number of messages sent with the /bot/message/reply endpoint.

        :param str date: Date the messages were sent. The format is `yyyyMMdd` (Timezone is UTC+9).
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.MessageDeliveryReplyResponse`
        """
        response = self._get(
            '/v2/bot/message/delivery/reply?date={date}'.format(date=date),
            timeout=timeout
        )

        return MessageDeliveryReplyResponse.new_from_json_dict(response.json)

    def get_message_delivery_push(self, date, timeout=None):
        """Get number of sent push messages.

        https://developers.line.biz/en/reference/messaging-api/#get-number-of-push-messages

        Gets the number of messages sent with the /bot/message/push endpoint.

        :param str date: Date the messages were sent. The format is `yyyyMMdd` (Timezone is UTC+9).
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.MessageDeliveryPushResponse`
        """
        response = self._get(
            '/v2/bot/message/delivery/push?date={date}'.format(date=date),
            timeout=timeout
        )

        return MessageDeliveryPushResponse.new_from_json_dict(response.json)

    def get_message_delivery_multicast(self, date, timeout=None):
        """Get number of sent multicast messages.

        https://developers.line.biz/en/reference/messaging-api/#get-number-of-multicast-messages

        Gets the number of messages sent with the /bot/message/multicast endpoint.

        :param str date: Date the messages were sent. The format is `yyyyMMdd` (Timezone is UTC+9).
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.MessageDeliveryMulticastResponse`
        """
        response = self._get(
            '/v2/bot/message/delivery/multicast?date={date}'.format(date=date),
            timeout=timeout
        )

        return MessageDeliveryMulticastResponse.new_from_json_dict(response.json)

    def get_profile(self, user_id, timeout=None):
        """Call get profile API.

        https://developers.line.biz/en/reference/messaging-api/#get-profile

        Get user profile information.

        :param str user_id: User ID
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.Profile`
        :return: Profile instance
        """
        response = self._get(
            '/v2/bot/profile/{user_id}'.format(user_id=user_id),
            timeout=timeout
        )

        return Profile.new_from_json_dict(response.json)

    def get_group_summary(self, group_id, timeout=None):
        """Call get group summary API.

        https://developers.line.biz/en/reference/messaging-api/#get-group-summary

        Gets the group ID, group name, and group icon URL of a group
        where the LINE Official Account is a member.

        :param str group_id: Group ID
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.Group`
        :return: Profile instance
        """
        response = self._get(
            '/v2/bot/group/{group_id}/summary'.format(group_id=group_id),
            timeout=timeout
        )

        return Group.new_from_json_dict(response.json)

    def get_group_members_count(self, group_id, timeout=None):
        """Call get members in group count API.

        https://developers.line.biz/en/reference/messaging-api/#get-members-group-count

        Gets the count of members in a group.

        :param str group_id: Group ID
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.Group`
        :return: Profile instance
        """
        response = self._get(
            '/v2/bot/group/{group_id}/members/count'.format(group_id=group_id),
            timeout=timeout
        )

        return response.json.get('count')

    def get_room_members_count(self, room_id, timeout=None):
        """Call get members in room count API.

        https://developers.line.biz/en/reference/messaging-api/#get-members-room-count

        Gets the count of members in a room.

        :param str room_id: Room ID
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.Group`
        :return: Profile instance
        """
        response = self._get(
            '/v2/bot/room/{room_id}/members/count'.format(room_id=room_id),
            timeout=timeout
        )

        return response.json.get('count')

    def get_group_member_profile(self, group_id, user_id, timeout=None):
        """Call get group member profile API.

        https://developers.line.biz/en/reference/messaging-api/#get-group-member-profile

        Gets the user profile of a member of a group that
        the bot is in. This can be the user ID of a user who has
        not added the bot as a friend or has blocked the bot.

        :param str group_id: Group ID
        :param str user_id: User ID
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.Profile`
        :return: Profile instance
        """
        response = self._get(
            '/v2/bot/group/{group_id}/member/{user_id}'.format(group_id=group_id, user_id=user_id),
            timeout=timeout
        )

        return Profile.new_from_json_dict(response.json)

    def get_room_member_profile(self, room_id, user_id, timeout=None):
        """Call get room member profile API.

        https://developers.line.biz/en/reference/messaging-api/#get-room-member-profile

        Gets the user profile of a member of a room that
        the bot is in. This can be the user ID of a user who has
        not added the bot as a friend or has blocked the bot.

        :param str room_id: Room ID
        :param str user_id: User ID
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.Profile`
        :return: Profile instance
        """
        response = self._get(
            '/v2/bot/room/{room_id}/member/{user_id}'.format(room_id=room_id, user_id=user_id),
            timeout=timeout
        )

        return Profile.new_from_json_dict(response.json)

    def get_group_member_ids(self, group_id, start=None, timeout=None):
        """Call get group member IDs API.

        https://developers.line.biz/en/reference/messaging-api/#get-group-member-ids

        Gets the user IDs of the members of a group that the bot is in.
        This includes the user IDs of users who have not added the bot as a friend
        or has blocked the bot.

        :param str group_id: Group ID
        :param str start: continuationToken
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.MemberIds`
        :return: MemberIds instance
        """
        params = None if start is None else {'start': start}

        response = self._get(
            '/v2/bot/group/{group_id}/members/ids'.format(group_id=group_id),
            params=params,
            timeout=timeout
        )

        return MemberIds.new_from_json_dict(response.json)

    def get_room_member_ids(self, room_id, start=None, timeout=None):
        """Call get room member IDs API.

        https://developers.line.biz/en/reference/messaging-api/#get-room-member-ids

        Gets the user IDs of the members of a group that the bot is in.
        This includes the user IDs of users who have not added the bot as a friend
        or has blocked the bot.

        :param str room_id: Room ID
        :param str start: continuationToken
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.MemberIds`
        :return: MemberIds instance
        """
        params = None if start is None else {'start': start}

        response = self._get(
            '/v2/bot/room/{room_id}/members/ids'.format(room_id=room_id),
            params=params,
            timeout=timeout
        )

        return MemberIds.new_from_json_dict(response.json)

    def get_message_content(self, message_id, timeout=None):
        """Call get content API.

        https://developers.line.biz/en/reference/messaging-api/#get-content

        Retrieve image, video, and audio data sent by users.

        :param str message_id: Message ID
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.Content`
        :return: Content instance
        """
        response = self._get(
            '/v2/bot/message/{message_id}/content'.format(message_id=message_id),
            endpoint=self.data_endpoint, stream=True, timeout=timeout
        )

        return Content(response)

    def leave_group(self, group_id, timeout=None):
        """Call leave group API.

        https://developers.line.biz/en/reference/messaging-api/#leave-group

        Leave a group.

        :param str group_id: Group ID
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        """
        self._post(
            '/v2/bot/group/{group_id}/leave'.format(group_id=group_id),
            timeout=timeout
        )

    def leave_room(self, room_id, timeout=None):
        """Call leave room API.

        https://developers.line.biz/en/reference/messaging-api/#leave-room

        Leave a room.

        :param str room_id: Room ID
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        """
        self._post(
            '/v2/bot/room/{room_id}/leave'.format(room_id=room_id),
            timeout=timeout
        )

    def get_rich_menu(self, rich_menu_id, timeout=None):
        """Call get rich menu API.

        https://developers.line.biz/en/reference/messaging-api/#get-rich-menu

        :param str rich_menu_id: ID of the rich menu
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.RichMenuResponse`
        :return: RichMenuResponse instance
        """
        response = self._get(
            '/v2/bot/richmenu/{rich_menu_id}'.format(rich_menu_id=rich_menu_id),
            timeout=timeout
        )

        return RichMenuResponse.new_from_json_dict(response.json)

    def get_rich_menu_alias(self, rich_menu_alias_id=None, timeout=None):
        """Call get rich menu alias API.

        https://developers.line.biz/en/reference/messaging-api/#get-rich-menu-alias-by-id

        :param str rich_menu_alias_id: ID of an uploaded rich menu alias.
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.RichMenuAliasResponse`
        :return: RichMenuAliasResponse instance
        """
        response = self._get(
            '/v2/bot/richmenu/alias/{rich_menu_id}'.format(rich_menu_id=rich_menu_alias_id),
            timeout=timeout
        )
        return RichMenuAliasResponse.new_from_json_dict(response.json)

    def get_rich_menu_alias_list(self, timeout=None):
        """Call get rich menu alias list API.

        https://developers.line.biz/en/reference/messaging-api/#update-rich-menu-alias

        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.RichMenuAliasListResponse`
        :return: RichMenuAliasListResponse instance
        """
        response = self._get(
            '/v2/bot/richmenu/alias/list',
            timeout=timeout
        )
        return RichMenuAliasListResponse.new_from_json_dict(response.json)

    def create_rich_menu(self, rich_menu, timeout=None):
        """Call create rich menu API.

        https://developers.line.biz/en/reference/messaging-api/#create-rich-menu

        :param rich_menu: Inquired to create a rich menu object.
        :type rich_menu: T <= :py:class:`linebot.models.rich_menu.RichMenu`
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: str
        :return: rich menu id
        """
        response = self._post(
            '/v2/bot/richmenu', data=rich_menu.as_json_string(), timeout=timeout
        )

        return response.json.get('richMenuId')

    def create_rich_menu_alias(self, rich_menu_alias, timeout=None):
        """Call create rich menu alias API.

        https://developers.line.biz/en/reference/messaging-api/#create-rich-menu-alias

        :param rich_menu_alias: Inquired to create a rich menu alias object.
        :type rich_menu_alias: T <= :py:class:`linebot.models.rich_menu.RichMenuAlias`
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: str
        :return: rich menu id
        """
        self._post(
            '/v2/bot/richmenu/alias', data=rich_menu_alias.as_json_string(), timeout=timeout
        )

    def update_rich_menu_alias(self, rich_menu_alias_id, rich_menu_alias, timeout=None):
        """Call update rich menu alias API.

        https://developers.line.biz/en/reference/messaging-api/#update-rich-menu-alias

        :param str rich_menu_alias_id: ID of an uploaded rich menu alias.
        :param rich_menu_alias: Inquired to create a rich menu alias object.
        :type rich_menu_alias: T <= :py:class:`linebot.models.rich_menu.RichMenuAlias`
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: str
        :return: rich menu id
        """
        self._post(
            '/v2/bot/richmenu/alias/{rich_menu_id}'.format(rich_menu_id=rich_menu_alias_id),
            data=rich_menu_alias.as_json_string(),
            timeout=timeout
        )

    def delete_rich_menu(self, rich_menu_id, timeout=None):
        """Call delete rich menu API.

        https://developers.line.biz/en/reference/messaging-api/#delete-rich-menu

        :param str rich_menu_id: ID of an uploaded rich menu
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        """
        self._delete(
            '/v2/bot/richmenu/{rich_menu_id}'.format(rich_menu_id=rich_menu_id),
            timeout=timeout
        )

    def delete_rich_menu_alias(self, rich_menu_alias_id, timeout=None):
        """Call delete rich menu alias API.

        https://developers.line.biz/en/reference/messaging-api/#delete-rich-menu-alias

        :param str rich_menu_alias_id: ID of an uploaded rich menu alias.
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        """
        self._delete(
            '/v2/bot/richmenu/alias/{rich_menu_alias_id}'.format(
                rich_menu_alias_id=rich_menu_alias_id),
            timeout=timeout
        )

    def get_rich_menu_id_of_user(self, user_id, timeout=None):
        """Call get rich menu ID of user API.

        https://developers.line.biz/en/reference/messaging-api/#get-rich-menu-id-of-user

        :param str user_id: IDs of the user
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: str
        :return: rich menu id
        """
        response = self._get(
            '/v2/bot/user/{user_id}/richmenu'.format(user_id=user_id),
            timeout=timeout
        )

        return response.json.get('richMenuId')

    def link_rich_menu_to_user(self, user_id, rich_menu_id, timeout=None):
        """Call link rich menu to user API.

        https://developers.line.biz/en/reference/messaging-api/#link-rich-menu-to-user

        :param str user_id: ID of the user
        :param str rich_menu_id: ID of an uploaded rich menu
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        """
        self._post(
            '/v2/bot/user/{user_id}/richmenu/{rich_menu_id}'.format(
                user_id=user_id,
                rich_menu_id=rich_menu_id
            ),
            timeout=timeout
        )

    def link_rich_menu_to_users(self, user_ids, rich_menu_id, timeout=None):
        """Links a rich menu to multiple users.

        https://developers.line.biz/en/reference/messaging-api/#link-rich-menu-to-users

        :param user_ids: user IDs
            Max: 150 users
        :type user_ids: list[str]
        :param str rich_menu_id: ID of an uploaded rich menu
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        """
        self._post(
            '/v2/bot/richmenu/bulk/link',
            data=json.dumps({
                'userIds': user_ids,
                'richMenuId': rich_menu_id,
            }),
            timeout=timeout
        )

    def unlink_rich_menu_from_user(self, user_id, timeout=None):
        """Call unlink rich menu from user API.

        https://developers.line.biz/en/reference/messaging-api#unlink-rich-menu-from-user

        :param str user_id: ID of the user
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        """
        self._delete(
            '/v2/bot/user/{user_id}/richmenu'.format(user_id=user_id),
            timeout=timeout
        )

    def unlink_rich_menu_from_users(self, user_ids, timeout=None):
        """Unlinks rich menus from multiple users.

        https://developers.line.biz/en/reference/messaging-api/#unlink-rich-menu-from-users

        :param user_ids: user IDs
            Max: 150 users
        :type user_ids: list[str]
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        """
        self._post(
            '/v2/bot/richmenu/bulk/unlink',
            data=json.dumps({
                'userIds': user_ids,
            }),
            timeout=timeout
        )

    def get_rich_menu_image(self, rich_menu_id, timeout=None):
        """Call download rich menu image API.

        https://developers.line.biz/en/reference/messaging-api#download-rich-menu-image

        :param str rich_menu_id: ID of the rich menu with the image to be downloaded
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.Content`
        :return: Content instance
        """
        response = self._get(
            '/v2/bot/richmenu/{rich_menu_id}/content'.format(rich_menu_id=rich_menu_id),
            endpoint=self.data_endpoint, timeout=timeout
        )

        return Content(response)

    def set_rich_menu_image(self, rich_menu_id, content_type, content, timeout=None):
        """Call upload rich menu image API.

        https://developers.line.me/en/docs/messaging-api/reference/#upload-rich-menu-image

        Uploads and attaches an image to a rich menu.

        :param str rich_menu_id: IDs of the richmenu
        :param str content_type: image/jpeg or image/png
        :param content: image content as bytes, or file-like object
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        """
        self._post(
            '/v2/bot/richmenu/{rich_menu_id}/content'.format(rich_menu_id=rich_menu_id),
            endpoint=self.data_endpoint,
            data=content,
            headers={'Content-Type': content_type},
            timeout=timeout
        )

    def get_rich_menu_list(self, timeout=None):
        """Call get rich menu list API.

        https://developers.line.me/en/docs/messaging-api/reference/#get-rich-menu-list

        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: list(T <= :py:class:`linebot.models.responses.RichMenuResponse`)
        :return: list[RichMenuResponse] instance
        """
        response = self._get(
            '/v2/bot/richmenu/list',
            timeout=timeout
        )

        result = []
        for richmenu in response.json['richmenus']:
            result.append(RichMenuResponse.new_from_json_dict(richmenu))

        return result

    def set_default_rich_menu(self, rich_menu_id, timeout=None):
        """Set the default rich menu.

        https://developers.line.biz/en/reference/messaging-api/#set-default-rich-menu

        :param str rich_menu_id: ID of an uploaded rich menu
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        """
        self._post(
            '/v2/bot/user/all/richmenu/{rich_menu_id}'.format(
                rich_menu_id=rich_menu_id,
            ),
            timeout=timeout
        )

    def get_default_rich_menu(self, timeout=None):
        """Get the ID of the default rich menu set with the Messaging API.

        https://developers.line.biz/en/reference/messaging-api/#get-default-rich-menu-id

        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        """
        response = self._get(
            '/v2/bot/user/all/richmenu',
            timeout=timeout
        )

        return response.json.get('richMenuId')

    def cancel_default_rich_menu(self, timeout=None):
        """Cancel the default rich menu set with the Messaging API.

        https://developers.line.biz/en/reference/messaging-api/#cancel-default-rich-menu

        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        """
        self._delete(
            '/v2/bot/user/all/richmenu',
            timeout=timeout
        )

    def get_message_quota(self, timeout=None):
        """Call Get the target limit for additional messages.

        https://developers.line.biz/en/reference/messaging-api/#get-quota

        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.MessageQuotaResponse`
        :return: MessageQuotaResponse instance
        """
        response = self._get(
            '/v2/bot/message/quota',
            timeout=timeout
        )

        return MessageQuotaResponse.new_from_json_dict(response.json)

    def get_message_quota_consumption(self, timeout=None):
        """Get number of messages sent this month.

        https://developers.line.biz/en/reference/messaging-api/#get-consumption

        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.MessageQuotaConsumptionResponse`
        :return: MessageQuotaConsumptionResponse instance
        """
        response = self._get(
            '/v2/bot/message/quota/consumption',
            timeout=timeout
        )

        return MessageQuotaConsumptionResponse.new_from_json_dict(response.json)

    def issue_link_token(self, user_id, timeout=None):
        """Issues a link token used for the account link feature.

        https://developers.line.biz/en/reference/messaging-api/#issue-link-token

        :param str user_id: User ID for the LINE account to be linked
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.IssueLinkTokenResponse`
        :return: IssueLinkTokenResponse instance
        """
        response = self._post(
            '/v2/bot/user/{user_id}/linkToken'.format(
                user_id=user_id
            ),
            timeout=timeout
        )

        return IssueLinkTokenResponse.new_from_json_dict(response.json)

    def issue_channel_token(self, client_id, client_secret,
                            grant_type='client_credentials', timeout=None):
        """Issues a short-lived channel access token.

        https://developers.line.biz/en/reference/messaging-api/#issue-channel-access-token

        :param str client_id: Channel ID.
        :param str client_secret: Channel secret.
        :param str grant_type: `client_credentials`
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.IssueChannelTokenResponse`
        :return: IssueChannelTokenResponse instance
        """
        response = self._post(
            '/v2/oauth/accessToken',
            data={
                'client_id': client_id,
                'client_secret': client_secret,
                'grant_type': grant_type,
            },
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            timeout=timeout
        )

        return IssueChannelTokenResponse.new_from_json_dict(response.json)

    def revoke_channel_token(self, access_token, timeout=None):
        """Revokes a channel access token.

        https://developers.line.biz/en/reference/messaging-api/#revoke-channel-access-token

        :param str access_token: Channel access token.
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        """
        self._post(
            '/v2/oauth/revoke',
            data={'access_token': access_token},
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            timeout=timeout
        )

    def get_insight_message_delivery(self, date, timeout=None):
        """Get the number of messages sent on a specified day.

        https://developers.line.biz/en/reference/messaging-api/#get-number-of-delivery-messages

        :param str date: Date for which to retrieve number of sent messages.
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.InsightMessageDeliveryResponse`
        """
        response = self._get(
            '/v2/bot/insight/message/delivery?date={date}'.format(date=date),
            timeout=timeout
        )

        return InsightMessageDeliveryResponse.new_from_json_dict(response.json)

    def get_insight_followers(self, date, timeout=None):
        """Get the number of users who have added the bot on or before a specified date.

        https://developers.line.biz/en/reference/messaging-api/#get-number-of-followers

        :param str date: Date for which to retrieve the number of followers.
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.InsightFollowersResponse`
        """
        response = self._get(
            '/v2/bot/insight/followers?date={date}'.format(date=date),
            timeout=timeout
        )

        return InsightFollowersResponse.new_from_json_dict(response.json)

    def get_insight_demographic(self, timeout=None):
        """Retrieve the demographic attributes for a bot's friends.

        https://developers.line.biz/en/reference/messaging-api/#get-demographic

        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.InsightDemographicResponse`
        """
        response = self._get(
            '/v2/bot/insight/demographic',
            timeout=timeout
        )

        return InsightDemographicResponse.new_from_json_dict(response.json)

    def get_insight_message_event(self, request_id, timeout=None):
        """Return statistics about how users interact with broadcast messages.

        https://developers.line.biz/en/reference/messaging-api/#get-message-event

        :param str request_id: Request ID of broadcast message.
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.InsightMessageEventResponse`
        """
        response = self._get(
            '/v2/bot/insight/message/event?requestId={request_id}'.format(request_id=request_id),
            timeout=timeout
        )

        return InsightMessageEventResponse.new_from_json_dict(response.json)

    def get_bot_info(self, timeout=None):
        """Get a bot's basic information.

        https://developers.line.biz/en/reference/messaging-api/#get-bot-info

        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.BotInfo`
        """
        response = self._get(
            '/v2/bot/info',
            timeout=timeout
        )

        return BotInfo.new_from_json_dict(response.json)

    def create_audience_group(self, audience_group_name, audiences=[],
                              is_ifa=False, timeout=None):
        """Create an audience group.

        https://developers.line.biz/en/reference/messaging-api/#create-upload-audience-group

        :param str audience_group_name: The audience's name
        :param list audiences: An array of user IDs or IFAs
        :param bool is_ifa: true | false
        :return: audience group id
        """
        if audiences:
            audiences = [Audience.new_from_json_dict(audience) for audience in audiences]
        response = self._post(
            '/v2/bot/audienceGroup/upload',
            data=json.dumps({
                "description": audience_group_name,
                "isIfaAudience": is_ifa,
                "audiences": [audience.as_json_dict() for audience in audiences],
            }),
            timeout=timeout
        )

        return CreateAudienceGroup.new_from_json_dict(response.json)

    def get_audience_group(self, audience_group_id, timeout=None):
        """Get the object of audience group.

        https://developers.line.biz/en/reference/messaging-api/#get-audience-group

        :param str audience_group_id: The audience ID
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :return: AudienceGroup instance
        """
        response = self._get(
            '/v2/bot/audienceGroup/{audience_group_id}'.format(
                audience_group_id=audience_group_id),
            timeout=timeout
        )

        return AudienceGroup.new_from_json_dict(response.json)

    def get_audience_group_list(self, page=1, description=None, status=None, size=20,
                                include_external_public_group=None, create_route=None,
                                timeout=None):
        """Get data for more than one audience.

        https://developers.line.biz/en/reference/messaging-api/#get-audience-groups

        :param int page: The page to return when getting (paginated) results. Must be 1 or higher
        :param str description: The name of the audience(s) to return
        :param str status: IN_PROGRESS | READY | FAILED | EXPIRED
        :param int size: The number of audiences per page. Default: 20, Max: 40
        :param bool include_external_public_group: true | false
        :param str create_route: How the audience was created.
        :type create_route: OA_MANAGER | MESSAGING_API
        :return: AudienceGroup instance
        """
        params = {}
        if page:
            params["page"] = page
        if description:
            params["description"] = description
        if status:
            params["status"] = status
        if size:
            params["size"] = size
        if include_external_public_group:
            params["includesExternalPublicGroup"] = include_external_public_group
        if create_route:
            params["createRoute"] = create_route
        response = self._get(
            '/v2/bot/audienceGroup/list?',
            params=params,
            timeout=timeout
        )
        result = []
        for audience_group in response.json.get('audienceGroups', []):
            result.append(AudienceGroup.new_from_json_dict(audience_group))
        if response.json.get('hasNextPage', False):
            result += self.get_audience_group_list(page + 1, description, status, size,
                                                   include_external_public_group,
                                                   create_route, timeout)
        return result

    def delete_audience_group(self, audience_group_id, timeout=None):
        """Delete an existing audience.

        https://developers.line.biz/en/reference/messaging-api/#delete-audience-group

        :param str audience_group_id: The audience ID
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        """
        self._delete(
            '/v2/bot/audienceGroup/{}'.format(audience_group_id),
            timeout=timeout
        )

    def rename_audience_group(self, audience_group_id, description, timeout=None):
        """Modify the name of an existing audience.

        https://developers.line.biz/en/reference/messaging-api/#set-description-audience-group

        :param str audience_group_id: The audience ID
        :param str description: The new audience's name
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        """
        self._put(
            '/v2/bot/audienceGroup/{audience_group_id}/updateDescription'.format(
                audience_group_id=audience_group_id),
            data=json.dumps({
                "description": description,
            }),
            timeout=timeout
        )

        return ''

    def add_audiences_to_audience_group(self, audience_group_id, audiences,
                                        upload_description=None, timeout=None):
        """Add new user IDs or IFAs to an audience for uploading user IDs.

        https://developers.line.biz/en/reference/messaging-api/#update-upload-audience-group

        :param str audience_group_id: The audience ID
        :param list audiences: An array of user IDs or IFAs
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :param bool is_ifa: If this is false (default), recipients are specified by user IDs.
            If true, recipients must be specified by IFAs.
        :param str upload_description: The description to register for the job
        :type timeout: float | tuple(float, float)
        """
        if audiences:
            audiences = [Audience.new_from_json_dict(audience) for audience in audiences]
        response = self._put(
            '/v2/bot/audienceGroup/upload',
            data=json.dumps({
                "audienceGroupId": audience_group_id,
                "audiences": [audience.as_json_dict() for audience in audiences],
                "uploadDescription": upload_description,
            }),
            timeout=timeout
        )

        return response.json

    def get_audience_group_authority_level(self, timeout=None):
        """Get the authority level of the audience.

        https://developers.line.biz/en/reference/messaging-api/#get-authority-level

        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :return: json
        """
        response = self._get(
            '/v2/bot/audienceGroup/authorityLevel',
            timeout=timeout
        )

        return GetAuthorityLevel.new_from_json_dict(response.json)

    def change_audience_group_authority_level(self, authority_level='PUBLIC', timeout=None):
        """Change the authority level of all audiences created in the same channel.

        https://developers.line.biz/en/reference/messaging-api/#change-authority-level

        :param str authority_level: PUBLIC | PRIVATE.
        """
        self._put(
            '/v2/bot/audienceGroup/authorityLevel',
            data=json.dumps({
                "authorityLevel": authority_level,
            }),
            timeout=timeout
        )

        return ''

    def create_click_audience_group(self, description, request_id,
                                    click_url=None, timeout=None):
        """Create an audience for click-based retargeting.

        https://developers.line.biz/en/reference/messaging-api/#create-click-audience-group

        :param str description: The audience's name. Audience names must be unique.
        :param str request_id: The request ID of a message sent in the past 60 days.
        :param str click_url: The URL clicked by the user.
        If empty, users who clicked any URL in the message are added to the list of recipients.
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :return: ClickAudienceGroup instance
        """
        response = self._post(
            '/v2/bot/audienceGroup/click',
            data=json.dumps({
                "description": description,
                "requestId": request_id,
                "clickUrl": click_url,
            }),
            timeout=timeout
        )

        return ClickAudienceGroup.new_from_json_dict(response.json)

    def create_imp_audience_group(self, description, request_id,
                                  timeout=None):
        """Create an audience for impression-based retargeting.

        https://developers.line.biz/en/reference/messaging-api/#create-imp-audience-group

        :param str description: The audience's name. Audience names must be unique.
        :param str request_id: The request ID of a  message sent in the past 60 days.
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :return: ImpAudienceGroup instance
        """
        response = self._post(
            '/v2/bot/audienceGroup/imp',
            data=json.dumps({
                "description": description,
                "requestId": request_id,
            }),
            timeout=timeout
        )

        return ImpAudienceGroup.new_from_json_dict(response.json)

    def set_webhook_endpoint(self, webhook_endpoint, timeout=None):
        """Set the webhook endpoint URL.

        https://developers.line.biz/en/reference/messaging-api/#set-webhook-endpoint-url

        :param str webhook_endpoint: A valid webhook URL to be set.
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: dict
        :return: Empty dict.
        """
        data = {
            'endpoint': webhook_endpoint
        }

        response = self._put(
            '/v2/bot/channel/webhook/endpoint',
            data=json.dumps(data),
            timeout=timeout,
        )

        return response.json

    def get_webhook_endpoint(self, timeout=None):
        """Get information on a webhook endpoint.

        https://developers.line.biz/en/reference/messaging-api/#get-webhook-endpoint-information

        :rtype: :py:class:`linebot.models.responses.GetWebhookResponse`
        :return: Webhook information, including `endpoint` for webhook
            URL and `active` for webhook usage status.
        """
        response = self._get(
            '/v2/bot/channel/webhook/endpoint',
            timeout=timeout,
        )

        return GetWebhookResponse.new_from_json_dict(response.json)

    def test_webhook_endpoint(self, webhook_endpoint=None, timeout=None):
        """Checks if the configured webhook endpoint can receive a test webhook event.

        https://developers.line.biz/en/reference/messaging-api/#test-webhook-endpoint

        :param webhook_endpoint: (optional) Set this parameter to
            specific the webhook endpoint of the webhook. Default is the webhook
            endpoint that is already set to the channel.
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.TestWebhookResponse`
        """
        data = {}

        if webhook_endpoint is not None:
            data['endpoint'] = webhook_endpoint

        response = self._post(
            '/v2/bot/channel/webhook/test',
            data=json.dumps(data),
            timeout=timeout,
        )

        return TestWebhookResponse.new_from_json_dict(response.json)

    def get_followers_ids(self, limit=300, start=None, timeout=None):
        """Get a list of users who added your LINE Official Account as a friend.

        https://developers.line.biz/en/reference/messaging-api/#get-follower-ids

        :param int limit: The maximum number of user IDs to retrieve in a single request.
            The default value is 300.
        :param str start: Get the next array of user IDs.
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.UserIds`
        """
        params = {'limit': limit} if start is None else {'limit': limit, 'start': start}

        response = self._get(
            '/v2/bot/followers/ids',
            params=params,
            timeout=timeout
        )

        return UserIds.new_from_json_dict(response.json)

    def issue_channel_access_token_v2_1(
            self, client_assertion, grant_type='client_credentials',
            client_assertion_type='urn:ietf:params:oauth:client-assertion-type:jwt-bearer',
            timeout=None):
        """Issues a channel access token v2.1.

        https://developers.line.biz/en/reference/messaging-api/#issue-channel-access-token-v2-1

        :param str client_assertion: Client assertion.
        :param str grant_type: `client_credentials`
        :param str client_assertion_type: `urn:ietf:params:oauth:client-assertion-type:jwt-bearer`.
        :param timeout: (optional) How long to wait for the server
        to send data before giving up, as a float,
        or a (connect timeout, read timeout) float tuple.
        Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.IssueChannelTokenResponseV2`
        """
        response = self._post(
            '/oauth2/v2.1/token',
            data={
                'grant_type': grant_type,
                'client_assertion_type': client_assertion_type,
                'client_assertion': client_assertion,
            },
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            timeout=timeout
        )

        return IssueChannelTokenResponseV2.new_from_json_dict(response.json)

    def revoke_channel_access_token_v2_1(
             self, client_id,
             client_secret, access_token,
             timeout=None):
        """Revokes a channel access token v2.1.

        https://developers.line.biz/en/reference/messaging-api/#revoke-channel-access-token-v2-1

        :param str client_id: Client id.
        :param str client_secret: Channel secret.
        :param str access_token: Channel access token.
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        """
        self._post(
            '/oauth2/v2.1/revoke',
            data={'client_id': client_id,
                  'client_secret': client_secret,
                  'access_token': access_token},
            timeout=timeout
        )

    def get_channel_access_tokens_v2_1(
            self, client_assertion,
            client_assertion_type='urn:ietf:params:oauth:client-assertion-type:jwt-bearer',
            timeout=None):
        """Get issued channel access tokens v2.1.

        https://developers.line.biz/en/reference/messaging-api/#get-issued-channel-access-tokens-v2-1

        :param str client_assertion: Client assertion.
        :param str client_assertion_type: `urn:ietf:params:oauth:client-assertion-type:jwt-bearer`.
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.ChannelAccessTokens`
        """
        response = self._get(
            '/oauth2/v2.1/tokens',
            params={'client_assertion': client_assertion,
                    'client_assertion_type': client_assertion_type},
            timeout=timeout
        )
        return ChannelAccessTokens.new_from_json_dict(response.json)

    def verify_channel_access_token_v2_1(self, access_token, timeout=None):
        """Validate channel access token v2.1.

        https://developers.line.biz/en/reference/messaging-api/#verfiy-channel-access-token-v2-1

        :param str access_token: Channel access token.
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.VerifyChannelTokenResponseV2`
        """
        response = self._get('/oauth2/v2.1/verify',
                             params={'access_token': access_token},
                             timeout=timeout)
        return VerifyChannelTokenResponseV2.new_from_json_dict(response.json)

    def get_channel_token_key_ids_v2_1(
           self, client_assertion,
           client_assertion_type='urn:ietf:params:oauth:client-assertion-type:jwt-bearer',
           timeout=None):
        """Get all valid channel access token key IDs v2.1.

        https://developers.line.biz/en/reference/messaging-api/#get-all-valid-channel-access-token-key-ids-v2-1

        :param str client_assertion: Client assertion.
        :param str client_assertion_type: `urn:ietf:params:oauth:client-assertion-type:jwt-bearer`.
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.VerifyChannelTokenResponseV2`
        """
        response = self._get('/oauth2/v2.1/tokens/kid',
                             params={"client_assertion": client_assertion,
                                     "client_assertion_type": client_assertion_type},
                             timeout=timeout)
        return ValidAccessTokenKeyIDsResponse.new_from_json_dict(response.json)

    def get_statistics_per_unit(self, custom_aggregation_unit, from_date, to_date, timeout=None):
        """Return statistics about how users interact with push and multicast messages.

        https://developers.line.biz/en/reference/partner-docs/#get-statistics-per-unit

        :param str custom_aggregation_unit: Name of aggregation unit specified when sending
            the message like `push_message(...)` and `multicast(...)`.
        :param str from_date: Start date of aggregation period.
            The format is `yyyyMMdd` (Timezone is UTC+9).
        :param str to_date: End date of aggregation period.
            The end date can be specified for up to 30 days later.
            The format is `yyyyMMdd` (Timezone is UTC+9).
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:
            `linebot.models.responses.InsightMessageEventOfCustomAggregationUnitResponse`
        """
        response = self._get(
            '/v2/bot/insight/message/event/aggregation?'
            'customAggregationUnit={custom_aggregation_unit}&from={from_date}&to={to_date}'.format(
                custom_aggregation_unit=custom_aggregation_unit,
                from_date=from_date, to_date=to_date),
            timeout=timeout
        )

        return InsightMessageEventOfCustomAggregationUnitResponse.new_from_json_dict(response.json)

    def get_number_of_units_used_this_month(self, timeout=None):
        """Return the number of aggregation units used this month.

        https://developers.line.biz/en/reference/partner-docs/#get-number-of-units-used-this-month

        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class: `linebot.models.responses.AggregationInfoResponse`
        """
        response = self._get('/v2/bot/message/aggregation/info', timeout=timeout)
        return AggregationInfoResponse.new_from_json_dict(response.json)

    def get_name_list_of_units_used_this_month(self, limit=100, start=None, timeout=None):
        """Return the name list of units used this month for statistics aggregation.

        :param int limit: Maximum number of aggregation units you can get per request.
            If you don't specify a value, or if you specify a value greater than or equal to 100,
            the maximum is 100.
        :param str start: Get the next array of name list of units
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class: `linebot.models.responses.AggregationNameListResponse`
        """
        params = {'limit': limit} if start is None else {'limit': limit, 'start': start}

        response = self._get(
            '/v2/bot/message/aggregation/list',
            params=params,
            timeout=timeout
        )

        return AggregationNameListResponse.new_from_json_dict(response.json)

    def _get(self, path, endpoint=None, params=None, headers=None, stream=False, timeout=None):
        url = (endpoint or self.endpoint) + path

        if headers is None:
            headers = {}
        headers.update(self.headers)

        response = self.http_client.get(
            url, headers=headers, params=params, stream=stream, timeout=timeout
        )

        self.__check_error(response)
        return response

    def _post(self, path, endpoint=None, data=None, headers=None, timeout=None):
        url = (endpoint or self.endpoint) + path

        if headers is None:
            headers = {'Content-Type': 'application/json'}
        headers.update(self.headers)

        response = self.http_client.post(
            url, headers=headers, data=data, timeout=timeout
        )

        self.__check_error(response)
        return response

    def _delete(self, path, endpoint=None, data=None, headers=None, timeout=None):
        url = (endpoint or self.endpoint) + path

        if headers is None:
            headers = {}
        headers.update(self.headers)

        response = self.http_client.delete(
            url, headers=headers, data=data, timeout=timeout
        )

        self.__check_error(response)
        return response

    def _put(self, path, endpoint=None, data=None, headers=None, timeout=None):
        url = (endpoint or self.endpoint) + path

        if headers is None:
            headers = {'Content-Type': 'application/json'}
        headers.update(self.headers)

        response = self.http_client.put(
            url, headers=headers, data=data, timeout=timeout
        )

        self.__check_error(response)
        return response

    @staticmethod
    def __check_error(response):
        if 200 <= response.status_code < 300:
            pass
        else:
            raise LineBotApiError(
                status_code=response.status_code,
                headers=dict(response.headers.items()),
                request_id=response.headers.get('X-Line-Request-Id'),
                accepted_request_id=response.headers.get('X-Line-Accepted-Request-Id'),
                error=Error.new_from_json_dict(response.json)
            )
