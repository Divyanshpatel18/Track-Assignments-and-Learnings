# Set Operations:
# Sets support various operations like union, intersection, difference, and symmetric difference.


set1 = {1, 2, 3}
set2 = {3, 4, 5}
#1. Union
union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}
print(set1.union(set2))
# 2.Intersection
intersection_set = set1 & set2
print(intersection_set)  # Output: {3}
print(set1.intersection(set2))

# 3.Difference
difference_set = set1 - set2
print(difference_set)  # Output: {1, 2}
print(set1.difference(set2))

# 4. Symmetric Difference
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}
print(set1.symmetric_difference(set2))

print(set1,set2)

# 5.update
set1.update(set2) # put values of set2 in set1
print(set1,set2)

#6.intesection update
set1.intersection_update(set2)
print(set1)

#7 add(element): Adds a single element to the set.
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange'}


#8 update(iterable): Adds multiple elements from an iterable to the set.
fruits = {"apple", "banana", "cherry"}
fruits.update(["orange", "grape"])
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange', 'grape'}

# Removing Elements:
#9 remove(element): Removes a specified element from the set. 
# Raises a KeyError if the element is not present.
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)  # Output: {'apple', 'cherry'}

#10 discard(element): Removes a specified element from the set if it is present. 
# Does not raise an error if the element is not present.
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)  # Output: {'apple', 'cherry'}

#11 pop(): Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.
fruits = {"apple", "banana", "cherry"}
removed_element = fruits.pop()
print(removed_element)  # Output: the removed element

#12 clear(): Removes all elements from the set, leaving it empty.
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)  # Output: set()

# Set Relationship Methods:
# issuperset(other_set): Returns True if the set contains all elements of the specified other_set,
# otherwise returns False.
set1 = {1, 2, 3, 4, 5}
set2 = {2, 4}
print(set1.issuperset(set2))  # Output: True

# issubset(other_set): Returns True if all elements of the set are present in the specified other_set,
# otherwise returns False.
set1 = {1, 2, 3, 4, 5}
set2 = {2, 4}
print(set2.issubset(set1))  # Output: True

# isdisjoint(other_set): Returns True if the set has no elements in common with the specified other_set
# , otherwise returns False.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2))  # Output: True

#del delete the entire set and it is not no more present
del set1
print(set1)