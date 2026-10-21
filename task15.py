import requests

data = requests.get("https://jsonplaceholder.typicode.com/users").json()

for user in data:
    print(user["name"], user["email"], user["address"]["city"])