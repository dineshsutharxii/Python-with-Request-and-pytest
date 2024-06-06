import requests
import json

url = "https://gorest.co.in/public/v2/users"

para = {
    'page': 3,
    'per_page': 5
}
# OR
json_file = open(r'C:\Users\dines\Learn And Interview\Api with Request python\datafiles\data.json')
json_data = json.load(json_file)

response = requests.get(url=url, params=para)
json_response = response.json()
print(json_response)
assert response.status_code == 200
