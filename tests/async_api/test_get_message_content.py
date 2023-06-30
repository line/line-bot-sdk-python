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

from aiohttp import web

from linebot import (
    AsyncLineBotApi
)
from linebot.aiohttp_async_http_client import AiohttpAsyncHttpClient


async def test_get(aiohttp_client, loop):
    msg = ''.join('Hello, world' for i in range(1000))

    async def hello(request):
        return web.Response(text=msg)

    app = web.Application()
    app.router.add_get('//v2/bot/message/abc/content', hello)

    aiohttp = await aiohttp_client(app, server_kwargs={"skip_url_asserts": True})
    async_client = AiohttpAsyncHttpClient(session=aiohttp)

    bot = AsyncLineBotApi('TOKENTOKEN', async_client, data_endpoint='/')
    content = await bot.get_message_content("abc")
    got = b''
    async for s in content.iter_content():
        got += s
    assert got.decode('utf-8') == msg
