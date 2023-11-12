'''
/create-event
'''

import requests
import base64
import json
import uuid
from datetime import datetime

BASE_URL = 'http://127.0.0.1:8000/api/backyard/v1/create-event'

HEADERS = {

}

PAYLOAD = {
    'event_id': str(uuid.uuid4()),
    'job_id': 'dcd95cf2-0178-4edf-8e4c-e8ea23a8236e',
    'date': datetime.now().strftime("%Y-%m-%d"),
    'metadata': json.dumps({
        'name': 'Backyard meeting',
        'notes': 'Want to move plantar',
    })
}

encoded_payload = base64.b64encode(json.dumps(PAYLOAD).encode())

response = requests.post(BASE_URL, data=encoded_payload, headers=HEADERS)

print(response.text)