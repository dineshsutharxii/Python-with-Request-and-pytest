import requests

url = "https://gorest.co.in/public/v2/users"
token = '66db568fb03cdd1bf01ef3e74d380c282f66ea00e2ff814f63759035b632bb17'

json_header = {
    'Content-Type': 'application/json;',
    'Authorization': 'Bearer ' + token
}

json_data = {
    "name": "Dipak__Singh",
    "email": "dipak__singh@reinger.example",
    "gender": "male",
    "status": "inactive"
}
print("----- Day 2 ----")
response = requests.post(url=url, headers=json_header, json=json_data)
print(response.json())
assert response.status_code == 201
new_id = response.json()['id']
print(new_id)
res_get = requests.get(url+'/'+str(new_id), headers=json_header)
print(res_get.json())
print(res_get)
