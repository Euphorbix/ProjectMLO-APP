import requests
req = requests.get('http://127.0.0.1:5000/')
print(req.status_code)
print(req.headers)
print(req.content)