my_list = list(range(10))
print(my_list)

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

print(even)
print(odd)

# Ranges represents sequences that follow a parent, they are not lists but can be used to iterate processes

small_decimals = range(0, 10)
print(small_decimals)
print(small_decimals.index(3))

odd = range(1, 10000, 2)
#print(odd)
print(odd.index(985))
print(odd[985])