import requests
import json
API_KEY = 'f64f1ce0638038163570a5644b9c6542970deb91'
url = "https://google.serper.dev/search"
payload = {
  "q": input('Enter Search Query: ')
}
headers = {
  'X-API-KEY': API_KEY,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, json=payload)

# print(response.text)
search_result = json.loads(response.text)
results = search_result['organic']
for result in results:
    print(result['title'])
    print(result['snippet'])
    print('~'*20)