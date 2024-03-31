# In Python, you can use the input() function to get user input from the command line.
# This function reads a line from the input, converts it to a string, and returns that string.
# a=input()
# print("my name is",a)

# a=input("Enter your name ")
# print("my name is",a)

#input always take and return input as string whether its a number therefore need to typecast it to int
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(a+b) # print(int(a)+int(b)) if not using int() with input