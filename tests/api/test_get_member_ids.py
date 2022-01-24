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


class TestLineBotApi(unittest.TestCase):
    def setUp(self):
        self.tested = LineBotApi('channel_secret')

    @responses.activate
    def test_get_group_member_ids(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/group/group_id/members/ids',
            json={
                'memberIds': ['U1', 'U2']
            },
            status=200
        )

        member_ids_response = self.tested.get_group_member_ids('group_id')

        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/group/group_id/members/ids')
        self.assertEqual(member_ids_response.member_ids, ['U1', 'U2'])
        self.assertEqual(member_ids_response.next, None)

    @responses.activate
    def test_get_group_member_ids_with_start(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/group/group_id/members/ids',
            json={
                'memberIds': ['U1', 'U2'],
                'next': 'continuationToken2'
            },
            status=200
        )

        member_ids_response = self.tested.get_group_member_ids('group_id',
                                                               start='continuationToken1')

        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/group/group_id/members/ids?start=continuationToken1')
        self.assertEqual(member_ids_response.member_ids, ['U1', 'U2'])
        self.assertEqual(member_ids_response.next, 'continuationToken2')

    @responses.activate
    def test_get_room_member_ids(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/room/room_id/members/ids',
            json={
                'memberIds': ['U1', 'U2']
            },
            status=200
        )

        member_ids_response = self.tested.get_room_member_ids('room_id')

        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/room/room_id/members/ids')
        self.assertEqual(member_ids_response.member_ids, ['U1', 'U2'])
        self.assertEqual(member_ids_response.next, None)

    @responses.activate
    def test_get_room_member_ids_with_start(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/room/room_id/members/ids',
            json={
                'memberIds': ['U1', 'U2'],
                'next': 'continuationToken2'
            },
            status=200
        )

        member_ids_response = self.tested.get_room_member_ids('room_id',
                                                              start='continuationToken1')

        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/room/room_id/members/ids?start=continuationToken1')
        self.assertEqual(member_ids_response.member_ids, ['U1', 'U2'])
        self.assertEqual(member_ids_response.next, 'continuationToken2')

    @responses.activate
    def test_get_follower_user_ids(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/followers/ids',
            json={
                'userIds': ['U1', 'U2']
            },
            status=200
        )

        member_ids_response = self.tested.get_followers_ids()

        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/followers/ids?limit=300')
        self.assertEqual(member_ids_response.user_ids, ['U1', 'U2'])
        self.assertEqual(member_ids_response.next, None)

    @responses.activate
    def test_get_follower_user_ids_with_start(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/followers/ids',
            json={
                'userIds': ['U1', 'U2'],
                'next': 'continuationToken2'
            },
            status=200
        )

        member_ids_response = self.tested.get_followers_ids(start='continuationToken1')

        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/followers/ids?limit=300&start=continuationToken1')
        self.assertEqual(member_ids_response.user_ids, ['U1', 'U2'])
        self.assertEqual(member_ids_response.next, 'continuationToken2')

    @responses.activate
    def test_get_follower_user_ids_with_start_and_limit(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/followers/ids',
            json={
                'userIds': ['U1', 'U2'],
                'next': 'continuationToken2'
            },
            status=200
        )

        member_ids_response = self.tested.get_followers_ids(limit=2, start='continuationToken1')

        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/followers/ids?limit=2&start=continuationToken1')
        self.assertEqual(member_ids_response.user_ids, ['U1', 'U2'])
        self.assertEqual(member_ids_response.next, 'continuationToken2')


if __name__ == '__main__':
    unittest.main()
