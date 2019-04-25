# LIST CREATION
list1 = []
list2 = list()
print("List 1 {}".format(list1))
print("List 2 {}".format(list2))

if list1 == list2:
    print("The list are equal")

print(list("The list are equal"))

# Methods on a new list affects original
even = [2, 4, 6, 8]
another_even = even
another_even.sort(reverse=True)
print(even is another_even)

#
another_even = list(even)
print(even is another_even)

odd = [1, 3, 5, 7, 9]
numbers = [even, odd]
for number_set in numbers:
    print(number_set)
    for number in number_set:
        print(number)
