from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#from chatterbot import chatterbot_corpus

# Create a new chat bot named Charlie
chatbot = ChatBot('Yahia',
                storage_adapter='chatterbot.storage.SQLStorageAdapter',
                logic_adapters=[
                    'chatterbot.logic.MathematicalEvaluation',
                    'chatterbot.logic.TimeLogicAdapter',
                    'chatterbot.logic.BestMatch'
                ],
                database_uri='sqlite:///database.sqlite3'
                )

# trainer = ListTrainer(chatbot)
#
# trainer.train([
#     "Hi, can I help you?",
#     "Sure, I'd like to book a flight to Iceland.",
#     "Your flight has been booked."
# ])

# Get a response to the input text 'I would like to book a flight.'
while True:
    try:
        q = input("question:")
        if len(q) == 0:
            break
        bot_input = chatbot.get_response(q)
        print(bot_input)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
    #response = chatbot.get_response('I would like to book a flight.')

