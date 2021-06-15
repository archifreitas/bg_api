import requests
import json

print("Testing POST endpoint 😀 ")
data = {'sample': {'ppp': 99 } }

#{"detail":[{"loc":["query","sample"],"msg":"field required","type":"value_error.missing"}]}'
response = requests.post('http://127.0.0.1:8000/predict', json=data)

print(f"{response.status_code} -- {response.content}")

