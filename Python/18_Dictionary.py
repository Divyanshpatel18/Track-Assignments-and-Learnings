# a dictionary is a built-in data type that is used to store key-value pairs.
# Dictionaries are ordered, mutable, and iterable collections. 
# Each element in a dictionary consists of a key and its corresponding value. 
# Keys in a dictionary must be unique, and they must be immutable objects, such as strings, numbers, or tuples.
# Values in a dictionary can be of any data type and can be mutable or immutable

# Creating an empty dictionary
empty_dict = {}

# Creating a dictionary with key-value pairs
person = {"name": "John", "age": 30, "city": "New York"}

print(person["name"])
print(person.get("name"))


#get all keys
print(person.keys())

#get all values
print(person.values())

#iterating a dictionary
person = {"name": "John", "age": 30, "city": "New York"}

# Iterating over keys and values
for key, value in person.items():
    print(key, ":", value)

for key in person.keys():
    print(key,"the value is",(person[key]))
