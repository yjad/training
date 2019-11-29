#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.
import random
# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':'Springfield',
    'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':'Topeka',
    'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':'Augusta',
    'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':'Lansing',
    'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':'Jefferson City',
    'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':'Carson City',
    'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
    'New York': 'Albany', 'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
    'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':'Nashville',
    'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':'Montpelier',
    'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
    'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
# Generate

def one_quiz(quiz_no):
    f = open(f'quiz_{quiz_no+1}.txt','w+t')
    f.write('Student Name:\n\n')
    f.write('Date:\n\n')
    f.write('Period:\n\n')

    states = list(capitals)
    capitals_list = list(capitals.values())

    random.shuffle(states)
    for i, state in enumerate(states):
        correct_answer = capitals[state]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        answers_options = wrong_answers + [correct_answer]
        random.shuffle(answers_options)

        #print (answers_options)
        f.write(f'{i+1}- What is the capital of {state}?\n')

        for j in range(0, 4):
            f.write (f'{chr(ord("A")+j)} - {answers_options[j]}\n')

        f.write('\n\n')

No_of_quiz = 2

for i in range(No_of_quiz):
    one_quiz(i)