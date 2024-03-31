# a tuple is a collection of ordered, immutable, and heterogeneous elements. Tuples are similar to lists,
# but the main difference is that tuples are immutable, 
# meaning their elements cannot be changed or modified after creation

# tuple with one element if not separated by comma is int type therefore use comma
empty=(1,)
print(type(empty))

# Creating an empty tuple
empty_tuple = ()

# Creating a tuple of integers
numbers = (1, 2, 3, 4, 5)

# Creating a tuple of strings
fruits = ("apple", "banana", "cherry")

# Creating a tuple of mixed data types
mixed_tuple = (1, "apple", True, 3.14)

# Immutable Nature:
print(numbers[0])
# numbers[0]=2  is not allowed TypeError'tuple' object does not support item assignment
# Creating a new tuple with modified elements
modified_numbers = (10,) + numbers[1:]
print(modified_numbers)  # Output: (10, 2, 3, 4, 5)


# Tuple Packing and Unpacking:
# Tuple packing refers to packing multiple values into a single tuple. 
# Tuple unpacking allows you to extract the elements of a tuple into individual variables.
# Tuple packing
person = ("John", 30, "New York")

# Tuple unpacking
name, age, city = person

print(name)  # Output: "John"
print(age)   # Output: 30
print(city)  # Output: "New York"

if "John" in person:
    print("yes it is present")


# Advantages of Tuples:
# Tuples are faster than lists because they are immutable.
# Tuples can be used as keys in dictionaries (lists cannot be used as keys because they are mutable).
# Tuples are often used to represent fixed collections of items, such as coordinates, database records, or function arguments.
# When to Use Tuples:
# Use tuples when you have a fixed collection of items that you don't want to change.
# Use tuples as keys in dictionaries or as elements in sets.
# Use tuples for returning multiple values from a function (tuple packing and unpacking).