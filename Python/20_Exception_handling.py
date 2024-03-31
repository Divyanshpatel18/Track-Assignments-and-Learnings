# Exception handling in Python allows you to handle errors that occur during the execution of a program gracefully,
# preventing the program from crashing. 
# This is particularly important when dealing with user input, file operations, network operations, and 
# other scenarios where errors might occur.

# case 1
a=input("enter a number ")
try:
    b=int(a)*5/5
    print(b)
except Exception as e:
    print(e)
else:
    print("expression is evaluated")
print("important lines of code")

# case 2
a=input("enter a number ")
try:
    b=int(a)*5/5
    print(b)
except:
    print("invalid input")

print("Some lines of code")

# case 3
try:
    # Code block where an exception might occur
    result = 10 / 0
except ZeroDivisionError:
    # Exception handling block
    print("Cannot divide by zero!")
except ValueError:
    print("value error occured")
else:
    # Optional else block that executes if no exception occurs
    print("Division successful!")
finally:
    # Optional finally block that always executes, regardless of whether an exception occurred or not
    print("Execution completed")

# The finally block in Python is used to define cleanup actions that must be executed,
# regardless of whether an exception occurred or not in the preceding try block. 
# This block is typically used to release resources 
# or perform cleanup tasks that should always occur, such as closing files or database connections

try:
    file = open("1_Python.py", "r")
    # Perform operations on the file
    print(file.read())
except FileNotFoundError:
    print("File not found.")
finally:
    # Close the file, whether an exception occurred or not
    file.close()

#NOTE
# finally block code  vs code written outside try catch indentation
def fun1():
        try:
           l=[1,2,3,4]
           i=int(input("enter the index"))
           print(l[i])
           return 1
        except :
           # Exception handling block
           print("some error occured")
           return 0
        
        # print("i am always executed")# it will not print since we need a finally block which will always executed
        finally:
           print("will be executed always")
x=fun1()
print(x)