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

from __future__ import unicode_literals, absolute_import

import json
import unittest

import responses

from linebot import (
    LineBotApi
)
from linebot.models import (
    TextSendMessage,
    Limit,
    OpAND,
    OpOR,
    OpNOT,
    GenderFilter,
    DemographicFilter,
    AppTypeFilter,
    AreaFilter,
    AgeFilter,
    AudienceRecipient,
    SubscriptionPeriodFilter,
    NarrowcastResponse,
    MessageProgressNarrowcastResponse,
)


class TestNarrowcastMessage(unittest.TestCase):
    def setUp(self):
        self.tested = LineBotApi('channel_secret')
        self.maxDiff = None

        # test data
        self.text_message = TextSendMessage(text='Hello, world')
        self.message = [{"type": "text", "text": "Hello, world"}]

    @responses.activate
    def test_narrowcast_text_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/narrowcast',
            json={}, status=200,
            headers={'X-Line-Request-Id': 'request_id_test'},
        )

        response = self.tested.narrowcast(
            self.text_message,
            recipient=OpAND(
                AudienceRecipient(group_id=5614991017776),
                OpNOT(AudienceRecipient(group_id=4389303728991))
            ),
            filter=DemographicFilter(
                OpOR(
                    OpAND(
                        GenderFilter(one_of=["male", "female"]),
                        AgeFilter(gte="age_20", lt="age_25"),
                        AppTypeFilter(one_of=["android", "ios"]),
                        AreaFilter(one_of=["jp_23", "jp_05"]),
                        SubscriptionPeriodFilter(gte="day_7", lt="day_30")
                    ),
                    OpAND(
                        AgeFilter(gte="age_35", lt="age_40"),
                        OpNOT(GenderFilter(one_of=["male"]))
                    )
                )
            ),
            limit=Limit(max=100),
        )

        request = responses.calls[0].request
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/narrowcast')
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            json.loads(request.body),
            {
                "messages": self.message,
                "recipient": {
                    "type": "operator",
                    "and": [
                        {
                            'audienceGroupId': 5614991017776,
                            'type': 'audience'
                        },
                        {
                            "type": "operator",
                            "not": {
                                "type": "audience",
                                "audienceGroupId": 4389303728991
                            }
                        }
                    ]
                },
                "filter": {
                    "demographic": {
                        "type": "operator",
                        "or": [
                            {
                                "type": "operator",
                                "and": [
                                    {
                                        "type": "gender",
                                        "oneOf": [
                                            "male",
                                            "female"
                                        ]
                                    },
                                    {
                                        "type": "age",
                                        "gte": "age_20",
                                        "lt": "age_25"
                                    },
                                    {
                                        "type": "appType",
                                        "oneOf": [
                                            "android",
                                            "ios"
                                        ]
                                    },
                                    {
                                        "type": "area",
                                        "oneOf": [
                                            "jp_23",
                                            "jp_05"
                                        ]
                                    },
                                    {
                                        "type": "subscriptionPeriod",
                                        "gte": "day_7",
                                        "lt": "day_30"
                                    }
                                ]
                            },
                            {
                                "type": "operator",
                                "and": [
                                    {
                                        "type": "age",
                                        "gte": "age_35",
                                        "lt": "age_40"
                                    },
                                    {
                                        "type": "operator",
                                        "not": {
                                            "type": "gender",
                                            "oneOf": [
                                                "male"
                                            ]
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                },
                "limit": {
                    "max": 100
                }
            }
        )
        self.assertEqual('request_id_test', response.request_id)


if __name__ == '__main__':
    unittest.main()
