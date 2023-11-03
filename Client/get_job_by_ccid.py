import requests
import base64
import json

BASE_URL = 'http://127.0.0.1:8000/api/backyard/v1/get-job'

HEADERS = {

}

PAYLOAD = {
    # 'by_job_id': '73205484-f6b5-4c5c-b556-165f1e28d0eb',
    'by_client_and_contractor_id': {
        'client_id': '99daca12-11ed-4b3b-a63f-fe0ec90048e3',
        'contractor_id': 'f064eff9-d90b-4a90-95c1-fedf8978b2af'
    }
}

encoded_payload = base64.b64encode(json.dumps(PAYLOAD).encode())


response = requests.post(BASE_URL, data=encoded_payload, headers=HEADERS)

print(response.text)