# test_api.py

import pytest
import requests
import json


# using "reqres.in" website to test against an api endpoint
@pytest.fixture
def main_url():
    return "https://reqres.in"

def test_valid_login(main_url): 
    url = main_url + "/" + "api/login/" # appending api path
    # data = {"email":"abc@xyz.com",
    #         "password":"qwerty"} # this one doesn't work
    data = {"email":"eve.holt@reqres.in",
            "password":"cityslicka"}
    response = requests.post(url, data=data) # not getting, posting it
    json_data = json.loads(response.text)
    assert response.status_code == 200 # keeps running through to end of function
    assert json_data['token'] == "QpwL5tke4Pnpja7X4" # hashed password?