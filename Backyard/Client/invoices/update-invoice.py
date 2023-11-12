'''
/update-invoice
'''

import requests
import base64
import json
from datetime import datetime, timedelta

BASE_URL = 'http://127.0.0.1:8000/api/backyard/v1/update-invoice'

HEADERS = {

}

now = datetime.now()
time_change = timedelta(days=15) 
update = now + time_change

PAYLOAD = {
    'invoice_id': 'e72ac7a2-d511-419b-b0b1-98a1a24cb359',
    'values': json.dumps({
        'due_date': update.strftime('%Y-%m-%d'),
    })
}

encoded_payload = base64.b64encode(json.dumps(PAYLOAD).encode())

response = requests.post(BASE_URL, data=encoded_payload, headers=HEADERS)

print(response.text)