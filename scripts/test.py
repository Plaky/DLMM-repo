import requests

url = 'https://dlmm-api.meteora.ag/info/protocol_metrics'
headers = {'accept': 'application/json'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Request failed with status code {response.status_code}")