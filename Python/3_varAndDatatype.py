# Variables in Python are used to store data values. 
#  Python does not require you to declare a variable's type explicitly
# Assigning values to variables
x = 10  # x is an integer
y = 3.14  # y is a float
name = "Alice"  # name is a string
is_student = True  # is_student is a boolean


#   DATA TYPES
# Numeric Types
integer_var = 10
float_var = 3.14
complex_var=complex(8,2) #(8+2j)

# Sequence Types
string_var = "Hello, Python!"
list_var = [1, 2, 3, 4]
tuple_var = ('a', 'b', 'c')

# Mapping Type
dictionary_var = {'name': 'Alice', 'age': 30}

# Set Types
set_var = {1, 2, 3}
frozenset_var = frozenset({4, 5, 6})

# Boolean Type
boolean_var = True

# None Type
none_var = None

# Binary Types
bytes_var = b'hello'
bytearray_var = bytearray(b'world')

# Printing variables and their types
print("Integer variable:", integer_var, "Type:", type(integer_var))
print("Float variable:", float_var, "Type:", type(float_var))
print("String variable:", string_var, "Type:", type(string_var))
print("List variable:", list_var, "Type:", type(list_var))
print("Tuple variable:", tuple_var, "Type:", type(tuple_var))
print("Dictionary variable:", dictionary_var, "Type:", type(dictionary_var))
print("Set variable:", set_var, "Type:", type(set_var))
print("Frozenset variable:", frozenset_var, "Type:", type(frozenset_var))
print("Boolean variable:", boolean_var, "Type:", type(boolean_var))
print("None variable:", none_var, "Type:", type(none_var))
print("Bytes variable:", bytes_var, "Type:", type(bytes_var))
print("Bytearray variable:", bytearray_var, "Type:", type(bytearray_var))


a=9
print(type(a))