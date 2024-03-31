# Method overriding in Python occurs when a subclass defines a method that already exists in its superclass,
# with the same name and signature. By doing this, the subclass provides a specific implementation of the method,
#  which is different from that of the superclass.
#  When an object of the subclass calls the overridden method, the subclass's implementation is invoked instead of 
#  the superclass's implementation.

# import math

# class Shape:
#     def area(self):
#         pass  # This method will be overridden by subclasses

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
    
#     def area(self):
#         return self.width * self.height

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         return math.pi * self.radius ** 2

# # Creating instances of subclasses
# rectangle = Rectangle(5, 10)
# circle = Circle(7)

# # Calculating areas
# rectangle_area = rectangle.area()
# circle_area = circle.area()

# print("Area of rectangle:", rectangle_area)  # Output: 50
# print("Area of circle:", circle_area)        # Output: ~153.938

