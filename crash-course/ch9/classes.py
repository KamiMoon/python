class Dog():

    #constructor with two leading and trailing _
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
        print(self.name.title() + " is now rolling over.")

#self is required on all methods otherwise it does give an error

# 2.7:  class ClassName(object)

# can directly access attributes - no private scope

# Inheritance
    #1 - must be part of current file
    #2 - class ClassName(parent)
    #3 - super().__init__(make, model, year) in the constructor
        #2.7 - super(ClassName, self).__init__(make, model, year)
    #4 - extra attributes can come after super
    #5 - override - use same method name and that is used instead

# Python Standard Library
    # OrderedDict - ordered dictionary for keys
        # from collections import OrderedDict
    # from random import randint
        # x = randint(1, 6)

# https://pymotw.com/3/