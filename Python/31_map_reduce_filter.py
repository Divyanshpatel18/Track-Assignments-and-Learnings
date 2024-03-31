#
# 1.map(function, iterable): The map function applies the given function to each item
#     of the iterable (like a list, tuple, etc.) and returns a new iterator with the results. 
#     It takes two arguments: a function and an iterable.

# Squaring each element in a list
def square(x):
    return x*x

numbers = [1, 2, 3, 4, 5]
# newl=[]
# for item in numbers:
#     newl.append(square(item))
# print(newl)
#instead of creating a new list and passing item into cube function use the map function
squared = map(square, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]
# or use can use the map function /
# squared = map(lambda x: x**2, numbers)

# 2.
# filter(function, iterable): The filter function constructs a new iterator from elements of the iterable for
# which the function returns true. It takes two arguments: a function and an iterable.
# Filtering even numbers from a list
     
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def iseven(x):
     if(x%2==0):
          return True
     else: 
          return False    
even_numbers = filter(iseven, numbers)
# or use below
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4, 6, 8, 10]

# reduce(function, iterable[, initializer]):
# The reduce function applies a rolling computation to sequential pairs of values in the iterable.
# It's available in the functools module in Python 3.x. 
# The function argument must take two arguments  and return a single value.
#  The initializer is an optional initial value. If provided, reduce will performthe computation using 
# initializer and the first item in the iterable,then apply the function to the result and the next item, and so on.

from functools import reduce

# Summing up elements in a list
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # Output: 15
