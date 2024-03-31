number = 10

match number:
    case 1:
        print("Number is 1")
    case 5:
        print("Number is 5")
    case 10:
        print("Number is 10")
    case _ if number % 2 == 0:
        print("Number is even")
    case _:
        print("Number doesn't match any case and is odd")

# Output:
# Number is 10
# Number is even

# Output:
# Number is 10
# Number is even
