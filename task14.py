import requests

data = requests.get("https://jsonplaceholder.typicode.com/users").json()
print(len(data), "users")
print(data[0])