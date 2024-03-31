# Dunder or magic methods in Python are special methods with double underscores (__) at the beginning and
#  end of their names. They provide a way to define how objects behave in various contexts,
#  such as arithmetic operations, comparisons, string representations, and more. 
#  methods are called "magic" or "dunder" (double underscore) methods because of their special
#  behavior and the syntax used to define them.

# __init__(self, ...):
# This method is called when an instance of the class is created. It initializes the attributes of the object.

# __str__(self): 
# This method returns the string representation of the object when str() function is called on it. 
# It's used for informal string representations, such as for printing.

# __repr__(self): 
# This method returns the official string representation of the object. 
# It's used for debugging and logging, and it should ideally return a string that, when evaluated with
# Python, produces an equivalent object.

# __len__(self): This method returns the length of the object when len() function is called on it.
# It's commonly used for sequences like lists, tuples, and strings.

# __getitem__(self, key): This method allows objects to be indexed like sequences or mappings. 
# It's called to retrieve the value associated with the given key.

# __setitem__(self, key, value): This method allows objects to be assigned values like mappings. 
# It's called to set the value associated with the given key.

# __add__(self, other): This method allows objects to support the addition operator (+).

# __eq__(self, other): This method defines the behavior of the equality operator (==). 
# It's called when comparing objects for equality.

# __lt__(self, other), __le__(self, other), __gt__(self, other), __ge__(self, other): T
# hese methods define the behavior of comparison operators (<, <=, >, >=), respectively.


#suppose file name is emp.py
from typing import Any


class Employee:
    def __init__(self,name):
        self.name=name

    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
    
    def __str__(self):
        return f"the name is {self.name} str"
    def __repr__(self):
        return f"the name is {self.name} repr"
    
    def __call__(self):
        print("hey i am good")

# e=Employee("Divy")
# print(e.name)
# print(len(e))#we defined func as __len__ but using as len(e)

