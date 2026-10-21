import requests

data = requests.get("https://jsonplaceholder.typicode.com/users").json()

for user in data:
    print(f"{user['name']:<25} {user['email']}")

name = "Ali"
score = 93.456
print("{} got {:.1f}".format(name, score))