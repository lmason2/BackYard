import requests
import base64
import json
import uuid

BASE_URL = 'http://127.0.0.1:8000/api/backyard/v1/create-user'

HEADERS = {

}

PAYLOAD = {
    'user_id': str(uuid.uuid4()),
    'name': 'Test name',
    'email': 'test-email@test.com'
}

encoded_payload = base64.b64encode(json.dumps(PAYLOAD).encode())

response = requests.post(BASE_URL, data=encoded_payload, headers=HEADERS)

print(response.text)
