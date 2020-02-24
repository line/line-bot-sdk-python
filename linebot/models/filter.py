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

"""linebot.models.filter module."""

from __future__ import unicode_literals

from abc import ABCMeta

from future.utils import with_metaclass

from .base import Base


class Filter(with_metaclass(ABCMeta, Base)):
    """Filter.

    https://developers.line.biz/en/reference/messaging-api/#narrowcast-demographic-filter

    A filter is the top-level structure of a demographic element.
    """

    def __init__(self, demographic=None, **kwargs):
        """__init__ method.

        :param demographic: Combination of different criteria using logical
            operator objects.
        :type demographic: :py:class:`linebot.model.DemographicFilter` |
            :py:class:`linebot.model.Operator`
        :param kwargs:
        """
        super(Filter, self).__init__(**kwargs)

        self.demographic = demographic


class DemographicFilter(Filter):
    """DemographicFilter.

    https://developers.line.biz/en/reference/messaging-api/#narrowcast-demographic-filter

    Demographic filter objects represent criteria (e.g. age, gender, OS, region,
    and friendship duration) on which to filter the list of recipients.
    You can filter recipients based on a combination of different criteria using
    logical operator objects.
    """

    def __init__(self, **kwargs):
        """__init__ method.

        :param kwargs:
        """
        super(DemographicFilter, self).__init__(**kwargs)

        self.type = None


class GenderFilter(DemographicFilter):
    """GenderFilter."""

    def __init__(self, one_of=[], **kwargs):
        """__init__ method.

        :param one_of: Send messages to users of a given gender. One of:
            male: Users who identify as male
            female: Users who identify as female
        :type one_of: list[str]
        """
        super(GenderFilter, self).__init__(**kwargs)

        self.type = "gender"
        self.one_of = one_of


class AppTypeFilter(DemographicFilter):
    """AppTypeFilter."""

    def __init__(self, one_of=[], **kwargs):
        """__init__ method.

        :param one_of: Send messages to users of the specified OS. One of:
            ios: Users who using iOS.
            android: Users who using Android.
        :type one_of: list[str]
        """
        super(AppTypeFilter, self).__init__(**kwargs)

        self.type = "appType"
        self.one_of = one_of


class AreaFilter(DemographicFilter):
    """AreaFilter."""

    def __init__(self, one_of=[], **kwargs):
        """__init__ method.

        :param one_of: Send messages to users in the specified region.
        :type one_of: list[str]
        """
        super(AreaFilter, self).__init__(**kwargs)

        self.type = "area"
        self.one_of = one_of


class AgeFilter(DemographicFilter):
    """AgeFilter.

    This lets you filter recipients with a given age range.
    """

    def __init__(self, gte=None, lt=None, **kwargs):
        """__init__ method.

        Be sure to specify either gte, lt, or both.

        :param gte: Send messages to users at least as old as the specified age.
        :type gte: str
        :param lt: Send messages to users younger than the specified age.
            You can specify the same values as for the gte property.
        :type lt: str
        """
        super(AgeFilter, self).__init__(**kwargs)

        self.type = "age"
        self.gte = gte
        self.lt = lt


class SubscriptionPeriodFilter(DemographicFilter):
    """SubscriptionPeriodFilter.

    This lets you filter recipients with a given range of friendship durations.
    """

    def __init__(self, gte=None, lt=None, **kwargs):
        """__init__ method.

        Be sure to specify either gte, lt, or both.

        :param gte: Send messages to users who have been friends of yours for
            at least the specified number of days
        :type gte: str
        :param lt: Send messages to users who have been friends of yours for
            less than the specified number of days.
            You can specify the same values as for the gte property.
        :type lt: str
        """
        super(SubscriptionPeriodFilter, self).__init__(**kwargs)

        self.type = "subscriptionPeriod"
        self.gte = gte
        self.lt = lt
