# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the 'License'); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an 'AS IS' BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from __future__ import unicode_literals, absolute_import

import unittest

from linebot.models import (
    GenderFilter,
    AppTypeFilter,
    AreaFilter,
    AgeFilter,
    SubscriptionPeriodFilter
)
from tests.models.serialize_test_case import SerializeTestCase


class TestFilter(SerializeTestCase):
    def test_gender_filter(self):
        arg = {
            "one_of": ["male", "female"]
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.GENDER),
            GenderFilter(**arg).as_json_dict()
        )

    def test_app_type_filter(self):
        arg = {
            "one_of": ["ios", "android"]
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.APP_TYPE),
            AppTypeFilter(**arg).as_json_dict()
        )

    def test_age_filter(self):
        arg = {
            "gte": "age_35",
            "lt": "age_40",
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.AGE),
            AgeFilter(**arg).as_json_dict()
        )

    def test_area_filter(self):
        arg = {
            "one_of": ["jp_34", "jp_05"]
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.AREA),
            AreaFilter(**arg).as_json_dict()
        )

    def test_subscription_period_filter(self):
        arg = {
            "gte": "day_7",
            "lt": "day_30",
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.SUBSCRIPTION_PERIOD),
            SubscriptionPeriodFilter(**arg).as_json_dict()
        )


if __name__ == '__main__':
    unittest.main()
