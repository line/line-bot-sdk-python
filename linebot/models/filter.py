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

    def __init__(self, **kwargs):
        """__init__ method.

        :param kwargs:
        """
        super(Filter, self).__init__(**kwargs)

        self.type = None


class DemographicFilter(Filter):
    """Demographic.

    https://developers.line.biz/en/reference/messaging-api/#narrowcast-demographic-filter

    A demogrphic filter is the top-level structure of a demographic element.
    """

    def __init__(self, condition=None, **kwargs):
        """__init__ method.

        :param kwargs:
        """
        super(DemographicFilter, self).__init__(**kwargs)

        self.demographic = condition


class GenderFilter(Filter):
    """GenderFilter
    """

    def __init__(self, one_of=[], **kwargs):
        """__init__ method.

        :param header: Style of the header block
        :type header: :py:class:`linebot.models.flex_message.BlockStyle`
        """
        super(GenderFilter, self).__init__(**kwargs)

        self.type = "gender"
        self.one_of = one_of


class AppTypeFilter(Filter):
    """AppTypeFilter
    """

    def __init__(self, one_of=[], **kwargs):
        """__init__ method.

        """
        super(AppTypeFilter, self).__init__(**kwargs)

        self.type = "appType"
        self.one_of = one_of


class AreaFilter(Filter):
    """AreaFilter
    """

    def __init__(self, one_of=[], **kwargs):
        """__init__ method.

        """
        super(AreaFilter, self).__init__(**kwargs)

        self.type = "area"
        self.one_of = one_of


class AgeFilter(Filter):
    """AgeFilter
    """

    def __init__(self, gte=None, lt=None, **kwargs):
        """__init__ method.

        """
        super(AgeFilter, self).__init__(**kwargs)

        self.type = "age"
        self.gte = gte
        self.lt = lt


class SubscriptionPeriodFilter(Filter):
    """SubscriptionPeriodFilter
    """

    def __init__(self, gte=None, lt=None, **kwargs):
        """__init__ method.

        """
        super(SubscriptionPeriodFilter, self).__init__(**kwargs)

        self.type = "subscriptionPeriod"
        self.gte = gte
        self.lt = lt
