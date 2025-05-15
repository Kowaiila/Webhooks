import requests
import json

webhook_url = 'https://webhook.site/99918c8c-bb81-4862-946a-6a5e6010640c'

data = {
    'name' : 'Vicky y Nata',
    'youtube_url': 'https://youtu.be/Ekv5fmB6EDs?si=wuregV4iOp8RMJPU'
}

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})