# FastAPI line messaging API

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, FileResponse
from linebot import LineBotApi, WebhookHandler, AsyncLineBotApi
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, StickerMessage, ImageMessage, TextSendMessage, StickerSendMessage, ImageSendMessage

import uvicorn
import logging

import aiohttp
from linebot.aiohttp_async_http_client import AiohttpAsyncHttpClient
app = FastAPI()

import cv2
import tempfile 

import json
import torch
import os
    
# session = aiohttp.ClientSession()
# async_http_client = AiohttpAsyncHttpClient(session)

channel_access_token = "Channel_Access_Token"
channel_secret = "Channel_Secret"

line_bot_api = LineBotApi(channel_access_token)
# line_bot_api_async =  AsyncLineBotApi(channel_access_token, async_http_client)

handler = WebhookHandler(channel_secret)

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')


def root_url(req):
    global url_root
    url_root = req
    return url_root


@app.get("/result/{filename}")
async def main(filename):
    img = './static/' + filename
    return FileResponse(img)


@app.get("/url")
def read_root(request: Request):
    client_host = request.client.host
    root_path = request.base_url._url
    return {"client_host": client_host, "root_path": root_path}

# /callback => Post Request
@app.post("/callback")
async def callback(request: Request):
    root_path = request.base_url._url
    print(root_path)
    root_url(root_path)
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = await request.body()
    # bytes => str
    body = body.decode('utf-8')
    # FastAPI log info
    logging.info('Request body: ' + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        # fastapi response with status code 400
        return JSONResponse(status_code=400)

    return 'OK'

# Send message to user
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)
    try:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text))
    except Exception as e:
        print(e)

# Send sticker message to user
@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    try:
        line_bot_api.reply_message(
            event.reply_token,
            StickerSendMessage(
                package_id=event.message.package_id,
                sticker_id=event.message.sticker_id)
        )
    except Exception as e:
        print(e)

# Send sticker message to user
@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):

    if isinstance(event.message, ImageMessage):
        ext = 'jpg'
    else:
        return

    message_content = line_bot_api.get_message_content(event.message.id)
    with tempfile.NamedTemporaryFile(dir=static_tmp_path, prefix=ext + '-', delete=False) as tf:
        for chunk in message_content.iter_content():
            tf.write(chunk)
        tempfile_path = tf.name

    dist_path = tempfile_path + '.' + ext
    dist_name = os.path.basename(dist_path)
    os.rename(tempfile_path, dist_path)

    try:
        input_image = cv2.imread(dist_path)
        results = model(input_image)
        results_json = json.loads(results.pandas().xyxy[0].to_json(orient="records"))

        for result in results_json:
            x1, y1, x2, y2 = round(result['xmin']), round(result['ymin']), round(result['xmax']), round(result['ymax'])
            cv2.rectangle(input_image, (x1 - 20, y1 - 20), (x2 + 20, y2 + 20), (0, 255, 0), 2)
            cv2.putText(input_image, result['name'], (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imwrite('./static/' + dist_name , input_image)

        url = str(url_root) + 'result/' + dist_name

        line_bot_api.reply_message(
            event.reply_token, [
            ImageSendMessage(url, url),
            TextSendMessage(text=str(results_json))
            ])

    except Exception as e:
        print(e)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
