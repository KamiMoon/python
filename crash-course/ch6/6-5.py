rivers = {
   'nile': 'egypt',
   'missipplie': 'usa',
   'missouri': 'usa',
   'yellow': 'china',
   'blah': 'blah'
}

for k,v in rivers.items():
    print('The ' + k + " runs through " + v)

for k in rivers.keys():
    print(k)

for v in rivers.values():
    print(v)