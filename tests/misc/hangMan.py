import random

words=['Kamel', 'cat', 'dog', 'horse', 'donkey', 'bear', 'fox']

selected_word = random.choice(words)

no_of_trials = 0
while (True):
    guess = input('Enter part/full name of the animal: ')
    no_of_trials = no_of_trials + 1
    if guess == selected_word:
        print(f'*** you did it after {no_of_trials}')
        break

    found = selected_word.find(guess)

    #print (selected_word,": ", found)

    if found != -1:
        print ('Exists -->')
    else:
        print ('not valid!')

