"""
CP404 Practical
List warmup
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

# what values do the following expressions have?
# The following expression have a list containing integers as elements.

# Change the first element of numbers to "ten"
numbers[0] = "ten"
numbers[-1] = 1

# print all the elements from numbers except the first two
print(numbers[2:])

# print whether 9 in an element of numbers
print(9 in numbers)