with open('poll_responses.txt', 'a') as file_object:
    while True:
        why = input('Why do you like programming? ')
        if why == 'quit':
            break
        file_object.write(why + "\n")