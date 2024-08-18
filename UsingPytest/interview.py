import requests
import json

def test_get_and_post():
    url = "https://vydkq.wiremockapi.cloud/json/1"
    post_url = "https://vydkq.wiremockapi.cloud/json"
    88
    get_res = requests.get(url=url)
    print(f"Status code for get request is {get_res.status_code}")
    assert get_res.status_code == 200
    response_json = get_res.json()
    for i in range(len(response_json['data'])):
        id = response_json['data'][i]['id']
        data_body = {
            "id": id
        }
        post_req = requests.post(url=post_url, json=data_body)
        print(f"Status code for post request for {id} is {post_req.status_code}")
        #response code
        assert post_req.status_code == 201

test_get_and_post()