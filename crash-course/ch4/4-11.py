pizzas = ['Cheese', 'Pepperoni', 'Hamburger']
friend_pizzas = pizzas[:]

pizzas.append('Canadian Bacon')
friend_pizzas.append('Chicken')

print('My favorite pizzas are: ')

for pizza in pizzas:
    print("I like " + pizza.lower() + " pizza")


print('My friends pizzas are: ')

for pizza in friend_pizzas:
    print("He likes " + pizza.lower() + " pizza")
