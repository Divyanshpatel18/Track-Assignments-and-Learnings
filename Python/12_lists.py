# In Python, a list is a built-in data type used to store a collection of items. 
# Lists are mutable, meaning you can modify their elements after they have been created. 
# Lists are ordered and allow duplicate elements.
# You can create lists containing elements of any data type, including other lists

# Creating an empty list
empty_list = []

# Creating a list of integers
numbers=[1, 2, 3 ,4,5]

# Creating a list of strings
fruits = ["apple", "banana", "cherry"]

# Creating a list of mixed data types
mixed_list = [1, "apple", True, 3.14]

print(empty_list)
print(numbers)
print(fruits)
print(mixed_list)


# Accessing Elements:
# You can access individual elements of a list using index notation.
# Indexing starts from 0 for the first element and -1 for the last element.
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # Output: "apple"
print(fruits[-1])  # Output: "cherry"

# Slicing:
# You can extract a portion of a list using slicing notation [start:stop:step].
numbers=[1,2,3,4,5]
print(numbers[1:])
print(numbers[1:3])
print(numbers[::2])#(numbers[0:len(numbers):2])

# Modifying Lists:
# Lists are mutable, so you can modify their elements or their size.

numbers = [1, 2, 3, 4, 5]

# Modifying an element
numbers[2] = 10
print(numbers)   # Output: [1, 2, 10, 4, 5]

# Appending elements
numbers.append(6)
print(numbers)   # Output: [1, 2, 10, 4, 5, 6]

# Removing elements
numbers.remove(2)
print(numbers)   # Output: [1, 10, 4, 5, 6]

# Deleting elements by index
del numbers[0]
print(numbers)   # Output: [10, 4, 5, 6]

# List Operations:
# Lists support various operations like concatenation, repetition, and membership testing.
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
combined_list = list1 + list2
print(combined_list)  # Output: [1, 2, 3, 4, 5, 6]

# Repetition
repeated_list = list1 * 3
print(repeated_list)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Membership testing
print(2 in list1)  # Output: True
print(7 in list2)  # Output: False