import pytest
import requests
import yaml

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    login, password,address = data['login'], data['password'], data['url']

S = requests.Session()

@pytest.fixture()
def user_login():
    rest1 = S.post(url=address, data={'username' : login, 'password' : password})
    return rest1.json()['token']