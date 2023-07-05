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
    And,
    Or,
    Not,
    Filter,
    GenderFilter,
    AppTypeFilter,
    AreaFilter,
    AgeFilter,
    AudienceRecipient,
    SubscriptionPeriodFilter,
    RedeliveryRecipient,
)


class TestNarrowcastMessage(unittest.TestCase):
    def setUp(self):
        self.tested = LineBotApi('channel_secret')
        self.maxDiff = None
        self.request_id = 'f70dd685-499a-4231-a441-f24b8d4fba21'

        # test data
        self.text_message = TextSendMessage(text='Hello, world')
        self.message = [{"type": "text", "text": "Hello, world"}]

    @responses.activate
    def test_narrowcast_simple_text_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/narrowcast',
            json={}, status=200,
            headers={'X-Line-Request-Id': 'request_id_test'},
        )

        self.tested.narrowcast(
            self.text_message,
            recipient=AudienceRecipient(group_id=5614991017776),
            filter=Filter(demographic=AgeFilter(gte="age_35", lt="age_40")),
            limit=Limit(max=10),
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
                    'audienceGroupId': 5614991017776,
                    'type': 'audience'
                },
                "filter": {
                    "demographic": {
                        "type": "age",
                        "gte": "age_35",
                        "lt": "age_40"
                    }
                },
                "limit": {
                    "max": 10,
                    "upToRemainingQuota": False,
                },
                "notificationDisabled": False,
            }
        )

    @responses.activate
    def test_narrowcast_redelivery_recipient_text_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/narrowcast',
            json={}, status=200,
        )

        self.tested.narrowcast(
            self.text_message,
            recipient=And(
                AudienceRecipient(group_id=5614991017776),
                Not(
                    RedeliveryRecipient(request_id='request_id_test')
                )
            ),
            filter=Filter(demographic=AgeFilter(gte="age_35", lt="age_40")),
            limit=Limit(max=10),
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
                            "type": "audience",
                            "audienceGroupId": 5614991017776
                        },
                        {
                            "type": "operator",
                            "not": {
                                "type": "redelivery",
                                "requestId": "request_id_test"
                            }
                        }
                    ]
                },
                "filter": {
                    "demographic": {
                        "type": "age",
                        "gte": "age_35",
                        "lt": "age_40"
                    }
                },
                "limit": {
                    "max": 10,
                    "upToRemainingQuota": False,
                },
                "notificationDisabled": False,
            }
        )

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
            recipient=And(
                AudienceRecipient(group_id=5614991017776),
                Not(AudienceRecipient(group_id=4389303728991))
            ),
            filter=Filter(
                demographic=Or(
                    And(
                        GenderFilter(one_of=["male", "female"]),
                        AgeFilter(gte="age_20", lt="age_25"),
                        AppTypeFilter(one_of=["android", "ios"]),
                        AreaFilter(one_of=["jp_23", "jp_05"]),
                        SubscriptionPeriodFilter(gte="day_7", lt="day_30")
                    ),
                    And(
                        AgeFilter(gte="age_35", lt="age_40"),
                        Not(GenderFilter(one_of=["male"]))
                    )
                )
            ),
            limit=Limit(max=100, up_to_remaining_quota=True),
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
                    "max": 100,
                    "upToRemainingQuota": True,
                },
                "notificationDisabled": False,
            }
        )
        self.assertEqual('request_id_test', response.request_id)

    @responses.activate
    def test_narrowcast_text_message_with_retry_key(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/narrowcast',
            json={}, status=200,
            headers={
                'X-Line-Request-Id': 'request_id_test',
                'X-Line-Retry-Key': '123e4567-e89b-12d3-a456-426614174000'
            },
        )

        response = self.tested.narrowcast(
            self.text_message,
            recipient=And(
                AudienceRecipient(group_id=5614991017776),
                Not(AudienceRecipient(group_id=4389303728991))
            ),
            filter=Filter(
                demographic=Or(
                    And(
                        GenderFilter(one_of=["male", "female"])
                    )
                )
            ),
            limit=Limit(max=100, up_to_remaining_quota=True),
            retry_key='123e4567-e89b-12d3-a456-426614174000',
        )

        request = responses.calls[0].request
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/narrowcast')
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.headers['X-Line-Retry-Key'],
            '123e4567-e89b-12d3-a456-426614174000'
        )
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
                                    }
                                ]
                            }
                        ]
                    }
                },
                "limit": {
                    "max": 100,
                    "upToRemainingQuota": True,
                },
                "notificationDisabled": False,
            }
        )
        self.assertEqual('request_id_test', response.request_id)

    @responses.activate
    def test_get_progress_status_narrowcast(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/message/progress/narrowcast?requestId={request_id}'.format(
                request_id=self.request_id),
            json={'phase': 'waiting'}, status=200,
        )
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/message/progress/narrowcast?requestId={request_id}'.format(
                request_id=self.request_id),
            json={
                'phase': 'succeeded',
                'successCount': 10,
                'failureCount': 0,
                'targetCount': 10,
            }, status=200,
        )

        res = self.tested.get_progress_status_narrowcast(self.request_id)
        request = responses.calls[0].request
        self.assertEqual('GET', request.method)
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/message/progress/narrowcast?requestId={request_id}'.format(
                request_id=self.request_id)
        )

        self.assertEqual(res.phase, 'waiting')

        res = self.tested.get_progress_status_narrowcast(self.request_id)
        request = responses.calls[1].request
        self.assertEqual('GET', request.method)
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/message/progress/narrowcast?requestId={request_id}'.format(
                request_id=self.request_id)
        )

        self.assertEqual(res.phase, 'succeeded')
        self.assertEqual(res.success_count, 10)
        self.assertEqual(res.failure_count, 0)
        self.assertEqual(res.target_count, 10)


if __name__ == '__main__':
    unittest.main()
