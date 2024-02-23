# For loop syntax

numbers = [1, 2, 3, 4, 5]

for item in numbers:
    item += 2
    print("we are adding 2 each iteration, the result =  " + str(item))


# Now convert it to a while loop

i = 0
while 1 < len(numbers):
    print(numbers[i])
    i += 1
