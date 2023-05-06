# coding: utf-8

# flake8: noqa

"""
    LINE Messaging API(Insight)

    This document describes LINE Messaging API(Insight).  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


__version__ = "1.0.0"

# import apis into sdk package
from linebot.insight.api.insight_api import InsightApi

from linebot.insight.api.async_insight_api import AsyncInsightApi


# import ApiClient
from linebot.insight.api_response import ApiResponse
from linebot.insight.api_client import ApiClient
from linebot.insight.async_api_client import AsyncApiClient
from linebot.insight.configuration import Configuration
from linebot.insight.exceptions import OpenApiException
from linebot.insight.exceptions import ApiTypeError
from linebot.insight.exceptions import ApiValueError
from linebot.insight.exceptions import ApiKeyError
from linebot.insight.exceptions import ApiAttributeError
from linebot.insight.exceptions import ApiException

# import models into sdk package
from linebot.insight.models.age_tile import AgeTile
from linebot.insight.models.app_type_tile import AppTypeTile
from linebot.insight.models.area_tile import AreaTile
from linebot.insight.models.error_detail import ErrorDetail
from linebot.insight.models.error_response import ErrorResponse
from linebot.insight.models.gender_tile import GenderTile
from linebot.insight.models.get_friends_demographics_response import GetFriendsDemographicsResponse
from linebot.insight.models.get_message_event_response import GetMessageEventResponse
from linebot.insight.models.get_message_event_response_click import GetMessageEventResponseClick
from linebot.insight.models.get_message_event_response_message import GetMessageEventResponseMessage
from linebot.insight.models.get_message_event_response_overview import GetMessageEventResponseOverview
from linebot.insight.models.get_number_of_followers_response import GetNumberOfFollowersResponse
from linebot.insight.models.get_number_of_message_deliveries_response import GetNumberOfMessageDeliveriesResponse
from linebot.insight.models.get_statistics_per_unit_response import GetStatisticsPerUnitResponse
from linebot.insight.models.get_statistics_per_unit_response_click import GetStatisticsPerUnitResponseClick
from linebot.insight.models.get_statistics_per_unit_response_message import GetStatisticsPerUnitResponseMessage
from linebot.insight.models.get_statistics_per_unit_response_overview import GetStatisticsPerUnitResponseOverview
from linebot.insight.models.subscription_period_tile import SubscriptionPeriodTile