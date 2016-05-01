import requests

def create_annotation(secret, message):
    headers = {'Accept': 'application/json',
               'Content-Type': 'application/json;charset=UTF-8',
               'Authorization': 'Bearer {}'.format(secret)
               }
    payload = {
        "uri": "http://my.journal",
        "user": "acct:joebloggs@example.org",
        "permissions": {
            "read": ["group:__world__"],
            "update": ["acct:joebloggs@example.org"],
            "delete": ["acct:joebloggs@example.org"],
            "admin": ["acct:joebloggs@example.org"],
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
