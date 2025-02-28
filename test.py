import requests
import pytest





def test_create_user():
    response = requests.post(url="https://demoqa.com/Account/v1/User",
                             json={"userName":"Blazzer87","password":"!QAZ1qaz"})
    return response


def test_autorization_user():
    response = requests.post(url="https://demoqa.com/Account/v1/GenerateToken",
                             json={"userName": "Blazzer87", "password": "!QAZ1qaz"})
    token = response.json()['token']
    return token

