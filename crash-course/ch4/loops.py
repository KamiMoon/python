magicians = ['alice', 'david', 'carl']

for magician in magicians:
    print(magician)


# range(1,5) function to genrate numbers 1-4

# list() to convert to list


numbers = list(range(1,6))
print(numbers)

# min, max, sum on list of numbers

#list comprehension:  like a for loop to populating a list
squares = [value**2 for value in range(1, 11)]
print(squares)

#slicing a list
# stops 1 index before the index you specify, like range

# [:3] - first 3

# [:] - copy


# Tuples - immutable lists that use (800, 700)