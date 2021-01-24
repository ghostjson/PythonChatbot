from chatterbot.trainers import ListTrainer

import json

#TrainChatBot class which train data from convos/train.json file.
#File should be a json array.
class TrainChatBot:

    def __init__(self, chatbot):
        self.chatbot = chatbot

    def train(self):
        trainer = ListTrainer(self.chatbot)

        with open('convos/train.json') as train:
            data = json.load(train)
            trainer.train(data)
