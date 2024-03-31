# A lambda function in Python is a small anonymous function that can have any number of arguments, 
# but can only have one expression. Lambda functions are often used when you need a simple function for a 
# short period and don't want to define a regular function using the def keyword.

# The syntax of a lambda function is:
# lambda arguments: expression
# 1.
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8
# 2.
#giving function as an arguement
def app1(fx,value1,value2):
    return 6+fx(value1,value2)
print(app1(add,2,3))
# 3.
 #performing above fucntionality using lambda function
print(app1(lambda x,y:x+y,4,3))
# 4.Using lambda function with map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# 5.Using lambda function with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# 6.
# #multiple lines in a lambda function but not recommended and none instead of print statement
# multiline_lambda = lambda x, y: (
#     x + y,
#     x - y,
#     x * y,
#     # you cannot use if else or multiline code inside a lambda function
#     # print("definitelty you wll get an output")
#     # if(x<y):
#     #    print(x)
#     # else:
#     #    print(y)
# )

# result = multiline_lambda(5, 3)
# print(result)  # Output: (8, 2, 15)
