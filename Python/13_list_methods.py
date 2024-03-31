#1. append(x): Adds an element x to the end of the list.
numbers = [3,1,34,12,47,2]
numbers.append(4)
print(numbers)  # Output: [1, 2, 3, 4]
#2. sort()
numbers.sort()
# numbers.sort(reverse=True) for descending order
print(numbers)

#3.  extend(iterable): Extends the list by appending elements from the iterable.
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
print(numbers)  # Output: [1, 2, 3, 4, 5, 6]

#4.reverse
# numbers.reverse()
# print(numbers)

#5.index(x): Returns the index of the first occurrence of element x in the list.
print(numbers.index(3))

# 6.count(x): Returns the number of occurrences of element x in the list.
print(numbers.count(1))

# 7.copy(): Returns a shallow copy of the list
numbers2=numbers.copy()
numbers2[0]

#8.insert(index, x): Inserts element x at the specified index.
numbers = [1, 2, 4, 5]
numbers.insert(2, 3)
print(numbers)  # Output: [1, 2, 3, 4, 5]


# pop([index]): Removes and returns the element at the specified index. 
# If no index is specified, removes and returns the last element.
numbers = [1, 2, 3, 4, 5]
popped = numbers.pop(2)
print(popped)   # Output: 3
print(numbers)  # Output: [1, 2, 4, 5]

# remove(x): Removes the first occurrence of element x from the list.
numbers = [1, 2, 3, 4, 5]
numbers.remove(3)
print(numbers)  # Output: [1, 2, 4, 5]

# clear(): Removes all elements from the list.
numbers = [1, 2, 3, 4, 5]
numbers.clear()
print(numbers)  # Output: []
