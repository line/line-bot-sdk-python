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
    URITemplateAction,
    RichMenu, RichMenuSize, RichMenuArea, RichMenuBounds
)


class TestLineBotApi(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.tested = LineBotApi('channel_secret')

        self.rich_menu_id = 'richmenu-0000000000'
        self.user_id = 'userid'
        self.rich_menu = RichMenu(
            size=RichMenuSize(
                width=2500,
                height=1686
            ),
            selected=False,
            name="nice richmenu",
            chatBarText="touch me",
            areas=[
                RichMenuArea(
                    RichMenuBounds(
                        x=0,
                        y=0,
                        width=833,
                        height=843
                    ),
                    URITemplateAction(
                        uri='line://nv/location'
                    )
                )
            ]
        )

    @responses.activate
    def test_get_rich_menu(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/rich_menu_id',
            json={
                "richMenuId": "rich_menu_id",
                "size": {
                    "width": 2500,
                    "height": 1686
                },
                "selected": False,
                "name": "name",
                "chatBarText": "chatBarText",
                "areas": [
                    {
                        "bounds": {
                            "x": 0,
                            "y": 0,
                            "width": 2500,
                            "height": 1686
                        },
                        "action": {
                            "type": "postback",
                            "data": "action=buy&itemid=123"
                        }
                    }
                ]
            },
            status=200
        )

        rich_menu = self.tested.get_rich_menu('rich_menu_id')
        print(rich_menu)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/rich_menu_id'
        )

        self.assertEqual(rich_menu.rich_menu_id, 'rich_menu_id')
        self.assertEqual(rich_menu.size.width, 2500)
        self.assertEqual(rich_menu.size.height, 1686)
        self.assertEqual(rich_menu.selected, False)
        self.assertEqual(rich_menu.name, 'name')
        self.assertEqual(rich_menu.chat_bar_text, 'chatBarText')
        self.assertEqual(rich_menu.areas[0].bounds.x, 0)
        self.assertEqual(rich_menu.areas[0].bounds.y, 0)
        self.assertEqual(rich_menu.areas[0].bounds.width, 2500)
        self.assertEqual(rich_menu.areas[0].bounds.height, 1686)
        self.assertEqual(rich_menu.areas[0].action.type, 'postback')
        self.assertEqual(rich_menu.areas[0].action.data, 'action=buy&itemid=123')

    @responses.activate
    def test_create_rich_menu(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu',
            json={"richMenuId": "richMenuId"}, status=200
        )

        rich_menu = RichMenu(
            size=RichMenuSize(
                width=2500,
                height=1686
            ),
            selected=False,
            name="nice richmenu",
            chatBarText="touch me",
            areas=[
                RichMenuArea(
                    RichMenuBounds(
                        x=0,
                        y=0,
                        width=833,
                        height=843
                    ),
                    URITemplateAction(
                        uri='line://nv/location'
                    )
                )
            ]
        )

        result = self.tested.create_rich_menu(rich_menu)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu'
        )
        self.assertEqual(result, "richMenuId")

    @responses.activate
    def test_delete_rich_menu(self):
        responses.add(
            responses.DELETE,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/rich_menu_id',
            json={}, status=200
        )

        self.tested.delete_rich_menu('rich_menu_id')

        request = responses.calls[0].request
        self.assertEqual(request.method, 'DELETE')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/rich_menu_id'
        )

    @responses.activate
    def test_get_rich_menu_id_of_user(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/user/user_id/richmenu',
            json={"richMenuId": "richMenuId"}, status=200
        )

        result = self.tested.get_rich_menu_id_of_user('user_id')

        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/user/user_id/richmenu'
        )
        self.assertEqual(result, "richMenuId")

    @responses.activate
    def test_link_rich_menu_to_user(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/user/user_id/richmenu/rich_menu_id',
            json={}, status=200
        )

        self.tested.link_rich_menu_to_user('user_id', 'rich_menu_id')

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/user/user_id/richmenu/rich_menu_id'
        )

    @responses.activate
    def test_unlink_rich_menu_from_user(self):
        responses.add(
            responses.DELETE,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/user/user_id/richmenu',
            json={}, status=200
        )

        self.tested.unlink_rich_menu_from_user('user_id')

        request = responses.calls[0].request
        self.assertEqual(request.method, 'DELETE')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/user/user_id/richmenu'
        )

    @responses.activate
    def test_get_rich_menu_list(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/list',
            json={
                "richmenus": [
                    {
                        "richMenuId": "rich_menu_id",
                        "size": {
                            "width": 2500,
                            "height": 1686
                        },
                        "selected": False,
                        "name": "name",
                        "chatBarText": "chatBarText",
                        "areas": [
                            {
                                "bounds": {
                                    "x": 0,
                                    "y": 0,
                                    "width": 2500,
                                    "height": 1686
                                },
                                "action": {
                                    "type": "postback",
                                    "data": "action=buy&itemid=123"
                                }
                            }
                        ]
                    }
                ]
            },
            status=200
        )

        rich_menus = self.tested.get_rich_menu_list()

        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/list'
        )
        self.assertEqual(rich_menus[0].rich_menu_id, 'rich_menu_id')
        self.assertEqual(rich_menus[0].size.width, 2500)
        self.assertEqual(rich_menus[0].size.height, 1686)
        self.assertEqual(rich_menus[0].selected, False)
        self.assertEqual(rich_menus[0].name, 'name')
        self.assertEqual(rich_menus[0].chat_bar_text, 'chatBarText')
        self.assertEqual(rich_menus[0].areas[0].bounds.x, 0)
        self.assertEqual(rich_menus[0].areas[0].bounds.y, 0)
        self.assertEqual(rich_menus[0].areas[0].bounds.width, 2500)
        self.assertEqual(rich_menus[0].areas[0].bounds.height, 1686)
        self.assertEqual(rich_menus[0].areas[0].action.type, 'postback')
        self.assertEqual(rich_menus[0].areas[0].action.data, 'action=buy&itemid=123')


if __name__ == '__main__':
    unittest.main()
