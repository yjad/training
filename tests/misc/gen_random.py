import random


class Dice:

    def roll(self):
        r1 = random.randint(1,6)
        r2 = random.randint(1,6)
        return r1,r2


d =Dice()
# r1,r2 = d.roll()
# print ('roll: ({r1}, {r2})')
for i in range(6):
    print (d.roll())