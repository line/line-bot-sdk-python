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

from .base import Base
from .insight import (
    SubscriptionPeriodInsight, AppTypeInsight, AgeInsight,
    GenderInsight, AreaInsight, MessageInsight, ClickInsight,
    MessageStatistics, JobInsight, MessageStatisticsOfCustomAggregationUnit,
)
from .rich_menu import RichMenuSize, RichMenuArea, RichMenuAlias


class BroadcastResponse(object):
    """BroadcastResponse.

    https://developers.line.biz/en/reference/messaging-api/#send-broadcast-message
    """

    def __init__(self, request_id=None):
        """__init__ method.

        :param str request_id: Request ID. A unique ID is generated for each request
        """
        self.request_id = request_id


class ValidateReplyMessageObjectsResponse(object):
    """ValidateReplyMessageObjectsResponse.

    https://developers.line.biz/en/reference/messaging-api/#validate-message-objects-of-reply-message
    """

    def __init__(self, request_id=None):
        """__init__ method.

        :param str request_id: Request ID. A unique ID is generated for each request
        """
        self.request_id = request_id


class ValidatePushMessageObjectsResponse(object):
    """ValidatePushMessageObjectsResponse.

    https://developers.line.biz/en/reference/messaging-api/#validate-message-objects-of-push-message
    """

    def __init__(self, request_id=None):
        """__init__ method.

        :param str request_id: Request ID. A unique ID is generated for each request
        """
        self.request_id = request_id


class ValidateMulticastMessageObjectsResponse(object):
    """ValidateMulticastMessageObjectsResponse.

    https://developers.line.biz/en/reference/messaging-api/#validate-message-objects-of-multicast-message
    """

    def __init__(self, request_id=None):
        """__init__ method.

        :param str request_id: Request ID. A unique ID is generated for each request
        """
        self.request_id = request_id


class ValidateNarrowcastMessageObjectsResponse(object):
    """ValidateNarrowcastMessageObjectsResponse.

    https://developers.line.biz/en/reference/messaging-api/#validate-message-objects-of-narrowcast-message
    """

    def __init__(self, request_id=None):
        """__init__ method.

        :param str request_id: Request ID. A unique ID is generated for each request
        """
        self.request_id = request_id


