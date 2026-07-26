import os
import re
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage

app = Flask(__name__)

# ดึง Token และ Secret จาก Environment Variable ของ Render อัตโนมัติ
line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET'))

# ตัวแปรควบคุมโหมดสแตนด์บาย (เริ่มต้นปิดไว้)
IS_STANDBY = False 

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global IS_STANDBY
    
    # ถ้ายังไม่เปิดสแตนด์บาย จะไม่สนใจข้อความใดๆ ทั้งสิ้น
    if not IS_STANDBY:
        return

    user_message = event.message.text.strip()
    user_id = event.source.user_id
    
    # กรองเฉพาะข้อความที่เป็นรหัสงาน (ขึ้นต้นด้วย WC, WG, WK ตามด้วยตัวเลข)
    if re.match(r'^(WC|WG|WK)\d+', user_message, re.IGNORECASE):
        print(f"เจอและเก็บรหัสงาน: {user_message} จากผู้ใช้: {user_id}")
    else:
        return

if __name__ == "__main__":
    app.run()
