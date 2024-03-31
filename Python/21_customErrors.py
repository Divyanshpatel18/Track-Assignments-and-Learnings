a=int(input("enter a positive number "))

try:
    if(a<0):
     raise ValueError("number should be positive")  #raising a  custom error and handling it
except ValueError as e:
      print("Error:",e)

# raising custom exception
# Example of raising a custom exception
class CustomError(Exception):
    pass

def check_value(value):
    if value < 0:
        raise CustomError("Value cannot be negative")

try:
    check_value(-5)
except CustomError as e:
    print("Error:", e)

# The raise statement is used to raise an exception when a certain condition is met.
# For built-in exceptions, you can pass an optional message to provide additional context about the error.
# For custom exceptions, you define a class that inherits from Exception 
# and use it to raise specific types of errors.
# In the try block, the raised exceptions are caught using except blocks, where you can handle the error as needed.