name = {
    "my_name":"bill",
    "age":40,
    "status":"married",
    "children":["milca","elizabeth","beril"]
}
c = name.get("children")
y = name.keys()
for child in c:
    print((child))
print((y))

for m in name:
    print(name[m])

# .values method is allso applicable
for y in name.values():
    print(y)

# you can also loop through the dict keys and values using items method
for w, x in name.items():
    print(w, x)


