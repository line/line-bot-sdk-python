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

"""linebot.models.responses module."""

from __future__ import unicode_literals

from .base import Base
from .insight import (
    SubscriptionPeriodInsight, AppTypeInsight,
    AgeInsight, GenderInsight, AreaInsight,
    MessageInsight, ClickInsight, MessageStatistics,
)
from .rich_menu import RichMenuSize, RichMenuArea


class BroadcastResponse(object):
    """BroadcastResponse.

    https://developers.line.biz/en/reference/messaging-api/#send-broadcast-message
    """

    def __init__(self, request_id=None):
        """__init__ method.

        :param str request_id: Request ID. A unique ID is generated for each request
        """
        self.request_id = request_id


class Profile(Base):
    """Profile.

    https://developers.line.biz/en/reference/messaging-api/#get-profile
    """

    def __init__(self, display_name=None, user_id=None, picture_url=None,
                 status_message=None, language=None, **kwargs):
        """__init__ method.

        :param str display_name: Display name
        :param str user_id: User ID
        :param str picture_url: Image URL
        :param str status_message: Status message
        :param str language: Get user's language
        :param kwargs:
        """
        super(Profile, self).__init__(**kwargs)

        self.display_name = display_name
        self.user_id = user_id
        self.picture_url = picture_url
        self.status_message = status_message
        self.language = language


class Group(Base):
    """Group.

    https://developers.line.biz/en/reference/messaging-api/#get-group-id-response
    """

    def __init__(self, group_id=None, group_name=None, picture_url=None, **kwargs):
        """__init__ method.

        :param str group_id
        :param str group_name
        :param str picture_url
        :param kwargs:
        """
        super(Group, self).__init__(**kwargs)

        self.group_id = group_id
        self.group_name = group_name
        self.picture_url = picture_url


class MemberIds(Base):
    """MemberIds.

    https://developers.line.biz/en/reference/messaging-api/#get-group-member-user-ids
    https://developers.line.biz/en/reference/messaging-api/#get-room-member-user-ids
    """

    def __init__(self, member_ids=None, next=None, **kwargs):
        """__init__ method.

        :param member_ids: List of user IDs of the members in the group or room.
            Max: 100 user IDs
        :type member_ids: list[str]
        :param str next: continuationToken.
            Only returned when there are more user IDs remaining in memberIds.
        :param kwargs:
        """
        super(MemberIds, self).__init__(**kwargs)

        self.member_ids = member_ids
        self.next = next


class Content(object):
    """MessageContent.

    https://developers.line.biz/en/reference/messaging-api/#get-content
    """

    def __init__(self, response):
        """__init__ method.

        :param response: HttpResponse object
        :type response: T <= :py:class:`linebot.http_client.HttpResponse`
        """
        self.response = response

    @property
    def content_type(self):
        """Get Content-type header value.

        :rtype: str
        :return: content-type header value
        """
        return self.response.headers.get('content-type')

    @property
    def content(self):
        """Get content.

        If content size is large, should use iter_content.

        :rtype: binary
        """
        return self.response.content

    def iter_content(self, chunk_size=1024):
        """Get content as iterator (stream).

        If content size is large, should use this.

        :param chunk_size: Chunk size
        :rtype: iterator
        """
        return self.response.iter_content(chunk_size=chunk_size)


class RichMenuResponse(Base):
    """RichMenuResponse.

    https://developers.line.me/en/docs/messaging-api/reference/#rich-menu-response-object
    """

    def __init__(self, rich_menu_id=None, size=None, selected=None, name=None,
                 chat_bar_text=None, areas=None, **kwargs):
        """__init__ method.

        :param str id: Rich Menu ID
        :param size: size object which describe the rich menu displayed in the chat.
            Rich menu images must be one of the following sizes: 2500x1686, 2500x843.
        :type size: :py:class:`linebot.models.rich_menu.RichMenuSize`
        :param bool selected: true to display the rich menu by default. Otherwise, false.
        :param str name: Name of the rich menu.
            Maximum of 300 characters.
        :param str chat_bar_text: Text displayed in the chat bar.
            Maximum of 14 characters.
        :param areas: Array of area objects which define coordinates and size of tappable areas.
            Maximum of 20 area objects.
        :type areas: list[T <= :py:class:`linebot.models.rich_menu.RichMenuArea`]
        :param kwargs:
        """
        super(RichMenuResponse, self).__init__(**kwargs)

        self.rich_menu_id = rich_menu_id
        self.size = self.get_or_new_from_json_dict(size, RichMenuSize)
        self.selected = selected
        self.name = name
        self.chat_bar_text = chat_bar_text

        new_areas = []
        if areas:
            for area in areas:
                new_areas.append(
                    self.get_or_new_from_json_dict(area, RichMenuArea)
                )
        self.areas = new_areas


