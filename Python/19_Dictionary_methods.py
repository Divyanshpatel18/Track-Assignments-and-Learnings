# 1. clear():
# Removes all items from the dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.clear()
print(my_dict)  # Output: {}

# 2. copy():
# Returns a shallow copy of the dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3}
new_dict = my_dict.copy()
print(new_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

# 3. get(key[, default]):
# Returns the value for the specified key. If the key is not found, it returns default (which defaults to None).
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.get('b')
print(value)  # Output: 2

# 4. items():
# Returns a view object that displays a list of dictionary's key-value pairs as tuples.
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict.items())  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

# 5. keys():
# Returns a view object that displays a list of all the keys in the dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict.keys())  # Output: dict_keys(['a', 'b', 'c'])

# 6. values():
# Returns a view object that displays a list of all the values in the dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict.values())  # Output: dict_values([1, 2, 3])

# 7. pop(key[, default]):
# Removes and returns the value for the specified key. If the key is not found, it returns default (which defaults to raising a KeyError).
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.pop('b')
print(value)  # Output: 2
print(my_dict)  # Output: {'a': 1, 'c': 3}

# 8. popitem():
# Removes and returns an arbitrary key-value pair from the dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3}
item = my_dict.popitem()
print(item)  # Output: ('c', 3)
print(my_dict)  # Output: {'a': 1, 'b': 2}

# del my_dict
print(my_dict)

#update