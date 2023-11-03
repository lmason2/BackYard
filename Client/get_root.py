import requests
import base64
import json

BASE_URL = 'http://127.0.0.1:8000/'

HEADERS = {

}

PAYLOAD = {
    'by_job_id': '73205484-f6b5-4c5c-b556-165f1e28d0eb'
    # 'by_client_and_contractor_id': 'testing2'
}

encoded_payload = base64.b64encode(json.dumps(PAYLOAD).encode())


response = requests.get(BASE_URL)

print(response.text)