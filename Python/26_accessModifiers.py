# # In Python, access modifiers are used to control the visibility
# #  and accessibility of class members (attributes and methods).
# #  Python does not have traditional access modifiers like public, private,
# #  and protected as in some other programming languages (e.g., Java), 
# #  but it provides a mechanism using naming conventions and special identifiers to achieve similar behavior. 
# #  Here are the commonly used conventions for access control in Python:

# # Public:By default, all attributes and methods in a class are public and can be accessed from outside the class.

# # Protected: Conventionally, attributes and methods that are intended to be accessed within the class itself 
# # and its subclasses are prefixed with a single underscore _. However, this is merely a convention, 
# # and the attribute or method can still be accessed from outside the class.

# # Private: Attributes and methods that are intended to be accessed only within the class itself are 
# #  prefixed with a double underscore __. Python performs name mangling on such attributes/methods, 
# #  making them less accessible outside the class. However, they can still be accessed using a mangled name.

# class MyClass:
#     def __init__(self):
#         self.public_attribute = "Public"          # Public attribute
#         self._protected_attribute = "Protected"   # Protected attribute
#         self.__private_attribute = "Private"      # Private attribute

#     def public_method(self):
#         print("Public method")

#     def _protected_method(self):
#         print("Protected method")

#     def __private_method(self):
#         print("Private method")

# # Create an instance of MyClass
# obj = MyClass()

# # Accessing public attributes and methods
# print(obj.public_attribute)
# obj.public_method()

# # Accessing protected attributes and methods (conventionally)
# print(obj._protected_attribute)
# obj._protected_method()

# # Accessing private attributes and methods (mangled name)
# # Python mangles the name by adding _ClassName prefix
# print(obj._MyClass__private_attribute)
# obj._MyClass__private_method()


# # public_attribute and public_method() are public members, accessible from outside the class.
# # _protected_attribute and _protected_method() are conventionally considered protected,
# # but they can still be accessed from outside the class.
# # __private_attribute and __private_method() are private members,
# # but they can still be accessed using mangled names from outside the class.

class accesss:
    def __init__(self):
        self.public ="public variable"
        self._protected="protected variable"
        self.__private="private variable"

    def public1(self):
        print("public method")
        print(self.__private)
    def _protected1(self):
        print("protected method")
    def __private1(self):
        print("private method")

class subaccess(accesss):
    pass
a1=accesss()
# a1.public1()
a2=subaccess()
a2._accesss__private1()