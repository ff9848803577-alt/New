# they also store data in a key value pair format 
# they are mutable and can be changed
# they are unordered and do not have a specific order
# they are defined using curly braces {}
# example of a dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict)
# to access the value of a key in a dictionary we use the key name
print(my_dict["name"])
# to add a new key value pair to a dictionary we can use the update method
my_dict.update({"country": "USA"})
print(my_dict)
# to remove a key value pair from a dictionary we can use the pop method
my_dict.pop("age")
print(my_dict)

print(type(my_dict))# here its class is dict

marks = {
    "Bikki": 90,
    "rohit": 80,
    }
print(marks)
print(marks["Bikki"])

