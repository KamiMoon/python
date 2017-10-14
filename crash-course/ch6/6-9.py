favorite_places = {
    'bob': ['usa'],
    'alex': ['uk', 'japan', 'germany'],
    'jeff': ['africa', 'usa']
}

for k, v in favorite_places.items():
    print(k + ": ")
    for place in v:
        print(place + " ")