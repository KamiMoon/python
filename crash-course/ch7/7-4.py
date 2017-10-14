active = True

while active:
    pizza = input('Enter toppings: ')

    if pizza == 'quit':
        active = False
    else:
        print('Added ' + pizza + ' topping to pizza')