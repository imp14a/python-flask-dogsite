from flask import Flask, request
import uuid

app = Flask(__name__)


owners = [
    {
        "id" : str(uuid.uuid4())[:7],
        "name": "Miguel Mont",
        "personal_data": [
            {
                "email": "miguel.mont@google.com",
                "phone": 2113462345,
                "address": "Skywalker Road 4st "
            }
        ]
    }
]

@app.get("/owners")
def get_owners():
    return {"owners": owners}

@app.post("/owners")
def add_owner():
    request_data = request.get_json()
    new_owner = {"name": request_data["name"], "personal_data": []}
    owners.append(new_owner)
    return new_owner, 201

@app.post("/owners/<string:name>/data")
def create_data(name):
    request_data = request.get_json()
    for owner in owners:
        if owner["name"] == name:
            new_personal_data = {"email": request_data["email"], 
            "phone": request_data["phone"], "address": request_data["address"]}
            owner["personal_data"].append(new_personal_data)
            return new_personal_data, 201
    return {"message": "Owner not found"}, 404


@app.get("/owners/<string:name>")
def get_owner(name):
    for owner in owners:
        if owner["name"] == name:
            return owner
    return {"message": "Owner not found"}, 404

@app.get("/owners/<string:name>/data")
def get_data_of_owner(name):
    for owner in owners:
        if owner["name"] == name:
            return {"personal_data": owner["personal_data"]}
    return {"message": "Owner not found"}, 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='4040')