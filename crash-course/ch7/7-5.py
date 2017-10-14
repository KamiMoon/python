active = True

while active:
    age = input('Enter age: ')
    if(age == 'quit'):
        active = False
        break

    age = int(age)
    if age < 3:
        print('Ticket is free')
    elif age >=3 and age <= 12:
        print('Ticket is $10')
    elif age > 12:
        print('Ticket is $15')