# Tuples are like list, used to store a sequence of objects but tuples are immutable,
# which means we cannot change it once we create them

numbers = (1, 2, 3, 4, 5, 4)

# Count returns the number of occurrence of an element
# This returns 2
print(numbers.count(4))

# Index returns the index of the first occurrence
# This returns index 3
print(numbers.index(4))

# Methods that start with a __ are called "magic methods"
# Special Method Description
# .__init__() Provides an initializer in Python classes
# .__str__() and
# .__repr__() Provide string representations for objects
# .__call__() Makes the instances of a class callable
# .__len__() Supports the len() function
