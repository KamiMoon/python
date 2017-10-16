import json

file_name = 'favorite_number.json'

favorite_number = input('What is your favorite number? ')

with open(file_name, 'w') as file_object:
    json.dump(favorite_number, file_object)

try:
    with open(file_name) as file_object:
        favorite_number_read = json.load(file_object)
        print('Read ' + str(favorite_number_read))
except FileNotFoundException:
    print('File not found')