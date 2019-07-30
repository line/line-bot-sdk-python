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
