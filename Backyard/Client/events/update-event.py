'''
/update-event
'''

import requests
import base64
import json
import uuid
from datetime import datetime

BASE_URL = 'http://127.0.0.1:8000/api/backyard/v1/update-event'

HEADERS = {

}

PAYLOAD = {
    'event_id': '1e8f8212-3c81-437e-b65a-f5471406e705',
    'values': json.dumps({
        'date': datetime.now().strftime('%Y-%m-%d'),
        'metadata': json.dumps({'name': 'Frontyard Meeting'}),
    })
}

encoded_payload = base64.b64encode(json.dumps(PAYLOAD).encode())

response = requests.post(BASE_URL, data=encoded_payload, headers=HEADERS)

print(response.text)