# functions are blocks of code that perform a specific task and are reusable throughout your program. 
def greeting(name):
    print("hello",name)

greeting("shanu")

#return values
def add(a,b):
    return a+b

print(add(5,2))

#default arguements
def greet(name="divy",a=3,b=5):
    print(name)
    print(a+b)
greet()
greet("shanu")


# Variable Number of Arguments:
# Functions can accept a variable number of arguments using *args and **kwargs in the parameter list.

def addall(*args):#use args as tuple
    sum=0
    for i in args:
        sum+=i
    print(sum)
addall(1,2,3,1,1)

#pass :we can write that function code later
def multiply(a,b):
    pass

#to not match order
def add(a,b):
    print(a+b)
add(b=4,a=10)