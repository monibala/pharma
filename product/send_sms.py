from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC7f2e383f0e9ba57d9d1890eb8738aef7"
# Your Auth Token from twilio.com/console
auth_token  = "ac94fa76bfee0c2b7c587a9cae3ecaf3"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+918056071345", 
    from_="+14344742190",
    body="Hello from Python!")

print(message.sid)