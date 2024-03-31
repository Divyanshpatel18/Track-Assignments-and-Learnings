# # for loop

# # Iterate over a list
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)
#     for char in fruit:
#         print(char)
# # Iterate over a string
# for character in "hello":
#     print(character)

# # Iterate over a range
# for i in range(5): #(0,n-1)
#     print(i)
# for i in range(6,11):
#     print(i)

# Using range() function with step
# for i in range(0, 10, 2):  # start at 0, stop before 10, step by 2
#     print(i)
# # Reverse iteration with negative step
# for i in range(10, 0, -1):  # start at 10, stop before 0, step by -1 (backward)
#     print(i)
# Using step within the loop
fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
for i in range(0, len(fruits), 2):  # iterate over indices with step 2
    print(fruits[i])


# while loop

count = 0
while count < 5:
    print(count)
    count += 1

# Using else with loops
for i in range(5):
    print(i)
else:
    print("Loop completed ")