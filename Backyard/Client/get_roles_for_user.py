import requests
import base64
import json

BASE_URL = 'http://127.0.0.1:8000/api/backyard/v1/get-roles-for-user'

HEADERS = {

}

PAYLOAD = {
    'user_id': 'c65b1f8b-7227-4ac5-8f98-0bfa306ce2c2'
}

encoded_payload = base64.b64encode(json.dumps(PAYLOAD).encode())


response = requests.post(BASE_URL, data=encoded_payload, headers=HEADERS)

print(response.text)