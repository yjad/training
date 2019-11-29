from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

def y():
    bot = ChatBot('MyChatBot')
    bot.set_trainer(ListTrainer)

    conversation = open('chats.txt', 'r').readlines()

    bot.train(conversation)

    while True:
        message = input('You:')
        if message.strip() != 'Bye':
            reply = bot.get_response(message)
        print('ChatBot:', reply)
        if message.strip() == 'Bye':
            print('ChatBot:Bye')
            break

def x():
    chatbot = ChatBot("Ron Obvious")
    trainer = ListTrainer(chatbot)

    for _file in os.listdir('chats'):
        conversation = open('chats\\' + _file, 'r').readlines()
        trainer.train(conversation)

    while True:
        message = input('You:')
        if message.strip() != 'Bye':
            reply = chatbot.get_response(message)
        print('ChatBot:', reply)
        if message.strip() == 'Bye':
            print('ChatBot:Bye')
            break

x()
