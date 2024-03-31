# Regular expressions (regex) in Python are a powerful tool for pattern matching and string manipulation.

# Python's built-in re module provides support for working with regular expressions. 

import re
# 1
# re.search(pattern, string): Searches for the first occurrence of the pattern in the string.
# If the pattern is found, it returns a Match object representing the first match, otherwise, it returns None.
# The search is not restricted to the beginning of the string; it searches throughout the entire string

# re.match(pattern, string): Matches the pattern only at the beginning of the string.
# re.findall(pattern, string): Finds all occurrences of the pattern in the string.
# re.finditer(pattern, string): Returns an iterator yielding Match objects for all non-overlapping matches.

pattern = r'cat'
text = '''cat sat on the mat and 
      the cat eat milk.'''

# print(re.search(pattern, text))
# print(re.findall(pattern, text))
# for match in re.finditer(pattern, text):
#     print(match)
# print(re.match(pattern,text))



# . (dot): Matches any single character except newline (\n).
# Example: a.b matches "axb", "a1b", "a@b", etc.

# ^: Matches the start of the string.
# Example: ^abc matches "abc" at the beginning of the string.

# $: Matches the end of the string.
# Example: xyz$ matches "xyz" at the end of the string.

# *: Matches zero or more occurrences of the preceding character or group.
# Example: ab* matches "a", "ab", "abb", "abbb", etc.

# +: Matches one or more occurrences of the preceding character or group.
# Example: ab+ matches "ab", "abb", "abbb", etc.

# ?: Matches zero or one occurrence of the preceding character or group.
# Example: colou?r matches "color" or "colour".

# {}: Specifies the exact number of occurrences of the preceding character or group.
# Example: a{3} matches "aaa".

# []: Defines a character class, matches any single character within the brackets.
# Example: [aeiou] matches any vowel.

# |: Alternation, matches either the expression before or after the pipe symbol.
# Example: cat|dog matches "cat" or "dog".

# \ (backslash): Escapes metacharacters, allowing them to be matched as literals.
# Example: \. matches a literal dot ".".

# (): Groups patterns together, capturing the matched substring.
# Example: (ab)+ matches "ab", "abab", "ababab", etc.


# Example for .
print(re.search(r'a..b', 'axxb'))  # Match found

# # Example for ^
print(re.search(r'^abc', 'abcdef'))  # Match found

# # Example for $
print(re.search(r'xyz$', 'wxyz'))  # Match found

# # Example for *
print(re.findall(r'ab*', 'ab abb abbb'))  # ['a', 'ab', 'abb', 'abbb']

# # Example for +
# print(re.findall(r'ab+', 'ab abb abbb'))  # ['ab', 'abb', 'abbb']

# # Example for ?
# print(re.findall(r'colou?r', 'color colour'))  # ['color', 'colour']

# # Example for {}
# print(re.findall(r'a{3}', 'aaa a aaaaa'))  # ['aaa', 'aaa']

# # Example for []
# print(re.findall(r'[aeiou]', 'hello'))  # ['e', 'o']

# # Example for |
# print(re.findall(r'cat|dog', 'I have a cat and a dog'))  # ['cat', 'dog']

# # Example for \
print(re.search(r'c\.d', 'c.d'))  # Match found

# # Example for ()
# print(re.findall(r'(ab)+', 'ab abab ababab'))  # ['ab', 'abab', 'ababab']