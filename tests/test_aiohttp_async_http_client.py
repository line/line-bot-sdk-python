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

from linebot.aiohttp_async_http_client import AiohttpAsyncHttpClient


async def test_get(aiohttp_client, loop):
    async def hello(request):
        return web.Response(text='Hello, world')

    app = web.Application()
    app.router.add_get('/test', hello)

    client = AiohttpAsyncHttpClient(session=await aiohttp_client(app))
    resp = await client.get('/test')
    assert resp.status_code == 200
    text = await resp.text
    assert 'Hello, world' in text


async def test_get_json(aiohttp_client, loop):
    async def hello(request):
        return web.json_response({'test': 'Hello, world'})

    app = web.Application()
    app.router.add_get('/test', hello)
    client = AiohttpAsyncHttpClient(session=await aiohttp_client(app))
    resp = await client.get('/test')
    assert resp.status_code == 200
    json = await resp.json
    assert 'Hello, world' == json['test']


async def test_get_iter(aiohttp_client, loop):
    async def hello(request):
        return web.Response(text='Hello, world')

    app = web.Application()
    app.router.add_get('/test', hello)

    client = AiohttpAsyncHttpClient(session=await aiohttp_client(app))
    resp = await client.get('/test')
    assert resp.status_code == 200

    buffer = ''
    async for data in resp.iter_content(1024):
        buffer += data.decode('utf-8')
    assert 'Hello, world' in buffer


async def test_post(aiohttp_client, loop):
    async def hello(request):
        return web.Response(text='Hello, world')

    app = web.Application()
    app.router.add_post('/test', hello)

    client = AiohttpAsyncHttpClient(session=await aiohttp_client(app))
    resp = await client.post('/test')
    assert resp.status_code == 200
    text = await resp.text
    assert 'Hello, world' in text


async def test_delete(aiohttp_client, loop):
    async def hello(request):
        return web.Response(text='Hello, world')

    app = web.Application()
    app.router.add_delete('/test', hello)

    client = AiohttpAsyncHttpClient(session=await aiohttp_client(app))
    resp = await client.delete('/test')
    assert resp.status_code == 200
    text = await resp.text
    assert 'Hello, world' in text


async def test_put(aiohttp_client, loop):
    async def hello(request):
        return web.Response(text='Hello, world')

    app = web.Application()
    app.router.add_put('/test', hello)

    client = AiohttpAsyncHttpClient(session=await aiohttp_client(app))
    resp = await client.put('/test')
    assert resp.status_code == 200
    text = await resp.text
    assert 'Hello, world' in text
