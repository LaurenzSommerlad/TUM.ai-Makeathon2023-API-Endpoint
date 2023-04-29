import requests
import json
url = 'http://127.0.0.1:1234/ask'
d = dict()

body = {'context': ['A']*15}

x = requests.post(url, json = body)
data = json.loads(x.text)
print(data)
print(data["context"])