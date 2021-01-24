import sys
from chatbot.chatbot import ChatBot
from trainer.train import TrainChatBot

input_command = sys.argv[1]
input_attribute = sys.argv[2]

def run(command, attribute):
    chatbot = ChatBot('Chatbot')

    if command == 'reply':
        chatbot.respond(attribute)

    elif command == 'train':
        trainer = TrainChatBot(chatbot)
        trainer.train()

    elif command == 'end':
        ChatBot.endChat(attribute)

run(input_command, input_attribute)
