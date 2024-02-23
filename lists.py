# List has indexes, the indexes can go from left to right starting with index 0,
# or from right to left starting at index -1

names = ["Marcela", "Ruben", "Santiago", "Ruth", "Laura"]

# Print Laura
print(names[-1])
print(names[4])

# Change a value in the list
names[3] = "Rut"
print(names)

# To return a range of elements of the list
# Excluding the last one
# Returns a new list, does not modify the original list
print(names[0:3])


# List methods

# List are also objects with methods

# Add a new number to the list
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)

# Insert a number in a specific position
numbers.insert(0, -1)
print(numbers)

# Remove a specific number
numbers.remove(3)
print(numbers)

# Remove all the elements in the list
numbers.clear()
print(numbers)

# Check if a value exist in the list
# This method returns a boolean
print(1 in numbers)

# Check the length of the list
print(len(numbers))
