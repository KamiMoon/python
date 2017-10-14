#slices

cubes = [value**3 for value in range(1, 11)]

print('All the items ' + str(cubes))
print('The first three items in the list are: ' + str(cubes[:3]))
print('The first three items in the middle are: ' + str(cubes[4:7]))
print('The last three items in the list are: ' + str(cubes[-3:]))