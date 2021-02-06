import sys
from chatbot.chatbot import ChatBot
from trainer.train import TrainChatBot

#first parameter
input_command = sys.argv[1]

#second parameter (default = -1)
try:
    input_attribute = sys.argv[2]
except IndexError:
    input_attribute = -1

def run(command, attribute):
    chatbot = ChatBot('Chatbot')

    if command == 'reply':
        chatbot.respond(attribute)

    elif command == 'reply_instant':
        response = chatbot.respondInstant(attribute)
        print(response)

    elif command == 'train':
        trainer = TrainChatBot(chatbot)
        trainer.train()

    elif command == 'end':
        ChatBot.endChat(attribute)

    elif command == 'serve':
        server.run()

    else:
        print("Invalid Command")
        print("Available Commands are [reply, reply_instant, train, end]")


#run function
run(input_command, input_attribute)
