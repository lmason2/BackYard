'''
/get-events-by-job-id
'''

import requests
import base64
import json
import uuid

BASE_URL = 'http://127.0.0.1:8000/api/backyard/v1/get-events-by-job-id'

HEADERS = {

}

PAYLOAD = {
    'job_id': 'dcd95cf2-0178-4edf-8e4c-e8ea23a8236e',
}

encoded_payload = base64.b64encode(json.dumps(PAYLOAD).encode())

response = requests.post(BASE_URL, data=encoded_payload, headers=HEADERS)

print(response.text)