import requests
import json
from Package.data import payload_pet
from Package.data import update_payload_pet
from Package.urls import base_url
from Package.urls import endpoint
def post_request():
    try:
        response = requests.post(f'{base_url}{endpoint}', json=payload_pet)
        print("\n POST request successful.\n Response:", json.dumps(response.json(), indent=4))
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print(f"\n POST request failed. Error: {error}")
post_request()
def get_request():
    try:
        response = requests.get(f'{base_url}{endpoint}3', json=payload_pet)
        print("\nGET request successful.\n Response:", json.dumps(response.json(), indent=4))
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print(f"\nGET request failed. Error: {error}")
get_request()
def put_request():
    try:
        response = requests.put(f'{base_url}{endpoint}', json=update_payload_pet)
        print("\nPUT request successful.\n Response:", json.dumps(response.json(), indent=4))
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print(f"\nPUT request failed. Error: {error}")
put_request()

for key in payload_pet:
    if payload_pet[key] != update_payload_pet[key]:
        print(f"\t\t\t\t\t\t\t{key} is not equal to {update_payload_pet[key]}")
def delete_request():
    try:
        response = requests.delete(f'{base_url}{endpoint}4', json=update_payload_pet)
        print("\nDELETE request successful.\n Response:", json.dumps(response.json(), indent=4))
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print(f"\nDELETE request failed. Error: {error}")
delete_request()