class MessageQuotaResponse(Base):
    """MessageQuotaResponse.

    https://developers.line.biz/en/reference/messaging-api/#get-quota
    """

    def __init__(self, type=None, value=None, **kwargs):
        """__init__ method.

        :param str type: Quota limitation type
        :param int value: The target limit for additional messages in the current month.
            This property is returned when the type property has a value of limited.
        :param kwargs:
        """
        super(MessageQuotaResponse, self).__init__(**kwargs)

        self.type = type
        self.value = value


class MessageQuotaConsumptionResponse(Base):
    """MessageQuotaConsumptionResponse.

    https://developers.line.biz/en/reference/messaging-api/#get-consumption
    """

    def __init__(self, total_usage=None, **kwargs):
        """__init__ method.

        :param str total_usage: The number of sent messages in the current month
        :param kwargs:
        """
        super(MessageQuotaConsumptionResponse, self).__init__(**kwargs)

        self.total_usage = total_usage


class MessageDeliveryBroadcastResponse(Base):
    """MessageDeliveryBroadcastResponse."""

    def __init__(self, status=None, success=None, **kwargs):
        """__init__ method.

        :param str status: Status of the counting process.
        :param int success: The number of messages sent with the Messaging API on the
            date specified in date.
        :param kwargs:
        """
        super(MessageDeliveryBroadcastResponse, self).__init__(**kwargs)

        self.status = status
        self.success = success


class MessageDeliveryReplyResponse(Base):
    """MessageDeliveryReplyResponse."""

    def __init__(self, status=None, success=None, **kwargs):
        """__init__ method.

        :param str status: Status of the counting process.
        :param int success: The number of messages sent with the Messaging API on the
            date specified in date.
        :param kwargs:
        """
        super(MessageDeliveryReplyResponse, self).__init__(**kwargs)

        self.status = status
        self.success = success


class MessageDeliveryPushResponse(Base):
    """MessageDeliveryPushResponse."""

    def __init__(self, status=None, success=None, **kwargs):
        """__init__ method.

        :param str status: Status of the counting process.
        :param int success: The number of messages sent with the Messaging API on the
            date specified in date.
        :param kwargs:
        """
        super(MessageDeliveryPushResponse, self).__init__(**kwargs)

        self.status = status
        self.success = success


class MessageDeliveryMulticastResponse(Base):
    """MessageDeliveryMulticastResponse."""

    def __init__(self, status=None, success=None, **kwargs):
        """__init__ method.

        :param str status: Status of the counting process.
        :param int success: The number of messages sent with the Messaging API on the
            date specified in date.
        :param kwargs:
        """
        super(MessageDeliveryMulticastResponse, self).__init__(**kwargs)

        self.status = status
        self.success = success


class MessageProgressNarrowcastResponse(Base):
    """MessageProgressNarrowcastResponse."""

    def __init__(self, phase=None, success_count=None, failure_count=None,
                 target_count=None, failed_description=None, error_code=None, **kwargs):
        """__init__ method.

        :param str phase: Progress status. One of `waiting`, `sending`,
            `succeeded`, or `failed`.
        :param int success_count: Number of narrowcast messages sent successful.
        :param int failure_count: Number of narrowcast messages sent failed.
        :param int target_count: Number of targeted messages sent.
        :param str failed_description: Reaseon why narrowcast failed, useful when
            phase is `failed`.
        :param int error_code: Summary of the error. One of `1` or `2`. `1`
            means internal error, whereas `2` indicates too few targets.
        :param kwargs:
        """
        super(MessageProgressNarrowcastResponse, self).__init__(**kwargs)

        self.phase = phase
        self.success_count = success_count
        self.failure_count = failure_count
        self.target_count = target_count
        self.failed_description = failed_description
        self.error_code = error_code


class IssueLinkTokenResponse(Base):
    """IssueLinkTokenResponse.

    https://developers.line.biz/en/reference/messaging-api/#issue-link-token
    """

    def __init__(self, link_token=None, **kwargs):
        """__init__ method.

        :param str link_token: Link token.
        :param kwargs:
        """
        super(IssueLinkTokenResponse, self).__init__(**kwargs)

        self.link_token = link_token


class IssueChannelTokenResponse(Base):
    """IssueAccessTokenResponse.

    https://developers.line.biz/en/reference/messaging-api/#issue-channel-access-token
    """

    def __init__(self, access_token=None, expires_in=None, token_type=None, **kwargs):
        """__init__ method.

        :param str access_token: Short-lived channel access token.
        :param int expires_in: Time until channel access token expires in seconds
            from time the token is issued.
        :param str token_type: Bearer.
        :param kwargs:
        """
        super(IssueChannelTokenResponse, self).__init__(**kwargs)

        self.access_token = access_token
        self.expires_in = expires_in
        self.token_type = token_type


