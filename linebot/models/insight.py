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

"""linebot.models.insight module."""

from __future__ import unicode_literals

from abc import ABCMeta

from future.utils import with_metaclass

from .base import Base


class DemographicInsight(with_metaclass(ABCMeta, Base)):
    """Abstract Base Class of DemographicInsight."""

    def __init__(self, percentage=None, **kwargs):
        """__init__ method.

        :param float percentage: Percentage.
        :param kwargs:
        """
        super(DemographicInsight, self).__init__(**kwargs)
        self.percentage = percentage


class GenderInsight(DemographicInsight):
    """GenderInsight."""

    def __init__(self, percentage=None, gender=None, **kwargs):
        """__init__ method.

        :param float percentage: Percentage.
        :param str gender: Gender
        :param kwargs:
        """
        super(GenderInsight, self).__init__(percentage=percentage, **kwargs)

        self.gender = gender


class AgeInsight(DemographicInsight):
    """AgeInsight."""

    def __init__(self, percentage=None, age=None, **kwargs):
        """__init__ method.

        :param float percentage: Percentage.
        :param str age: Age
        :param kwargs:
        """
        super(AgeInsight, self).__init__(percentage=percentage, **kwargs)

        self.age = age


class AreaInsight(DemographicInsight):
    """AreaInsight."""

    def __init__(self, percentage=None, area=None, **kwargs):
        """__init__ method.

        :param float percentage: Percentage.
        :param str area: Area
        :param kwargs:
        """
        super(AreaInsight, self).__init__(percentage=percentage, **kwargs)

        self.area = area


class AppTypeInsight(DemographicInsight):
    """AppTypeInsight."""

    def __init__(self, percentage=None, app_type=None, **kwargs):
        """__init__ method.

        :param float percentage: Percentage.
        :param str app_type: OS
        :param kwargs:
        """
        super(AppTypeInsight, self).__init__(percentage=percentage, **kwargs)

        self.app_type = app_type


class SubscriptionPeriodInsight(DemographicInsight):
    """SubscriptionPeriodInsight."""

    def __init__(self, percentage=None, subscription_period=None, **kwargs):
        """__init__ method.

        :param float percentage: Percentage.
        :param str subscription_period: Friendship duration
        :param kwargs:
        """
        super(SubscriptionPeriodInsight, self).__init__(percentage=percentage, **kwargs)

        self.subscription_period = subscription_period


class MessageStatistics(Base):
    """MessageStatistics."""

    def __init__(self, request_id=None, timestamp=None, delivered=None,
                 unique_impression=None, unique_click=None, unique_media_played=None,
                 unique_media_played_100_percent=None, **kwargs):
        """__init__ method.

        :param str request_id: Request ID.
        :param int timestamp: UNIX timestamp for message delivery time.
        :param int delivered: Number of messages delivered. This property shows values
            of less than 20.
        :param int unique_impression: Number of people who opened the message,
            meaning they displayed at least 1 bubble.
        :param int unique_click: Number of people who opened any URL in the message.
        :param int unique_media_played: Number of people who started playing any video
            or audio in the message.
        :param int unique_media_played_100_percent: Number of people who played the entirety of
            any video or audio in the message.
        """
        super(MessageStatistics, self).__init__(**kwargs)

        self.request_id = request_id
        self.timestamp = timestamp
        self.delivered = delivered
        self.unique_impression = unique_impression
        self.unique_click = unique_click
        self.unique_media_played = unique_media_played
        self.unique_media_played_100_percent = unique_media_played_100_percent


class MessageInsight(Base):
    """MessageInsight."""

    def __init__(self, seq=None, impression=None, media_played=None,
                 media_played_25_percent=None, media_played_50_percent=None,
                 media_played_75_percent=None, media_played_100_percent=None,
                 unique_media_played=None, unique_media_played_25_percent=None,
                 unique_media_played_50_percent=None, unique_media_played_75_percent=None,
                 unique_media_played_100_percent=None, **kwargs):
        """__init__ method.

        :param int seq: Bubble's serial number.
        :param int impression: Number of times the bubble was displayed.
        :param int media_played: Number of times audio or video in the bubble started playing.
        :param int media_played_25_percent: Number of times audio or video
            in the bubble was played from start to 25%.
        :param int media_played_50_percent: Number of times audio or video
            in the bubble was played from start to 50%.
        :param int media_played_75_percent: Number of times audio or video
            in the bubble was played from start to 75%.
        :param int media_played_100_percent: Number of times audio or video
            in the bubble was played in its entirety.
        :param int unique_media_played: Number of people that started playing
            audio or video in the bubble.
        :param int unique_media_played_25_percent: Number of people that played
            audio or video in the bubble from start to 25%.
        :param int unique_media_played_50_percent: Number of people that played
            audio or video in the bubble from start to 50%.
        :param int unique_media_played_75_percent: Number of people that played
            audio or video in the bubble from start to 75%.
        :param int unique_media_played_100_percent: Number of people that played
            audio or video in the bubble in its entirety.
        """
        super(MessageInsight, self).__init__(**kwargs)

        self.seq = seq
        self.impression = impression
        self.media_played = media_played
        self.media_played_25_percent = media_played_25_percent
        self.media_played_50_percent = media_played_50_percent
        self.media_played_75_percent = media_played_75_percent
        self.media_played_100_percent = media_played_100_percent
        self.unique_media_played = unique_media_played
        self.unique_media_played_25_percent = unique_media_played_25_percent
        self.unique_media_played_50_percent = unique_media_played_50_percent
        self.unique_media_played_75_percent = unique_media_played_75_percent
        self.unique_media_played_100_percent = unique_media_played_100_percent


class ClickInsight(Base):
    """ClickInsight."""

    def __init__(self, seq=None, url=None, click=None, unique_click=None,
                 unique_click_of_request=None, **kwargs):
        """__init__ method.

        :param int seq: The URL's serial number.
        :param str url: URL.
        :param int click: Number of times the URL was opened.
        :param int unique_click: Number of people that opened the URL.
        :param int unique_click_of_request: Number of people who opened this url
            through any link in the message.
        """
        super(ClickInsight, self).__init__(**kwargs)

        self.seq = seq
        self.url = url
        self.click = click
        self.unique_click = unique_click
        self.unique_click_of_request = unique_click_of_request
