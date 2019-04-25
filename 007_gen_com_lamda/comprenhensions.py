numbers = [1,2,3,4,5,6]

"""
    List comprehensions
    First part is the expression we want to return, the second part is an iteration over a sequence
"""

squares = [number ** 2 for number in numbers]
print(squares)

# Set comprenhensions
squares = {number ** 2  for number in numbers}

print(squares)