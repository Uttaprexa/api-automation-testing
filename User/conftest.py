import requests
import json
from Package.data import payload_user
from Package.data import update_payload_user
from Package.urls import base_url
from Package.urls import endpoint_user
def post_request():
    try:
        response = requests.post(f'{base_url}{endpoint_user}', json=payload_user)
        print("\n POST request successful.\n Response:", json.dumps(response.json(), indent=4))
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print(f"\n POST request failed. Error: {error}")
post_request()

def get_request():
    try:
        response = requests.get(f'{base_url}{endpoint_user}string', json=payload_user)
        print("\n GET request successful.\n Response:", json.dumps(response.json(), indent=4))
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print(f"\n GET request failed. Error: {error}")
get_request()

def put_request():
    try:
        response = requests.put(f'{base_url}{endpoint_user}aku', json=update_payload_user)
        print("\n PUT request successful.\n Response:", json.dumps(response.json(), indent=4))
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print(f"\n PUT request failed. Error: {error}")
put_request()

for key in payload_user:
    if payload_user[key] != update_payload_user[key]:
        print(f"\t\t\t\t\t\t\t\t\t\t\t\t{key} is not equal to {update_payload_user[key]}")

def delete_request():
    try:
        response = requests.delete(f'{base_url}{endpoint_user}aku', json=update_payload_user)
        print("\n DELETE request successful.\n Response:", json.dumps(response.json(), indent=4))
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print(f"\n DELETE request failed. Error: {error}")
delete_request()
