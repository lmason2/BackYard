import requests
import base64
import json
import uuid

BASE_URL = 'http://127.0.0.1:8000/api/backyard/v1/get-job-by-user-id'

HEADERS = {

}

PAYLOAD = {
    'user_id': '46fed996-60ba-45e3-b135-1f29a57b2706',
    'client_id': True,
}

encoded_payload = base64.b64encode(json.dumps(PAYLOAD).encode())

response = requests.post(BASE_URL, data=encoded_payload, headers=HEADERS)

print(response.text)
