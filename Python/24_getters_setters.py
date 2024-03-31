# getters and setters are used to control access to class attributes 
# and provide a way to encapsulate the internal state of objects. 
# They are commonly used to enforce data validation, perform calculations,
#  or trigger actions when getting or setting attribute values.

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Perform validation if needed
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError("Name must be a string")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        # Perform validation if needed
        if isinstance(value, int) and value >= 0:
            self._age = value
        else:
            raise ValueError("Age must be a non-negative integer")

# Creating an instance of the Person class
person = Person("Alice", 30)

# Getting attribute values using getters
print("Name:", person.name)
print("Age:", person.age)

# Setting attribute values using setters
person.name = "Bob"
person.age = 25

print("Updated Name:", person.name)
print("Updated Age:", person.age)

# We define a Person class with private attributes _name and _age.
# We use the @property decorator to create getter methods for accessing the attributes name and age.
# We use the @<attribute>.setter decorator to create setter methods for setting the attributes name and age.
# Inside the setter methods, we can perform validation checks on the input values before updating the attributes.