class ValidateBroadcastMessageObjectsResponse(object):
    """ValidateBroadcastMessageObjectsResponse.

    https://developers.line.biz/en/reference/messaging-api/#validate-message-objects-of-broadcast-message
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


class RichMenuAliasResponse(Base):
    """RichMenuAliasResponse.

    https://developers.line.biz/en/reference/messaging-api/#get-rich-menu-alias-by-id-response
    """

    def __init__(self, rich_menu_alias_id=None, rich_menu_id=None, **kwargs):
        """__init__ method.

        :param str rich_menu_alias_id: Rich menu alias ID.
        :param str rich_menu_id: Rich menu ID.
        :param kwargs:
        """
        super(RichMenuAliasResponse, self).__init__(**kwargs)

        self.rich_menu_alias_id = rich_menu_alias_id
        self.rich_menu_id = rich_menu_id


class RichMenuAliasListResponse(Base):
    """RichMenuAliasListResponse.

    https://developers.line.biz/en/reference/messaging-api/#get-rich-menu-alias-list-response
    """

    def __init__(self, aliases=None, **kwargs):
        """__init__ method.

        :param aliases: Array of rich menu alias objects
        :type areas: list[T <= :py:class:`linebot.models.RichMenuAlias`]
        :param kwargs:
        """
        super(RichMenuAliasListResponse, self).__init__(**kwargs)
        new_aliases = []
        if aliases:
            for alias in aliases:
                new_aliases.append(
                    self.get_or_new_from_json_dict(alias, RichMenuAlias)
                )
        self.aliases = new_aliases


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
                 target_count=None, failed_description=None, error_code=None,
                 accepted_time=None, completed_time=None, **kwargs):
        """__init__ method.

        :param str phase: Progress status. One of `waiting`, `sending`,
            `succeeded`, or `failed`.
        :param int success_count: Number of narrowcast messages sent successful.
        :param int failure_count: Number of narrowcast messages sent failed.
        :param int target_count: Number of targeted messages sent.
        :param str failed_description: Reason why narrowcast failed, useful when
            phase is `failed`.
        :param int error_code: Summary of the error. One of `1` or `2`. `1`
            means internal error, whereas `2` indicates too few targets.
        :param str accepted_time: Narrowcast message request accepted time in milliseconds.
        :param str completed_time: Processing of narrowcast message request
            completion time in milliseconds.
        :param kwargs:
        """
        super(MessageProgressNarrowcastResponse, self).__init__(**kwargs)

        self.phase = phase
        self.success_count = success_count
        self.failure_count = failure_count
        self.target_count = target_count
        self.failed_description = failed_description
        self.error_code = error_code
        self.accepted_time = accepted_time
        self.completed_time = completed_time


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


class InsightMessageEventOfCustomAggregationUnitResponse(Base):
    """InsightMessageEventResponse."""

    def __init__(self, overview=None, messages=None, clicks=None, **kwargs):
        """__init__ method.

        :param overview: Summary of message statistics.
        :type overview: T <= :py:class:`linebot.models.MessageStatisticsOfCustomAggregationUnit`
        :param messages: Array of information about individual message bubbles.
        :type messages: list[T <= :py:class:`linebot.models.MessageInsight`]
        :param clicks: Array of information about URLs in the message.
        :type clicks: list[T <= :py:class:`linebot.models.ClickInsight`]
        :param kwargs:
        """
        super(InsightMessageEventOfCustomAggregationUnitResponse, self).__init__(**kwargs)

        self.overview = self.get_or_new_from_json_dict(
            overview, MessageStatisticsOfCustomAggregationUnit)
        self.messages = [self.get_or_new_from_json_dict(it, MessageInsight) for it in messages]
        self.clicks = [self.get_or_new_from_json_dict(it, ClickInsight) for it in clicks]


class AggregationInfoResponse(Base):
    """The number of aggregation units used this month.

    https://developers.line.biz/en/reference/partner-docs/#get-number-of-units-used-this-month
    """

    def __init__(self, num_of_custom_aggregation_units=None, **kwargs):
        """__init__ method.

        :param int num_of_custom_aggregation_units: Number of aggregation units used this month.
        :param kwargs:
        """
        super(AggregationInfoResponse, self).__init__(**kwargs)

        self.num_of_custom_aggregation_units = num_of_custom_aggregation_units


class AggregationNameListResponse(Base):
    """The name list of units used this month for statistics aggregation.

    https://developers.line.biz/en/reference/partner-docs/#get-name-list-of-units-used-this-month
    """

    def __init__(self, custom_aggregation_units=None, next=None, **kwargs):
        """__init__ method.

        :param custom_aggregation_units: name list of aggregation units used this month.
            Max: 100 unit names
        :type custom_aggregation_units: list[str]
        :param str next: continuationToken.
            A continuation token to get the next array of unit names.
        :param kwargs:
        """
        super(AggregationNameListResponse, self).__init__(**kwargs)

        self.custom_aggregation_units = custom_aggregation_units
        self.next = next


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


class BotInfo(Base):
    """Response of `linebot.get_bot_info()` .

    https://developers.line.biz/en/reference/messaging-api/#get-bot-info
    """

    def __init__(self, user_id=None, basic_id=None, premium_id=None,
                 display_name=None, picture_url=None, chat_mode=None,
                 mark_as_read_mode=None, **kwargs):
        """__init__ method.

        :param kwargs:
        """
        super(BotInfo, self).__init__(**kwargs)

        self.user_id = user_id
        self.basic_id = basic_id
        self.premium_id = premium_id
        self.display_name = display_name
        self.picture_url = picture_url
        self.chat_mode = chat_mode
        self.mark_as_read_mode = mark_as_read_mode


class GetWebhookResponse(Base):
    """Response of `get_webhook_endpoint()` .

    https://developers.line.biz/en/reference/messaging-api/#get-webhook-endpoint-information
    """

    def __init__(self, endpoint=None, active=None, **kwargs):
        """__init__ method.

        :param str endpoint: The webhook endpoint URL.
        :param bool active: Whether the webhook is in use.
        :param kwargs:
        """
        super(GetWebhookResponse, self).__init__(**kwargs)

        self.endpoint = endpoint
        self.active = active


class TestWebhookResponse(Base):
    """Response of `test_webhook_endpoint()` .

    https://developers.line.biz/en/reference/messaging-api/#test-webhook-endpoint
    """

    def __init__(self, success=None, timestamp=None, status_code=None,
                 reason=None, detail=None, **kwargs):
        """__init__ method.

        :param bool success: Result of the communication from the LINE platform
            to the webhook URL.
        :param str timestamp: Timestamp
        :param int status_code: The HTTP status code.
        :param str reason: Reason for the response.
        :param str detail: Details of the response.
        :param kwargs:
        """
        super(TestWebhookResponse, self).__init__(**kwargs)

        self.success = success
        self.timestamp = timestamp
        self.status_code = status_code
        self.reason = reason
        self.detail = detail


class AudienceGroup(Base):
    """AudienceGroups.

    https://developers.line.biz/en/reference/messaging-api/#get-audience-group
    """

    def __init__(self, audience_group_id=None, type=None, description=None, status=None,
                 audience_count=None, created=None, is_ifa_audience=None, permission=None,
                 create_route=None, request_id=None, failed_type=None, click_url=None,
                 jobs=None, **kwargs):
        """__init__ method.

        :param int audience_group_id: The audience ID.
        :param str type: The audience type. One of `UPLOAD` or `CLICK` or `IMP` or `CHAT_TAG`
             or `FRIEND_PATH`.
        :param str description: The audience's name.
        :param str status: The audience's status. One of `IN_PROGRESS` or `READY` or `FAILED`
             or `EXPIRED`.
        :param int audience_count: The number of valid recipients.
        :param int created: When the audience was created (in UNIX time).
        :param bool is_ifa_audience: The value specified when creating an audience for uploading
            user IDs to indicate the type of accounts that will be given as recipients.
        :param str permission: Audience's update permission. Audiences linked to the same channel
            will be READ_WRITE.
        :param str create_route: How the audience was created. If omitted,
            you will get all audiences.
        :param str request_id: The request ID that was specified when the audience was created.
        :param str failed_type: The reason why the operation failed. This is only included when
            status is FAILED.  One of `AUDIENCE_GROUP_AUDIENCE_INSUFFICIENT` or `INTERNAL_ERROR`
        :param str click_url: The URL that was specified when the audience was created.
            This is only included when type is CLICK
        :param jobs: An array of jobs. This array is used to keep track of each attempt to
            add new user IDs or IFAs to an audience for uploading user IDs.
        :param kwargs:
        """
        super(AudienceGroup, self).__init__(**kwargs)

        self.audience_group_id = audience_group_id
        self.type = type
        self.description = description
        self.status = status
        self.audience_count = audience_count
        self.created = created
        self.is_ifa_audience = is_ifa_audience
        self.permission = permission
        self.create_route = create_route
        self.request_id = request_id
        self.failed_type = failed_type
        self.click_url = click_url
        if jobs:
            self.jobs = [self.get_or_new_from_json_dict(job, JobInsight) for job in jobs]


class ClickAudienceGroup(Base):
    """ClickAudienceGroup.

    https://developers.line.biz/en/reference/messaging-api/#create-click-audience-group
    """

    def __init__(self, audience_group_id=None, create_route=None, type=None, description=None,
                 created=None, permission=None, expire_timestamp=None, is_ifa_audience=None,
                 request_id=None, click_url=None, **kwargs):
        """__init__ method.

        :param int audience_group_id: The audience ID.
        :param str create_route: How the audience was created. If omitted,
            you will get all audiences.
        :param str type: The audience type. One of `UPLOAD` or `CLICK` or `IMP` or `CHAT_TAG`
             or `FRIEND_PATH`.
        :param str description: The audience's name.
        :param int created: When the audience was created (in UNIX time).
        :param str permission: Audience's update permission. Audiences linked to the same channel
            will be READ_WRITE.
        :param int expire_timestamp: Time of audience expiration. Only returned for specific
            audiences.
        :param bool is_ifa_audience: The value specified when creating an audience for uploading
            user IDs to indicate the type of accounts that will be given as recipients.
        :param str request_id: The request ID that was specified when the audience was created.
        :param str click_url: The URL that was specified when the audience was created.
            This is only included when type is CLICK
        :param kwargs:
        """
        super(ClickAudienceGroup, self).__init__(**kwargs)

        self.audience_group_id = audience_group_id
        self.create_route = create_route
        self.type = type
        self.description = description
        self.created = created
        self.permission = permission
        self.expire_timestamp = expire_timestamp
        self.is_ifa_audience = is_ifa_audience
        self.request_id = request_id
        self.click_url = click_url


class CreateAudienceGroup(Base):
    """ClickAudienceGroup.

    https://developers.line.biz/en/reference/messaging-api/#create-upload-audience-group
    """

    def __init__(self, audience_group_id=None, create_route=None, type=None, description=None,
                 created=None, permission=None, expire_timestamp=None, is_ifa_audience=None,
                 **kwargs):
        """__init__ method.

        :param int audience_group_id: The audience ID.
        :param str create_route: How the audience was created. If omitted,
            you will get all audiences.
        :param str type: The audience type. One of `UPLOAD` or `CLICK` or `IMP` or `CHAT_TAG`
             or `FRIEND_PATH`.
        :param str description: The audience's name.
        :param int created: When the audience was created (in UNIX time).
        :param str permission: Audience's update permission. Audiences linked to the same channel
            will be READ_WRITE.
        :param int expire_timestamp: Time of audience expiration. Only returned for specific
            audiences.
        :param bool is_ifa_audience: The value specified when creating an audience for uploading
            user IDs to indicate the type of accounts that will be given as recipients.
        :param kwargs:
        """
        super(CreateAudienceGroup, self).__init__(**kwargs)

        self.audience_group_id = audience_group_id
        self.create_route = create_route
        self.type = type
        self.description = description
        self.created = created
        self.permission = permission
        self.expire_timestamp = expire_timestamp
        self.is_ifa_audience = is_ifa_audience


class ImpAudienceGroup(Base):
    """ImpAudienceGroup.

    https://developers.line.biz/en/reference/messaging-api/#create-imp-audience-group
    """

    def __init__(self, audience_group_id=None, create_route=None, type=None, description=None,
                 created=None, permission=None, expire_timestamp=None, is_ifa_audience=None,
                 request_id=None, **kwargs):
        """__init__ method.

        :param int audience_group_id: The audience ID.
        :param str create_route: How the audience was created. If omitted,
            you will get all audiences.
        :param str type: The audience type. One of `UPLOAD` or `CLICK` or `IMP` or `CHAT_TAG`
             or `FRIEND_PATH`.
        :param str description: The audience's name.
        :param int created: When the audience was created (in UNIX time).
        :param str permission: Audience's update permission. Audiences linked to the same channel
            will be READ_WRITE.
        :param int expire_timestamp: Time of audience expiration. Only returned for specific
            audiences.
        :param bool is_ifa_audience: The value specified when creating an audience for uploading
            user IDs to indicate the type of accounts that will be given as recipients.
        :param str request_id: The request ID that was specified when the audience was created.
        :param kwargs:
        """
        super(ImpAudienceGroup, self).__init__(**kwargs)

        self.audience_group_id = audience_group_id
        self.create_route = create_route
        self.type = type
        self.description = description
        self.created = created
        self.permission = permission
        self.expire_timestamp = expire_timestamp
        self.is_ifa_audience = is_ifa_audience
        self.request_id = request_id


class GetAuthorityLevel(Base):
    """GetAuthorityLevel.

    https://developers.line.biz/en/reference/messaging-api/#get-authority-level
    """

    def __init__(self, authority_level=None, **kwargs):
        """__init__ method.

        :param str authority_level: The authority level for all audiences linked to a channel.
        :param kwargs:
        """
        super(GetAuthorityLevel, self).__init__(**kwargs)

        self.authority_level = authority_level


class Audience(Base):
    """Audience.

    https://developers.line.biz/en/reference/messaging-api/#update-upload-audience-group
    """

    def __init__(self, id=None, **kwargs):
        """__init__ method.

        :param str audience_id: A user ID or IFA.
        :param kwargs:
        """
        super(Audience, self).__init__(**kwargs)
        self.id = id


class UserIds(Base):
    """UserIds.

    https://developers.line.biz/en/reference/messaging-api/#get-follower-ids
    """

    def __init__(self, user_ids=None, next=None, **kwargs):
        """__init__ method.

        :param user_ids: List of user IDs of users
            that have added the LINE Official Account as a friend.
            Max: 300 user IDs
        :type user_ids: list[str]
        :param str next: continuationToken.
            A continuation token to get the next array of user IDs.
        :param kwargs:
        """
        super(UserIds, self).__init__(**kwargs)

        self.user_ids = user_ids
        self.next = next


class IssueChannelTokenResponseV2(Base):
    """IssueAccessTokenResponseV2.

    https://developers.line.biz/en/reference/messaging-api/#issue-channel-access-token-v2-1
    """

    def __init__(self, access_token=None, expires_in=None, token_type=None, key_id=None, **kwargs):
        """__init__ method.

        :param str access_token: Short-lived channel access token.
        :param int expires_in: Time until channel access token expires in seconds
            from time the token is issued.
        :param str token_type: Bearer.
        :param key_id: Unique key ID for identifying the channel access token.
        :param kwargs:
        """
        super(IssueChannelTokenResponseV2, self).__init__(**kwargs)

        self.access_token = access_token
        self.expires_in = expires_in
        self.token_type = token_type
        self.key_id = key_id


class ChannelAccessTokens(Base):
    """ChannelAccessTokens.

    https://developers.line.biz/en/reference/messaging-api/#get-issued-channel-access-tokens-v2-1
    """

    def __init__(self, access_tokens=None, **kwargs):
        """__init__ method.

        :param access_tokens: List of channel access token
        :type access_tokens: list[str]
        :param kwargs:

        """
        super(ChannelAccessTokens, self).__init__(**kwargs)

        self.access_tokens = access_tokens


class VerifyChannelTokenResponseV2(Base):
    """VerifyChannelTokenResponseV2.

    https://developers.line.biz/en/reference/messaging-api/#verfiy-channel-access-token-v2-1

    """

    def __init__(self, client_id=None, expires_in=None, scope=None, **kwargs):
        """__init__ method.

        :param str client_id: The channel ID for which the channel access token was issued.
        :param int expires_in: Number of seconds before the channel access token expires.
        :param str scope: Permissions granted to the channel access token.
        :param kwargs:

        """
        super(VerifyChannelTokenResponseV2, self).__init__(**kwargs)

        self.client_id = client_id
        self.expires_in = expires_in
        self.scope = scope


class ValidAccessTokenKeyIDsResponse(Base):
    """ValidAccessTokenKeyIDsResponse.

    https://developers.line.biz/en/reference/messaging-api/#get-all-valid-channel-access-token-key-ids-v2-1

    """

    def __init__(self, kids=None, **kwargs):
        """__init__ method.

        :param kids: Array of channel access token key IDs.
        :type kids: list[str]
        :param kwargs:
        """
        super(ValidAccessTokenKeyIDsResponse, self).__init__(**kwargs)

        self.kids = kids
