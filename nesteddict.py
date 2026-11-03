person = {
    "name": "Carol",
    "address": {
        "city": "Paris",
        "zip": "75001"
    }
}

student = {"name": "Dave", "grades": {"math": 88, "science": 92, "history": 75}}
print(person["address"]["city"])
print(student["grades"]["history"])

a=14

student = dict.fromkeys(student, a)

print(student)
student1 = {
    "name": "Dave",
    "age": 20,
    "city": "Ahmedabad"
}

student1["location"] = student1.pop("city")

print(student1)

keys_to_delete = ["age","location"]

for key in keys_to_delete:
    student1.pop(key)

print(student1)
