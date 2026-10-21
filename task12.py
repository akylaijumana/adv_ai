import requests

r = requests.get("https://httpbin.org/get")

print("HEADER:")
print(r.headers)
print("BODY:")
print(r.text)