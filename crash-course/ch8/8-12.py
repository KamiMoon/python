def summary_sandwich(*items):
    print('Created a sandwich with: ')
    for item in items:
        print(item)

summary_sandwich('Eggs', 'Beef')
summary_sandwich('Lettuce')
summary_sandwich('Rice', 'Beer')