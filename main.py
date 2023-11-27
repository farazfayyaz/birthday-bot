# Download the helper library from https://www.twilio.com/docs/python/install
import os
import birthday_checker
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body=birthday_checker.find_birthday_today(),
                     from_='+18335440526',
                     to='+15166526774'
                 )

print(message.sid)
