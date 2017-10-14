glossary = {
    "tuple": "Immutable Python list",
    "list comprehension": "like a for loop for popluating a list",
    "dictionaries": "key value pair object",
    "lists":  "Python lists",
    "blah": "blah"
}

for k, v in glossary.items():
    print(k + ": " + v + "\n")

glossary['a'] = 'abc'
glossary['b'] = 'abcb'
glossary['c'] = 'abcc'
glossary['d'] = 'abcd'
glossary['e'] = 'abce'

for k, v in glossary.items():
    print(k + ": " + v + "\n")
