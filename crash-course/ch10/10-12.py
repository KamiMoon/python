import json

file_name = 'favorite_number.json'

try:
    with open(file_name) as file_object:
        favorite_number_read = json.load(file_object)
        print('Your favorite number is ' + str(favorite_number_read))
except FileNotFoundError:
    favorite_number = input('What is your favorite number? ')
    with open(file_name, 'w') as file_object:
        json.dump(favorite_number, file_object)