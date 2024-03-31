#  A class is a blueprint for creating objects.
#  It defines the properties (attributes) and behaviors (methods) that objects of the class will have.
#  Classes allow you to encapsulate data and functionality into a single unit
#  making code more organized and reusable

# 1.Class Definition (class ClassName:)
# Use the class keyword followed by the class name to define a class.

# 2.self is a reference to the current instance of the class 
# and is used to access instance variables and methods within the class.

# class Person:
#     name="divy"
#     occupation="volley player"
#     country="India"
#     def info(self):
#         print(f"name is {self.name},is a {self.occupation} lives in {self.country}")

# a=Person() #creating the object of class person
# a.info()
# a.name="divyansh"
# print(a.name)

# 4. construtor
#  The __init__() method is a special method called the constructor or initializer.
# It is automatically invoked when an object of the class is created.
#one arguement self is known as default constructor
class Person:
    def __init__(self,name,country,sport):
      self.name=name
      self.coutry=country
      self.sport=sport
      print("name is ",self.name, "and country is ",self.coutry,"and sport is",self.sport)

person=Person("Divy","India","cricket") #creating the object of class person
person2=Person("ABD","england","football") #creating the object of class person

# 5.decorators
# decorators are a powerful feature that allows you to modify or
# extend the behavior of functions or methods without changing their original definition.
# Decorators are essentially functions that wrap other functions or methods to provide additional functionality. 
# They are commonly used for tasks such as logging, authentication, memoization, and more.

# def say_hello():
#     print("Hello!")

# # Calling the decorated function
# say_hello()


def my_decorator(func):
    def wrapper():
        print("Say hello function needs to be called.")
        func()
        print("thank you for using say hello function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
#  or use the below line for the same 
# my_decorator(say_hello)()

# Calling the decorated function
say_hello()


#for arguments
def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("add function needs to be called.")
        func(*args,**kwargs)
        print("thank you for using add function")
    return wrapper

@my_decorator
def add(a,b):
    print("sum is",a+b)

add(5,3)