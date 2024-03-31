# Inheritance is a fundamental concept in object-oriented programming (OOP) that allows 
# you to create a new class (subclass) based on an existing class (superclass)
# The subclass inherits attributes and methods from the superclass 
# and can also have its own additional attributes and methods
# class Human:
#       def man(self):
#           print("its a male living being")

# class Employee(Human):
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
    
#     def showDetails(self):
#         print("employee name is",self.name,"and id is",self.id)

# class Manager(Employee):
#     def showTask(self):
#         print("the task is human resources")

# e1=Employee("Virat",101)
# e1.showDetails()
# e2=Manager("Kohli",102)
# e2.showDetails() 
# e2.showTask()
# e1.man()
# e2.man()

# MUTIPLE INHERITANCE
class employee:
  def __init__(self,name):
    self.name=name
  def show(self):
    print(f"the name is {self.name}")

class dancer:
  def __init__(self,dance):
    self.dance=dance
  def show(self):
    print(f"the dance is {self.dance}") 

#the order in the below paranthesis defines which class method will be called ,if the methods are same in both class
class DancerEmployee(dancer,employee):
  def __init__(self, name,dance):
    self.name=name
    self.dance=dance

d=DancerEmployee("divy","salsa")
# print(d.name)
# print(d.dance)
d.show()
print(DancerEmployee.mro())#defines the order of execution of classes