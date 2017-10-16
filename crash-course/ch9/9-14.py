from random import randint

class Die(object):

    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        print(randint(1, self.sides))

sixDie = Die(6)
tenDie = Die(10)
twentyDie = Die(20)

for number in range(1, 11):
    sixDie.roll_die()

print("rolling 10")

for number in range(1, 11):
    tenDie.roll_die()

print("rolling 20")

for number in range(1, 11):
    twentyDie.roll_die()

