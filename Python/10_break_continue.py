# break Statement:

# The break statement is used to exit the loop prematurely. When Python encounters a break statement inside a loop
# , it immediately exits the loop
# and continues execution at the next statement after the loop.
# Example of using break
for i in range(10):
    if i == 5:
        break
    print(i)

# continue Statement:

# The continue statement is used to skip the rest of the code inside the loop for the current iteration 
# and proceed to the next iteration of the loop.
# Example of using continue
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
