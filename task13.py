import json

d = {"name": "Ali", "age": 20}

text = json.dumps(d)
print(text, type(text))

d2 = json.loads(text)
print(d2["name"], type(d2))
