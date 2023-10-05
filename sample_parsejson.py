import json

x = '{"name": "John","age" : "30", "city": "New York City"}'

y = json.loads(x)

print("The ouput of json file is ", y)
print("Name:", y["name"])
print("City:", y["city"])
print("Age:", y["age"])