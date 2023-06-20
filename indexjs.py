from json import dumps

x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = dumps(x)

# the result is a Python dictionary:
print(y)
