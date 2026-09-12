
# Dictionary
# A collection which stores data in the form of key-value pair
# We define dictionary using {key: value}
# key -> immutable, unique(like a set)
# Value -> Mutable or immutable

name = "Vipul Sontakke"
age = 29
emp_id = 101
city = "Pune"

vipul_emp_data = ["Vipul Sontakke", 29, 101, "Pune"]

# Example 1: Declare a Dictionary

vipul_emp_data1 = {
    "name" : "Vipul Sontakke",
    "age" : 29,
    "emp_id" : 101,
    "city" : "Pune"
}

print(vipul_emp_data1)
print(type(vipul_emp_data1))

emp_1 = {}
emp_2 = dict()

print(type(emp_1))
print(type(emp_2))

# Uniqueness of the key
vipul_emp_data1 = {
    "name" : "Vipul Sontakke",
    "age" : 29,
    "emp_id" : 101,
    "city" : "Pune",
    "name": "Harshit",
    "city": "Indore"
}
print(vipul_emp_data1)

# Get the value

print(vipul_emp_data1["emp_id"])
print(vipul_emp_data1["age"])

# Update the value

vipul_emp_data1["age"] = 31
print(vipul_emp_data1)

# Delete the value
print(vipul_emp_data1.pop("emp_id"))
print(vipul_emp_data1)

# vipul_emp_data1.pop("emp_id") KeyError: 'emp_id'

del vipul_emp_data1['city']
print(vipul_emp_data1) 
# del vipul_emp_data1['city'] KeyError: 'city'



# Example 2: Parsing the data

emp_data = {
    "name" : "Vipul Sontakke",
    "age" : 29,
    "emp_id" : 101,
    "city" : "Pune"
}

print(emp_data.keys())
print(emp_data.values())
print(emp_data.items())

for k in emp_data.keys():
    print(k)
    
for v in emp_data.values():
    print(v)
    
for i,j in emp_data.items():
    print(i,"has a value of", j)      


# Nested Dictionary

student_marks = {
    "Science": {"internals": 75, "externals": 12},
    "Maths": {"internals": 80, "externals": 10}
}

print(student_marks['Science']['externals'])
print(student_marks["Maths"]["internals"])
# print(student_marks["Maths"]["intals"]) KeyError: 'intals'

print(student_marks['Science'].get("internals"))
result = student_marks['Science'].get("internals","The key is not present")
if result == "The key is not present":
    print("Key is not present")
else:
    print("perform the tasks")
    
# Possible values for dictionary

student = {
    "string": True,
    1: True,
    1.2: True,
    True: True,
    # [1,2,3]: True, TypeError: unhashable type: 'list'
    (1,2,3): True,
    # {1,5,2}: True, TypeError: unhashable type: 'set'
    # {"key": "value"}: True TypeError: unhashable type: 'dict'
}
