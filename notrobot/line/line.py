from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

CHANNEL_ID="1655576826"
CHANNEL_SECRET= "7e85733f672d0fbcfef740adb250900f"
CHANNEL_ACCESS_TOKEN = "aa11mzRsoeYdyfw10jj5ZoXPCIy11brq7LJNie+/mCOfbbbN6sTnsBHVCCtIUOmayj2U6g7qE+pxhENoiTN2gml0pMHgFPQzBfP4fkFl9xWG1+TT/30ou49nXc32fQMt+u2V1+fxWhaEQ5N9lVpa7AdB04t89/1O/w1cDnyilFU="
BOT_ID = "@204lnkzq"


line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)