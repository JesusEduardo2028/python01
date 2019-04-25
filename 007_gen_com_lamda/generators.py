import sys


# GENERATORS

def my_range(n: int,):
    """yield return the yielded value and puts the function in a suspended value, so the next time its called it
    wakes ups and continues where it was stopped. It return a generator object.
    """
    print('my_range_starts')
    start = 0
    while start < n:
        print("my range is returning {}".format(start))
        yield start
        start += 1


# Range and list are iterators, big_range is special because is a GENERATOR, that's why occupies less memory
big_range = my_range(5)
print(next(big_range))
print(next(big_range))
print(next(big_range))
print("big_range is {} bytes".format(sys.getsizeof(big_range)))

# create a list containing all values in big_range

big_list = []

for val in big_range:
    big_list.append(val)


print("big_list is {} bytes".format(sys.getsizeof(big_list)))
# print(big_range)
print(big_list)