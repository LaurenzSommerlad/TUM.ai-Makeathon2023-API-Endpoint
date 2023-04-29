import requests

url = 'http://127.0.0.1:1234/ask'
d = dict()

body = {'context': str([])}

x = requests.post(url, json = body)

print(x.text)