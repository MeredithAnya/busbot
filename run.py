# /usr/bin/env python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from parser import parse_text_body
from parser import format_times_message, format_stops_message
from nextbus_client import NextBusClient

app = Flask(__name__)
# app.config.from_object('default_settings')

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()
    kwargs = parse_text_body(request.values['Body'])
    nb_client = NextBusClient(**kwargs)

    message = nb_client.get_message()
    resp.message(message)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
