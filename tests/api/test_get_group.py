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
    def test_get_group_summary(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/group/group_id/summary',
            json={
                "groupId": "Ca56f94637c...",
                "groupName": "Group name",
                "pictureUrl": "https://example.com/abcdefghijklmn"
            },
            status=200
        )

        group = self.tested.get_group_summary('group_id')

        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/group/group_id/summary')
        self.assertEqual(group.group_id, 'Ca56f94637c...')
        self.assertEqual(group.group_name, 'Group name')
        self.assertEqual(group.picture_url, 'https://example.com/abcdefghijklmn')

    @responses.activate
    def test_get_group_members_count(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/group/group_id/members/count',
            json={"count": 3},
            status=200
        )

        count = self.tested.get_group_members_count('group_id')

        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/group/group_id/members/count')
        self.assertEqual(count, 3)


if __name__ == '__main__':
    unittest.main()
