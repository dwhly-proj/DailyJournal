import requests
import os

def send_simple_message():
    print "Journal Mail <journalmail@{}>".format(os.environ['MAILGUN_DOMAIN'])

    return requests.post(
        "https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
        auth=("api", os.environ['MAILGUN_API_KEY']),
        data={"from": "Journal Mail <journalmail@{}>".format(os.environ['MAILGUN_DOMAIN']),
              "to": [os.environ['MAIL_RECIPIENT']],
              "subject": "Daily journal Reminder",
              "text": "Reply to this mail with your entry!"})