even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
numbers_in_order = sorted(numbers)

if numbers == numbers_in_order:
    print("The lists are equal")
else:
    print("The lists are not equal")

if sorted(numbers) == numbers_in_order:
    print("The lists are equal")
else:
    print("The lists are not equal")

# sort list method actually changes the array
numbers.sort()
if numbers == numbers_in_order:
    print("The lists are equal")
else:
    print("The lists are not equal")
