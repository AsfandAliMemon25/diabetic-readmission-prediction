import requests

url = "http://127.0.0.1:8000/predict"
data = {
    "age": 70,
    "gender": "Male",
    "num_medications": 5,
    "time_in_hospital": 3
    # Add all other required features
}

response = requests.post(url, json=data)
print(response.json())

