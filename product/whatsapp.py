import os
from twilio.rest import Client


TWILIO_ACCOUNT_SID = 'AC7f2e383f0e9ba57d9d1890eb8738aef7'
TWILIO_AUTH_TOKEN = 'ac94fa76bfee0c2b7c587a9cae3ecaf3'

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = os.environ[TWILIO_ACCOUNT_SID]
# auth_token = os.environ[TWILIO_AUTH_TOKEN]
# client = Client(account_sid, auth_token)
client = Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)
message = client.messages \
    .create(
         from_='whatsapp:+14155238886',
         body='Hi, Joe! Thanks for placing an order with us. We’ll let you know once your order has been processed and delivered. Your order number is O12235234',
         to='whatsapp:+919940977404'
     )

print(message.sid)