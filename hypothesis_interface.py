import requests
import os

def create_annotation(secret, message):
    headers = {'Accept': 'application/json',
               'Content-Type': 'application/json;charset=UTF-8',
               'Authorization': 'Bearer {}'.format(secret)
               }
    payload = {
        "uri": "http://my.journal",
        "user": "acct:{}".format(os.environ['MAIL_RECIPIENT']),
        "permissions": {
            "read": ["acct:{}".format(os.environ['HYPOTHESIS_USER'])],
            "update": ["acct:{}".format(os.environ['HYPOTHESIS_USER'])],
            "delete": ["acct:{}".format(os.environ['HYPOTHESIS_USER'])],
            "admin": ["acct:{}".format(os.environ['HYPOTHESIS_USER'])],
        },
        "document": {},
        "target": [],
        "tags": ['JournalEntry'],
        "text": message
    }

    url = 'https://hypothes.is/api/annotations'

    result = requests.post(url, json=payload, headers = headers)
    print result

    return result
