import random

upper_limit = int(input("Enter the upper Limit: "))
number = random.randint(1, upper_limit)

no_of_trials = 0
while True:
    trial = int(input("Enter your guess: "))
    no_of_trials = no_of_trials+1
    if trial > number:
        print ("your guess is too high, try one more time")
    elif trial < number:
        print ("your guess is too low, try one more time")
    else:
        print (f'*** congratulations ***, you did it, after {no_of_trials} trials')
        break
