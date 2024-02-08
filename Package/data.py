payload_user = {
  "id": 0,
  "username": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 0
}

payload_pet = {
    "id": 3,
    "category": {
      "name": "Cat"
    },
    "name": "Cat",
    "tags": [
      {
        "name": "Cat"
      }
    ],
    "status": "available"
  }


payload_store = {
  "id": 2,
  "petId": 3,
  "quantity": 0,
  "shipDate": "2024-01-25T12:07:38.703Z",
  "status": "placed",
  # "complete": true
}

update_payload_pet = {
  "id": 4,
  "category": {
    "name": "Cat"
  },
  "name": "Dog",
  "tags": [
    {
      "name": "Cat"
    }
  ],
  "status": "Unavailable"
}

update_payload_user = {
  "id": 1,
  "username": "aku",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 0
}