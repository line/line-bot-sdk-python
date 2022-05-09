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

import unittest

import responses

from linebot import (
    LineBotApi
)
from linebot.models import (
    GenderInsight, AreaInsight, AgeInsight, AppTypeInsight, SubscriptionPeriodInsight
)


class TestLineBotApi(unittest.TestCase):
    def setUp(self):
        self.tested = LineBotApi('channel_secret')
        self.date = '20190101'
        self.request_id = 'f70dd685-499a-4231-a441-f24b8d4fba21'

    @responses.activate
    def test_get_insight_message_delivery(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/insight/message/delivery?date={date}'.format(date=self.date),
            json={
                'status': 'ready',
                'broadcast': 100,
                'targeting': 200,
                'autoResponse': 300,
                'welcomeResponse': 400,
                'chat': 500,
                'apiBroadcast': 600,
                'apiPush': 700,
                'apiMulticast': 800,
            },
            status=200
        )

        res = self.tested.get_insight_message_delivery(self.date)
        request = responses.calls[0].request
        self.assertEqual('GET', request.method)
        self.assertEqual('ready', res.status)
        self.assertEqual(100, res.broadcast)
        self.assertEqual(200, res.targeting)
        self.assertEqual(300, res.auto_response)
        self.assertEqual(400, res.welcome_response)
        self.assertEqual(500, res.chat)
        self.assertEqual(600, res.api_broadcast)
        self.assertEqual(700, res.api_push)
        self.assertEqual(800, res.api_multicast)
        self.assertEqual(None, res.api_reply)

    @responses.activate
    def test_get_insight_followers(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/insight/followers?date={date}'.format(date=self.date),
            json={
                'status': 'ready',
                'followers': 100,
                'targetedReaches': 200,
                'blocks': 300
            },
            status=200
        )

        res = self.tested.get_insight_followers(self.date)
        request = responses.calls[0].request
        self.assertEqual('GET', request.method)
        self.assertEqual('ready', res.status)
        self.assertEqual(100, res.followers)
        self.assertEqual(200, res.targeted_reaches)
        self.assertEqual(300, res.blocks)

    @responses.activate
    def test_get_insight_demographic(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/insight/demographic',
            json={
                'available': True,
                'genders': [
                    {
                        'gender': 'unknown',
                        'percentage': 37.6
                    },
                    {
                        'gender': 'male',
                        'percentage': 31.8
                    },
                    {
                        'gender': 'female',
                        'percentage': 30.6
                    }
                ],
                'ages': [
                    {
                        'age': 'unknown',
                        'percentage': 37.6
                    },
                    {
                        'age': 'from50',
                        'percentage': 17.3
                    },
                ],
                'areas': [
                    {
                        'area': 'unknown',
                        'percentage': 50.5
                    },
                    {
                        'area': 'Tokyo',
                        'percentage': 49.5
                    },
                ],
                'appTypes': [
                    {
                        'appType': 'ios',
                        'percentage': 62.4
                    },
                    {
                        'appType': 'android',
                        'percentage': 27.7
                    },
                    {
                        'appType': 'others',
                        'percentage': 9.9
                    }
                ],
                'subscriptionPeriods': [
                    {
                        'subscriptionPeriod': 'over365days',
                        'percentage': 96.4
                    },
                    {
                        'subscriptionPeriod': 'within365days',
                        'percentage': 1.9
                    },
                    {
                        'subscriptionPeriod': 'within180days',
                        'percentage': 1.2
                    },
                    {
                        'subscriptionPeriod': 'within90days',
                        'percentage': 0.5
                    },
                    {
                        'subscriptionPeriod': 'within30days',
                        'percentage': 0.1
                    },
                    {
                        'subscriptionPeriod': 'within7days',
                        'percentage': 0
                    }
                ]
            },
            status=200
        )

        res = self.tested.get_insight_demographic()
        request = responses.calls[0].request
        self.assertEqual('GET', request.method)
        self.assertEqual(True, res.available)
        self.assertIn(GenderInsight(gender='male', percentage=31.8), res.genders)
        self.assertIn(AgeInsight(age='from50', percentage=17.3), res.ages)
        self.assertIn(AreaInsight(area='Tokyo', percentage=49.5), res.areas)
        self.assertIn(AppTypeInsight(app_type='ios', percentage=62.4), res.app_types)
        self.assertIn(
            SubscriptionPeriodInsight(subscription_period='over365days', percentage=96.4),
            res.subscription_periods
        )

    @responses.activate
    def test_get_insight_message_event(self):
        json = {
            'overview': {
                'requestId': 'f70dd685-499a-4231-a441-f24b8d4fba21',
                'timestamp': 1568214000,
                'delivered': 32,
                'uniqueImpression': 4,
                'uniqueClick': None,
                'uniqueMediaPlayed': 2,
                'uniqueMediaPlayed100Percent': -1
            },
            'messages': [
                {
                    'seq': 1,
                    'impression': 18,
                    'mediaPlayed': 11,
                    'mediaPlayed25Percent': -1,
                    'mediaPlayed50Percent': -1,
                    'mediaPlayed75Percent': -1,
                    'mediaPlayed100Percent': -1,
                    'uniqueMediaPlayed': 2,
                    'uniqueMediaPlayed25Percent': -1,
                    'uniqueMediaPlayed50Percent': -1,
                    'uniqueMediaPlayed75Percent': -1,
                    'uniqueMediaPlayed100Percent': -1
                }
            ],
            'clicks': [
                {
                    'seq': 1,
                    'url': 'https://www.yahoo.co.jp/',
                    'click': -1,
                    'uniqueClick': -1,
                    'uniqueClickOfRequest': -1
                },
                {
                    'seq': 1,
                    'url': 'https://www.google.com/?hl=ja',
                    'click': -1,
                    'uniqueClick': -1,
                    'uniqueClickOfRequest': -1
                }
            ]
        }
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/insight/message/event?requestId={request_id}'.format(request_id=self.request_id),
            status=200,
            json=json,
        )

        res = self.tested.get_insight_message_event(self.request_id)
        request = responses.calls[0].request
        self.assertEqual('GET', request.method)
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/insight/message/event?requestId={request_id}'.format(request_id=self.request_id)
        )

        self.assertEqual(res.overview.timestamp, json['overview']['timestamp'])
        self.assertEqual(res.overview.unique_media_played_100_percent, json['overview']['uniqueMediaPlayed100Percent'])
        self.assertEqual(res.messages[0].seq, json['messages'][0]['seq'])
        self.assertEqual(res.messages[0].media_played_50_percent, json['messages'][0]['mediaPlayed50Percent'])
        self.assertEqual(res.clicks[0].url, json['clicks'][0]['url'])
        self.assertEqual(res.clicks[0].unique_click_of_request, json['clicks'][0]['uniqueClickOfRequest'])

    @responses.activate
    def test_get_statistics_per_unit(self):
        json = {
            'overview': {
                "uniqueImpression": 40,
                "uniqueClick": 30,
                "uniqueMediaPlayed": 25,
                "uniqueMediaPlayed100Percent": None
            },
            'messages': [
                {
                    'seq': 1,
                    'impression': 42,
                    'mediaPlayed': 30,
                    'mediaPlayed25Percent': None,
                    'mediaPlayed50Percent': None,
                    'mediaPlayed75Percent': None,
                    'mediaPlayed100Percent': None,
                    'uniqueMediaPlayed': 25,
                    'uniqueMediaPlayed25Percent': None,
                    'uniqueMediaPlayed50Percent': None,
                    'uniqueMediaPlayed75Percent': None,
                    'uniqueMediaPlayed100Percent': None
                }
            ],
            'clicks': [
                {
                    'seq': 1,
                    'url': 'https://developers.line.biz/',
                    'click': 35,
                    'uniqueClick': 25,
                    'uniqueClickOfRequest': None
                },
                {
                    'seq': 1,
                    'url': 'https://www.line-community.me/',
                    'click': 20,
                    'uniqueClick': None,
                    'uniqueClickOfRequest': None
                }
            ]
        }
        request_param = {
            'custom_aggregation_unit': 'promotion_a',
            'from': '20210301',
            'to': '20210331'
        }
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/insight/message/event/aggregation'
            '?customAggregationUnit={custom_aggregation_unit}'
            '&from={from_date}&to={to_date}'.format(
                custom_aggregation_unit=request_param['custom_aggregation_unit'],
                from_date=request_param['from'], to_date=request_param['to']),
            status=200,
            json=json,
        )

        res = self.tested.get_statistics_per_unit(
            request_param['custom_aggregation_unit'], request_param['from'], request_param['to'])
        request = responses.calls[0].request
        self.assertEqual('GET', request.method)
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/insight/message/event/aggregation'
            '?customAggregationUnit={custom_aggregation_unit}'
            '&from={from_date}&to={to_date}'.format(
                custom_aggregation_unit=request_param['custom_aggregation_unit'],
                from_date=request_param['from'], to_date=request_param['to'])
        )

        self.assertEqual(res.overview.unique_media_played_100_percent, json['overview']['uniqueMediaPlayed100Percent'])
        self.assertEqual(res.messages[0].seq, json['messages'][0]['seq'])
        self.assertEqual(res.messages[0].media_played_50_percent, json['messages'][0]['mediaPlayed50Percent'])
        self.assertEqual(res.clicks[0].url, json['clicks'][0]['url'])
        self.assertEqual(res.clicks[0].unique_click_of_request, json['clicks'][0]['uniqueClickOfRequest'])


if __name__ == '__main__':
    unittest.main()
