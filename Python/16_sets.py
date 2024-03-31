# a set is an unordered collection of unique elements. 
# Sets are similar to lists or tuples, but unlike lists and tuples, sets do not allow duplicate elements.
# Sets are mutable, meaning you can add or remove elements from them after they are created.

# Creating an empty set
empty_set = set()
print(type(empty_set))

#set1={}  it will create an empty dict not set

# Creating a set of integers
numbers = {1, 2, 3, 4, 5,2,3}

# Creating a set of strings
fruits = {"apple", "banana", "cherry"}

# Creating a set from a list
my_list = [1, 2, 3, 3, 4]
my_set = set(my_list)

# Accessing Elements:
# Since sets are unordered, you cannot access individual elements by index. 
# You can iterate over the elements of a set using a loop or check for membership using the in operator.
fruits = {"apple", "banana", "cherry"}

# Iterating over elements
for fruit in fruits:
    print(fruit)

# Checking for membership
print("banana" in fruits)  # Output: True

# Sets are mutable, so you can add or remove elements from them.

fruits = {"apple", "banana", "cherry"}

# Adding elements
fruits.add("orange")
print(fruits)  # Output: {"apple", "banana", "cherry", "orange"}

# Removing elements
fruits.remove("banana")
print(fruits)  # Output: {"apple", "cherry", "orange"}

# Note:
# Sets automatically remove duplicate elements, so you cannot have duplicate elements in a set.
# Sets are unordered, so the order of elements in a set is not guaranteed.
# Sets cannot contain mutable elements like lists, but they can contain immutable elements like tuples.