cities = {
   'Omaha': {
       'country': 'USA',
       'population': 12,
       'fact': 'asdf'
   },
   'Plano': {
       'country': 'USA',
       'population': 1616,
       'fact': 'werew'
   },
   'Dallas': {
       'country': 'USA',
       'population': 123424,
       'fact': 'bg'
   }
}

for k,v in cities.items():
    print(k + ": " + str(v))