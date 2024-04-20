import pytest
import requests
import json

@pytest.fixture(scope="session")
def auth_token():
    with open("endpoints.json", "r") as f:
        endpoints = json.load(f)
        base_url = endpoints["base_url"]
        token_url = endpoints["token_url"]

    headers_test = {'Content-Type': 'application/json'}
    payload = {
        "username": 'kminchelle',
        "password": '0lelplR',
        "expiresInMins": 30
    }

    response = requests.post(url=base_url + token_url, headers=headers_test, json=payload)

    if response.status_code == 200:
        data = response.json()
        token = data.get('token')
        print("Token value:", token)
        return token
    else:
        raise ValueError("Failed to obtain token. Error code:", response.status_code)

@pytest.fixture(scope="session")
def api_endpoints():
    with open("endpoints.json", "r") as f:
        endpoints = json.load(f)
    return endpoints