class InsightMessageDeliveryResponse(Base):
    """InsightMessageDeliveryResponse."""

    def __init__(self, status=None, broadcast=None, targeting=None, auto_response=None,
                 welcome_response=None, chat=None, api_broadcast=None, api_push=None,
                 api_multicast=None, api_reply=None, **kwargs):
        """__init__ method.

        :param str status: Calculation status. One of `ready`, `unready`, or `out_of_service`.
        :param int broadcast: Number of broadcast messages sent.
        :param int targeting: Number of targeted/segmented messages sent.
        :param int auto_response: Number of auto-response messages sent.
        :param int welcome_response: Number of greeting messages sent.
        :param int chat: Number of messages sent from LINE Official Account Manager Chat screen.
        :param int api_broadcast: Number of broadcast messages sent with
            the Send broadcast message Messaging API operation.
        :param int api_push: Number of push messages sent
            with the Send push message Messaging API operation.
        :param int api_multicast: Number of multicast messages sent with
            the Send multicast message Messaging API operation.
        :param int api_reply: Number of replies sent
            with the Send reply message Messaging API operation.
        :param int success: The number of messages sent with the Messaging API
            on the date specified in date.
        :param kwargs:
        """
        super(InsightMessageDeliveryResponse, self).__init__(**kwargs)

        self.status = status
        self.broadcast = broadcast
        self.targeting = targeting
        self.auto_response = auto_response
        self.welcome_response = welcome_response
        self.chat = chat
        self.api_broadcast = api_broadcast
        self.api_push = api_push
        self.api_multicast = api_multicast
        self.api_reply = api_reply


class InsightFollowersResponse(Base):
    """InsightFollowersResponse."""

    def __init__(self, status=None, followers=None, targeted_reaches=None, blocks=None, **kwargs):
        """__init__ method.

        :param str status: Calculation status. One of `ready`, `unready`, or `out_of_service`.
        :param int followers: The number of times, as of the specified date,
            that a user added this LINE official account as a friend for the first time.
        :param int targeted_reaches: The number of users, as of the specified date,
            that the official account can reach through targeted messages based
            on gender, age, and/or region.
        :param int blocks: The number of users blocking the account as of the specified date.
        :param kwargs:
        """
        super(InsightFollowersResponse, self).__init__(**kwargs)

        self.status = status
        self.followers = followers
        self.targeted_reaches = targeted_reaches
        self.blocks = blocks


class InsightDemographicResponse(Base):
    """InsightDemographicResponse."""

    def __init__(self, available=None, genders=None, ages=None,
                 areas=None, app_types=None, subscription_periods=None, **kwargs):
        """__init__ method.

        :param bool available: `true` if friend demographic information is available.
        :param genders: Percentage per gender.
        :type genders: list[T <= :py:class:`linebot.models.GenderInsight`]
        :param ages: Percentage per age group.
        :type ages: list[T <= :py:class:`linebot.models.AgeInsight`]
        :param areas: Percentage per area.
        :type areas: list[T <= :py:class:`linebot.models.AreaInsight`]
        :param app_types: Percentage by OS.
        :type app_types: list[T <= :py:class:`linebot.models.AppTypeInsight`]
        :param subscription_periods: Percentage per friendship duration.
        :type subscription_periods: list[T <= :py:class:`linebot.models.SubscriptionPeriodInsight`]
        :param kwargs:
        """
        super(InsightDemographicResponse, self).__init__(**kwargs)

        self.available = available
        self.genders = [self.get_or_new_from_json_dict(it, GenderInsight) for it in genders]
        self.ages = [self.get_or_new_from_json_dict(it, AgeInsight) for it in ages]
        self.areas = [self.get_or_new_from_json_dict(it, AreaInsight) for it in areas]
        self.app_types = [self.get_or_new_from_json_dict(it, AppTypeInsight) for it in app_types]
        self.subscription_periods = [self.get_or_new_from_json_dict(it, SubscriptionPeriodInsight)
                                     for it in subscription_periods]


class InsightMessageEventResponse(Base):
    """InsightMessageEventResponse."""

    def __init__(self, overview=None, messages=None, clicks=None, **kwargs):
        """__init__ method.

        :param overview: Summary of message statistics.
        :type overview: T <= :py:class:`linebot.models.MessageStatistics`
        :param messages: Array of information about individual message bubbles.
        :type messages: list[T <= :py:class:`linebot.models.MessageInsight`]
        :param clicks: Array of information about URLs in the message.
        :type clicks: list[T <= :py:class:`linebot.models.ClickInsight`]
        :param kwargs:
        """
        super(InsightMessageEventResponse, self).__init__(**kwargs)

        self.overview = self.get_or_new_from_json_dict(overview, MessageStatistics)
        self.messages = [self.get_or_new_from_json_dict(it, MessageInsight) for it in messages]
        self.clicks = [self.get_or_new_from_json_dict(it, ClickInsight) for it in clicks]


class NarrowcastResponse(Base):
    """NarrowcastResponse.

    https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-message
    """

    def __init__(self, request_id=None, **kwargs):
        """__init__ method.

        :param str request_id: Request ID. A unique ID is generated for each request
        :param kwargs:
        """
        super(NarrowcastResponse, self).__init__(**kwargs)

        self.request_id = request_id
