'''
/create-document
'''

import requests
import base64
import json
import uuid

BASE_URL = 'http://127.0.0.1:8000/api/backyard/v1/create-document'

HEADERS = {

}

document_base64 = open("pdf_base64.txt", "r+")

PAYLOAD = {
    'document_id': str(uuid.uuid4()),
    'job_id': 'dcd95cf2-0178-4edf-8e4c-e8ea23a8236e',
    'base64': document_base64.read(),
    'type': 'permit',
    'metadata': json.dumps({
        'name': 'City permit'
    })
}

encoded_payload = base64.b64encode(json.dumps(PAYLOAD).encode())

response = requests.post(BASE_URL, data=encoded_payload, headers=HEADERS)

print(response.text)