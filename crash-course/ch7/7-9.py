sandwich_orders = ['pastrami', 'Ham', 'pastrami', 'Cheese', 'Beef', 'pastrami']

finished_sanwiches = []

print('The deli has run out of pastrami')


while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    print('I made you a ' + sandwich)
    finished_sanwiches.append(sandwich)

print('made: ' + str(finished_sanwiches))