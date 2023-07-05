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
    URITemplateAction,
    RichMenu, RichMenuSize, RichMenuArea, RichMenuBounds
)
from linebot.models.actions import RichMenuSwitchAction


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
                        uri='https://line.me/R/nv/location/'
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
    def test_validate_rich_menu_object(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/validate',
            json={}, status=200
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
                        uri='https://line.me/R/nv/location/'
                    )
                )
            ]
        )

        self.tested.validate_rich_menu_object(rich_menu)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/validate'
        )

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
                        uri='https://line.me/R/nv/location/'
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

    @responses.activate
    def test_link_rich_menu_to_users(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/richmenu/bulk/link',
            json={}, status=202
        )

        self.tested.link_rich_menu_to_users(['user_id1', 'user_id2'], 'rich_menu_id')

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/bulk/link'
        )
        self.assertEqual(
            json.loads(request.body),
            {
                "richMenuId": "rich_menu_id",
                "userIds": ["user_id1", "user_id2"],
            }
        )

    @responses.activate
    def test_unlink_rich_menu_to_users(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/richmenu/bulk/unlink',
            json={}, status=202
        )

        self.tested.unlink_rich_menu_from_users(['user_id1', 'user_id2'], 'rich_menu_id')

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/bulk/unlink'
        )
        self.assertEqual(
            json.loads(request.body),
            {
                "userIds": ["user_id1", "user_id2"],
            }
        )

    @responses.activate
    def test_set_default_rich_menu(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/user/all/richmenu/rich_menu_id',
            json={}, status=200
        )

        self.tested.set_default_rich_menu('rich_menu_id')

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/user/all/richmenu/rich_menu_id'
        )

    @responses.activate
    def test_get_default_rich_menu(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/user/all/richmenu',
            json={"richMenuId": "richMenuId"}, status=200
        )

        result = self.tested.get_default_rich_menu()

        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/user/all/richmenu'
        )
        self.assertEqual(result, "richMenuId")

    @responses.activate
    def test_cancel_default_rich_menu(self):
        responses.add(
            responses.DELETE,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/user/all/richmenu',
            json={}, status=200
        )

        self.tested.cancel_default_rich_menu()

        request = responses.calls[0].request
        self.assertEqual(request.method, 'DELETE')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/user/all/richmenu'
        )

    @responses.activate
    def test_get_rich_menu_image(self):
        rich_menu_id = '1234'
        body = b'hogieoidksk'
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_DATA_ENDPOINT +
            '/v2/bot/richmenu/{rich_menu_id}/content'.format(rich_menu_id=rich_menu_id),
            body=body, status=200
        )

        res = self.tested.get_rich_menu_image(rich_menu_id)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_DATA_ENDPOINT +
            '/v2/bot/richmenu/{rich_menu_id}/content'.format(rich_menu_id=rich_menu_id),
        )
        self.assertEqual(
            body,
            res.content
        )

    @responses.activate
    def test_set_rich_menu_image(self):
        rich_menu_id = '1234'
        body = b'hogieoidksk'
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_DATA_ENDPOINT +
            '/v2/bot/richmenu/{rich_menu_id}/content'.format(rich_menu_id=rich_menu_id),
            json={}, status=200
        )

        self.tested.set_rich_menu_image(
            rich_menu_id=rich_menu_id,
            content_type='image/jpeg',
            content=body
        )

        request = responses.calls[0].request
        self.assertEqual('POST', request.method)
        self.assertEqual(
            LineBotApi.DEFAULT_API_DATA_ENDPOINT +
            '/v2/bot/richmenu/{rich_menu_id}/content'.format(rich_menu_id=rich_menu_id),
            request.url
        )

    @responses.activate
    def test_rich_menu_with_switch_action(self):
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
                    RichMenuSwitchAction(
                        rich_menu_alias_id="richmenu-alias-a",
                        data="richmenu-changed-to-a"
                    )
                )
            ]
        )
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu',
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
                            "type": "richmenuswitch",
                            "richMenuAliasId": "richmenu-alias-a",
                            "data": "richmenu-changed-to-a"
                        }
                    }
                ]
            },
            status=200
        )

        result = self.tested.create_rich_menu(rich_menu)
        print(rich_menu)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu'
        )

        self.assertEqual(result, "rich_menu_id")


if __name__ == '__main__':
    unittest.main()
