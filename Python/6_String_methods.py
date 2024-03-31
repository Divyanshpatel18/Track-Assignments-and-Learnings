# Python provides a rich set of built-in string functions that allow you to manipulate and work with strings effectively. Here are some commonly used string functions in Python:


# STRINGS ARE IMMUTABLE
# method just create new strings but not change the original string
# 1.len(): Returns the length of the string.
s = "Hello, World!"
print(len(s))  # Output: 13

#2.lower(): Converts all characters in the string to lowercase.
s = "Hello, World!"
print(s.lower())  # Output: hello, world!

#3. upper(): Converts all characters in the string to uppercase.
s = "Hello, World!"
print(s.upper())  # Output: HELLO, WORLD!

#4. strip(): Removes leading and trailing whitespace characters from the string.
s = "  Hello, World!  "
print(s.strip())  # Output: Hello, World!
s1="!!!!!hello!!!!"
print(s1.strip("!")) #lstrip ,rstrip can also be used

#5. replace(): Replaces all occurrences of a specified substring with another substring.
s = "Hello, World!"
print(s.replace("Hello", "Hi"))  # Output: Hi, World!

#6.split(): Splits the string into a list of substrings based on a delimiter.
s = "Hello, World!"
print(s.split(","))  # Output: ['Hello', ' World!']

#7. join(): Joins elements of an iterable (e.g., list) into a string using the specified separator.
lst = ['Hello', 'World']
print('-'.join(lst))  # Output: Hello-World

#8. find(): Returns the lowest index of the substring if found, otherwise returns -1.
s = "Hello, World!"
print(s.find("World"))  # Output: 7

#9. startswith(): Checks if the string starts with the specified prefix.
s = "Hello, World!"
print(s.startswith("Hello"))  # Output: True

#10. endswith(): Checks if the string ends with the specified suffix.
s = "Hello, World!"
print(s.endswith("World!"))  # Output: True

#11. count(): Returns the number of occurrences of a substring in the string.
s = "Hello, World!"
print(s.count("l"))  # Output: 3

#12.capitalize()
s="this is shANU"
print(s.capitalize())#first char to uppercase and remaning ones to lower

#13. center
s="hello world"
print(s.center(50))

#14. isalnum()
s="heloo900"
print(s.isalnum())

#15 isspace() return true if string contains whitespace
#16 istitle() check if first world is capitalized
#17 swapcase() upper to lower and lower to upper