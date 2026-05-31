marks = {
    "harry": 100,
    "bikki": 90,
    "rahul": 56,
}

print(marks.items())

print(marks.keys())

print(marks.values())

print(marks.get("harry"))

print(marks.get("rohit", "not found")) # if the key is not found it will return the default value

marks.update({"bikki": 80, "renuka": 70}) # to update the value of a key in a dictionary we can use the update method
print(marks)                              #jo key xaina tyo add gardinxa js like renuka 