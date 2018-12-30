from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os


bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)


for file in os.listdir('E:/Github/ChatBot/data/'):
        Data = open(r'E:/Github/ChatBot/data/' + file,encoding='latin-1').readlines()
        bot.train(Data)


while True:

        message = input('You:')
        if message.strip()!= 'Bye':
        
            reply = bot.get_response(message)                        
            print('ChatBot :',reply)
        if message.strip() == 'Bye':
            print('Chatbot : Bye')
            break
    

