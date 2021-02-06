from chatterbot import ChatBot as ChatterBot
import json
import os

#Chatbot class inherited from ChatterBot class
class ChatBot(ChatterBot):

    def __init__(self, name):
        super(ChatBot, self).__init__(name)

    def respond(self, user_id):
        with open('convos/' + str(user_id) + '.json') as convos:
            data = json.load(convos)

        reply = self.get_response(data).text

        with open('convos/'+str(user_id)+'_reply.json', 'w') as convos_reply:
            json.dump(reply, convos_reply)

    def respondInstant(self, message):
            return self.get_response(message).text

    @staticmethod
    def endChat(user_id):
        file = 'convos/' + str(user_id) + '.json'
        reply_file = 'convos/'+str(user_id)+'_reply.json'

        try:
            os.remove(file)
            os.remove(reply_file)
        except OSError as e:
            pass

