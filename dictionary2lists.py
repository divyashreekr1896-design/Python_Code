##dictinary for 2 lists
keys = ["name", "age", "city"]
values = ["Pruthvi", 29, "Bangalore"]

result = dict(zip(keys, values))
print(result)
result.clear() ###to clear result
print(result)

###to merge 2 dictionaries
dict1 = {
    "name": "Pru",
    "age": 29
}
dict2 = {
    "city": "Bangalore",
    "State": "karnataka"
}
merged_dict = {**dict1, **dict2}
print(merged_dict)

