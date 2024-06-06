import requests

url = "https://fakerestapi.azurewebsites.net/api/v1/Activities"

# Get
res = requests.get(url)
assert res.status_code == 200
print(res.status_code)
print(res.json())

res = requests.get(url + '/3')
assert res.status_code == 200
print(res.status_code)
print(res.json())

# post
request_header = {
    'Content-Type' : 'application/json; charset=utf-8; v=1.0'
}
load = {
    "id": 265,
    "title": "string",
    "dueDate": "2024-06-06T08:21:47.033",
    "completed": True
}
res = requests.post(url, headers=request_header, json=load)
print(res.status_code)
json_ = res.json()
print(json_)
id = json_['id']
assert id == 265
print(id)

#put
request_header = {
    'Content-Type' : 'application/json; charset=utf-8; v=1.0'
}
response = requests.get(url + '/15')
print("--- Before updating ---" )
print(response.json())

load = {
        'id': 20,
        'title': 'Activity 20',
        'dueDate': '2024-06-07T00:20:24.444004+00:00',
        'completed': False
}

response = requests.put(url + '/15', json=load)
json_ = response.json()
print("--- After Updating ---")
print(json_)
status_code = response.status_code
assert status_code == 200
assert json_['title'] == "Activity 20"
assert json_['id'] == 20

#Delete
response = requests.delete(url + '/15')
print(response.status_code)


