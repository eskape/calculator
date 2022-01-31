
import json
import requests
import sys

api_url = "http://localhost:5002/add"

def test_add_calculator():
    json_data = {"val1" : 1, "val2" : 2}
    response = requests.post(api_url, json=json_data)
    json_mssg = response.json()
    
    assert response.status_code == 200
    assert json_mssg["Result"] == 3
