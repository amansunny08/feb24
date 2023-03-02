import json
data={
    "Name": "aman",
    "Age": 35,
    "class": 10
}

# x=json.dumps(data)
# print(x)
# print(type(x))


# ##Convert json into python

# y=json.loads(x)
# print(y)
# print(type(y))

f=open('abc', mode='r')
data=json.load(f)
# print(data)
# print(type(data))

# print(data.values(['Age']))
#     print(i)
print (data.get('Age'))