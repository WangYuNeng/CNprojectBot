from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('v4nBwDMkqdXr7wjbKON42g0G8pvWoGcaDdHxF+RTPqWeA+jI7z+tAc/xMkAnMd4r5yIomV0+Okqdp6+LW/HdYNGqgFDpWZTBJyJukqTKl3KWMZpK6oIyjKr6jcqWrOjsrPBQ/NMZPsdccLcDUApOAwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f5fbe708f00e032157ebe66e255845a8')


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
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="123456"))


if __name__ == "__main__":
    app.run()
