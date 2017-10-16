from collections import OrderedDict

glossary = OrderedDict()

glossary["tuple"] = "Immutable Python list"
glossary["list comprehension"] = "like a for loop for popluating a list"
glossary["dictionaries"] = "key value pair object"
glossary["lists"] = "Python lists"
glossary["blah"] = "blah"

for k, v in glossary.items():
    print(k + ": " + v + "\n")

glossary['a'] = 'abc'
glossary['b'] = 'abcb'
glossary['c'] = 'abcc'
glossary['d'] = 'abcd'
glossary['e'] = 'abce'

for k, v in glossary.items():
    print(k + ": " + v + "\n")
