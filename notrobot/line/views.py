from django.shortcuts import render
from rest_framework import views, status
from rest_framework.response import Response
import json
import requests as requests_lib
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from .line import CHANNEL_ACCESS_TOKEN, CHANNEL_SECRET, CHANNEL_ID, line_bot_api

"""
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
"""

class LineCallbackAPPIView(views.APIView):
    def post(self, request):
        if request.method == 'POST':
            payload = json.loads(request.body)
            Reply_token = payload['events'][0]['replyToken']
            print(Reply_token)
            message = payload['events'][0]['message']['text']
            print(message)
            if 'สวัสดี' in message :
                Reply_messasge = 'ยินดีต้อนรับเข้าสู่ววววววววววววววววววววววววววววววววววววววววว'
                ReplyMessage(Reply_token,Reply_messasge, CHANNEL_ACCESS_TOKEN)
            else:
                line_bot_api.broadcast(TextSendMessage(text='Hello World!'))
            return Response("callback", status=200)


def ReplyMessage(Reply_token, TextMessage, Line_Acees_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(CHANNEL_ACCESS_TOKEN) ##ที่ยาวๆ
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
    }

    data = {
        "replyToken":Reply_token,
        "messages":[{
            "type":"text",
            "text":TextMessage
        }]
    }

    data = json.dumps(data) ## dump dict >> Json Object
    r = requests_lib.post(LINE_API, headers=headers, data=data) 
    return 200