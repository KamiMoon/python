
with open('guest_book.txt', 'a') as file_object:
    while True:
        name = input('What is your name? ')
        if name == 'quit':
            break
        file_object.write(name + "\n")