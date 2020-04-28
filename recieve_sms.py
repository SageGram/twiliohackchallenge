import os
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)

print("boo hoo")
@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()
    print("2")

    resp.message("The Robots are coming! Head for the hills")
    print("3")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
    print("4")
