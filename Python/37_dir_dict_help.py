# dir(): The dir() function returns a list of valid attributes for the specified object.
#  If no object is specified, it returns the attributes for the current scope.
#  It's commonly used for exploring the attributes of modules, classes, or objects.


#  dunder method - __ vale
# Getting attributes of a module
import math
print(dir(math))

# Getting attributes of a data type
print(dir(list))

# Getting attributes of an object
my_list = [1, 2, 3]
print(dir(my_list))

print(my_list.__add__)



# __dict__ is a special attribute in Python that holds a dictionary 
# containing the namespace of a class or an instance of a class. 
class MyClass:
    class_variable = 10
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def method(self):
        return self.a + self.b

# Accessing __dict__ attribute of the class
print(MyClass.__dict__)

# Creating an instance of MyClass
obj = MyClass(3, 5)

# Accessing __dict__ attribute of the instance
print(obj.__dict__)


# help(): The help() function in Python is used to display documentation about modules, 
# , classes, etc. It provides an interactive way to access information about Python objects.
# Getting help about a specific module
import math
help(math)

# Getting help about a specific function
help(math.sqrt)
