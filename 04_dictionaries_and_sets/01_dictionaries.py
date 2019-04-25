# Dictionary is list that is acceded using a keys not an index
# Keys can not be duplicated
# Values can hold different type of data
# We can use tuples as keys but not lists because they are not inmutable
fruit = {"orange": "a sweet orange citrus fruit",
         "apple": "a good fruit to make cider"}

print(fruit)
print(fruit["apple"])

# Remove items from collection with 'del'
# If no key is defined it removes the whole dictionary
del fruit["apple"]
print(fruit)

# Clean dictionary
fruit.clear()
print(fruit)



fruits = {"fruit1": "one very first fruit",
         "fruit2": "a second fruit"}

# List keys and values
print(fruits.keys())
print(fruits.values())

# If we need to sort the dictionary we have to do it using the keys
sortedFruits = sorted(fruits.keys())
print(sortedFruits)