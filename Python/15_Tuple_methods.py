# 1.count(value): Returns the number of occurrences of a specified value in the tuple.

numbers = (1, 2, 2, 3, 4, 2)
count_2 = numbers.count(2)
print(count_2)  # Output: 3

# 2. index(value): Returns the index of the first occurrence of a specified value in the tuple.
#  index(element,start,end)
numbers = (1, 2, 3, 4, 2)
index_2 = numbers.index(2)
print(index_2)  # Output: 1 if not found raises a valueErro

# len()
print(len(numbers))
# 3.Example of "modifying" a tuple by creating a new tuple
numbers = (1, 2, 3)
modified_numbers = numbers + (4,)
print(modified_numbers)  # Output: (1, 2, 3, 4)

#4. concatenation since it doesnot modify just create new tuple
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)


#converting list to tuple and tuple to list
# Original tuple
original_tuple = (1, 2, 3, 4, 5)

# Convert tuple to list
list_from_tuple = list(original_tuple)

# Modify the list
list_from_tuple[2] = 10
list_from_tuple.append(6)

# Convert list back to tuple
modified_tuple = tuple(list_from_tuple)

print(modified_tuple)  # Output: (1, 2, 10, 4, 5, 6)
