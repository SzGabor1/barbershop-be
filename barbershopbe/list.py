import requests
from getpass import getpass
endpoint_auth = "http://localhost:8000/api/auth/"
username = input("Username: ")
password = getpass("Password:")
auth_response = requests.post(endpoint_auth, json={"username": username, "password": password})
print(auth_response.json())


if auth_response.status_code == 200:
    token = auth_response.json().get('token')
    headers = {
        "Authorization": f"Bearer {token}"
    }
    endpoint = "http://localhost:8000/api/news/"

    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())

