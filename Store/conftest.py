import requests
import json
from Package.data import payload_store
from Package.urls import base_url
from Package.urls import endpoint_store
def post_request():
    try:
        response = requests.post(f'{base_url}{endpoint_store}order', json=payload_store)
        print("\nPOST request successful.\n Response:", json.dumps(response.json(), indent=4))
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print(f"\nPOST request failed. Error: {error}")
post_request()

def get_request():
    try:
        response = requests.get(f'{base_url}{endpoint_store}order/2', json=payload_store)
        print("\nGET request successful.\n Response:", json.dumps(response.json(), indent=4))
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print(f"\nGET request failed. Error: {error}")
get_request()

def delete_request():
    try:
        response = requests.delete(f'{base_url}{endpoint_store}order/2', json=payload_store)
        print("\nDELETE request successful.\n Response:", json.dumps(response.json(), indent=4))
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print(f"\nDELETE request failed. Error: {error}")
delete_request()

def make_get_request():
    try:
        response = requests.get(f'{base_url}{endpoint_store}inventory')
        print("\nGET request successful.\n Response:", json.dumps(response.json(), indent=4))
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print(f"\nGET request failed. Error: {error}")
make_get_request()