# A range function generates and stores a sequence of numbers

numbers = range(5)

# Print range(0, 5)
print(numbers)

# To print all the numbers inside the range
# Prints 0 1 2 3 4
for number in numbers:
    print(number)

# A range given 2 numbers
# Prints 5 6 7 8 9 , does not include 10
numbers = range(5, 10)
for number in numbers:
    print(number)

# Given a third value, this value is a step
numbers = range(10, 18, 2)
for number in numbers:
    print(number)

# Without storing the range in a variable
for number in range(10):
    print(number)
