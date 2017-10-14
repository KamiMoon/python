favorite_numbers = {
    'eric': [5],
    'bob': [12, 7],
    'zeus': [9, 6, 9]
}

for k, v in favorite_numbers.items():
    print(k + ": ")
    for num in v:
        print(str(num) + " ")