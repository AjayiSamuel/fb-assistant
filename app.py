import os, sys
from flask import Flask, request
from utils.util import wit_response
from pymessenger import Bot

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAmX5UFYV78BAJRKl8BYtxuvSnxLhftJlPVDvuR1itvUpNRD7CbZCOYxWGLqTvZBwFD6ttuiiKd86cbnShZBbjzTje82WgyalOK8ZBIdGXuklTlwCyu663tWBdbH3ZCWjkz0Q8qjCVeKt68mUkfqe6t7ZAjZBv7SjV8ZCVmNOX1KfSFvYCL7d6eNJ85czT3XkjsZD"

bot = Bot(PAGE_ACCESS_TOKEN)

@app.route('/', methods=['GET'])
def verify():
    # Webhook Verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Welcome to OctoBanking", 200


@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    log(data)

    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
                # IDs
                sender_id = messaging_event['sender']['id']
                recipient_id = messaging_event['recipient']['id']

                if messaging_event.get('message'):
                    if 'text' in messaging_event['message']:
                        messaging_text = messaging_event['message']['text']
                    else:
                        messaging_text = 'no text'
                    #  Echo
                    response = messaging_text
                    response = None
                    entity, value = wit_response(messaging_text)

                    if entity == 'airtime':
                        response = "Ok. How much airtime do you need"
                    elif entity == 'data':
                        response = "ok. what type of data would you like to buy"
                    bot.send_text_message(sender_id, response)

    return "ok", 200


def log(message):
    print(message)
    sys.stdout.flush()


if __name__ == "__main__":
    app.run(debug=True, port=80)