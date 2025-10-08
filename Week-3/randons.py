import random

print(random.randint(5, 20))  # line 1
# What did you see on line 1?
# I saw a random integer between 5 and 20 inclusive everytime the line runs.

# What was the smallest number you could have seen, what was the largest?
# The smallest possible number is 5 and the largest possible number is 20.

print(random.randrange(3, 10, 2))  # line 2
# What did you see on line 2?
# I saw different random integers in this set of numbers {3, 5, 7, 9}.

# What was the smallest number you could have seen, what was the largest?
# The smallest possible number is 3 and the largest possible number is 9.

# Could line 2 have produced a 4?
# No it couldn't because it isn't in the range which only consists of odd numbers because the step size is 2.

print(random.uniform(2.5, 5.5))  # line 3
# What did you see on line 3?
# I saw different float numbers between 2.5 and 5.5.

# What was the smallest number you could have seen, what was the largest?
# The smallest possible number is 2.5 and the largest possible number is 5.5.

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))