with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)


# with open('pi_digits.txt') as file_object:
#    lines = file_object.readlines()
#
# for line in lines:
#   print(line.rstrip())
#


# use second arge of open with 'w' to write
# r, w, a (append), r+ (read and write)

#with open( filename, 'w') as file_object:
#    file_object.write(" I love programming.")

# open automatically creates file if it doesn't exist

# write mode overwrites, use append mode to add






# Exceptions

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero.")
else:
    #only run if try block successful
    print()

# except FileNotFoundError
    # pass - do nothing


# str.split()


# JSON

# import json
# json.dump(object, file_object)
# json.load(file_object)



# return None is a good practice - instead of null