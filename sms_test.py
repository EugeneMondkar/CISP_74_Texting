from twilio.rest import Client
import twilio_account

# Your Account SID from twilio.com/console
account_sid = twilio_account.SID
# Your Auth Token from twilio.com/console
auth_token  = twilio_account.TOKEN

client = Client(account_sid, auth_token)

message = client.messages.create(
    to=twilio_account.TEST_PHONE_NUMBER, 
    from_=twilio_account.TEST_SOURCE_NUMBER,
    body="Hello from Python!")

print(message.sid)