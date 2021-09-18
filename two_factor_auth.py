from tkinter import *

from twilio.rest import Client
import twilio_account

import random

# Simulates User Authentication Database
password = dict()
password['user1995'] = 'password95'
contact = dict()
contact['mobile'] = twilio_account.TEST_PHONE_NUMBER

# Set up for SMS messaging to implement 2 Factor Authentication
account_sid = twilio_account.SID
auth_token  = twilio_account.TOKEN
client = Client(account_sid, auth_token)


def sendSMS():

    send_SMS_Btn.destroy()

    # Create SMS code
    sms_code = str(random.randrange(1000, 10000))

    message = client.messages.create(
    to=contact['mobile'], 
    from_=twilio_account.TEST_SOURCE_NUMBER,
    body=sms_code)

    print(message.sid)

    label_3 =Label(root,text="Enter SMS Code", width=20,font=("bold",10))
    label_3.place(x=80,y=250)

    sms_entry=Entry(root)
    sms_entry.place(x=240,y=250)

    verify_Btn = Button(root, text='Submit' , width=20,bg="black",fg='white', command= lambda: verify(sms_entry.get(), sms_code))
    verify_Btn.place(x=180,y=380)

def verify(sms_entry, sms_code):

    sms_validation = sms_entry == sms_code # Test to see if correct sms code given

    try:
        if password_entry.get() == password[username_entry.get()] and sms_validation:
            result = "Successful Login!"
        else:
            result = "Wrong username, password,\nor failed 2-factor authentication" # Right Username, Wrong password
    except KeyError:
        result = "Wrong username or password." # Wrong username
    except:
        result = "General Error" # General Error

    label_4 =Label(root,text=result,font=("bold",20))
    label_4.place(x=80,y=275)
    

root = Tk()

root.geometry("500x500")

root.title('Login Page')

label_0 =Label(root,text="LOGIN PAGE", width=20,font=("bold",20))
label_0.place(x=90,y=60)

label_1 =Label(root,text="User Name", width=20,font=("bold",10))
label_1.place(x=80,y=130)

#this will accept the input string text from the user.
username_entry=Entry(root)
username_entry.place(x=240,y=130)

#this creates 'Label' widget for Email and uses place() method.
label_2 =Label(root,text="Password", width=20,font=("bold",10))
label_2.place(x=68,y=180)


password_entry=Entry(root)
password_entry.place(x=240,y=180)


#this creates button for submitting the details provides by the user
send_SMS_Btn = Button(root, text='Submit' , width=20,bg="black",fg='white', command=sendSMS)
send_SMS_Btn.place(x=180,y=380)


#this will run the mainloop.
root.mainloop()
