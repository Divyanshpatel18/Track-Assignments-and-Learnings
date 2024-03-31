
# In Python, strings are sequences of characters, enclosed in either single quotes (' ') or double quotes (" "). 
# Strings are immutable, meaning once they are created, their contents cannot be changed. 

#1.STRING CAN BE IN SINGLE OR DOUBLE QUOTES
# name="Divyansh"
# friend='virat'
# print("hello",name)

#2. CAN USE \ FOR "" PRINTING
string="he said ,\"he want to eat apple\"" # or string='he said ,"he want to eat apple"'

#3. triple single quotes or triple double quotes for multi line string
string2="""hey
I 
am 
good"""
print(string2)
#4. PRINTING INDEX(indexing starts from 0)
string3="apple"
print(string3[0])
print(string3[-1]) # will give you the last character

#5.PRINTING EVERY CHARACTER OF STRING USING FOR LOOP
# for character in string2:
#      print(character)

#6.You can extract a substring (a portion of the string) using slicing:
str="helloshan"
print(str[3:]) #from index 3 to end
print(str[4:7]) #from index 4 to index 7-1 i.e. 6
print(str[:4])#same as str[0:4] add 0 automatically
print(str[0:-3])# print(str[0:len(str)-3])
print(str[-2:-4])# will print nothing

#7.CONCATENATION
my_string ="hello"
another_string="divy"
new_string = my_string + ' ' + another_string
print(new_string)  

# 8.STRING FORMATTING
name = "Alice"
age = 30
print("My name is %s and I am %d years old." % (name, age))
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")

# f-string
letter="hey my is {1} and i am from {0}"
country="india"
name="divy"
weight=75.23243434
print(letter.format(name,country))
print(f"my name is {name}  and i live in {country} and age is {weight:.2f}")
print(f"{2*30}") # also you can use for calc which will return result as string
# retain ur fstring
print(f"my name is {{name}}  and i live in {{country}} and age is {{weight:.2f}}")
