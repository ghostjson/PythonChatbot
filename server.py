from flask import Flask
from flask import request
from chatbot.chatbot import ChatBot

app = Flask(__name__)

@app.route('/reply', methods= ['POST'])
def reply():

    if request.method == 'POST':
        data = request.form
        chatbot = ChatBot('Chatbot')

    return chatbot.respondInstant(data['message'])


def run():
    app.run()

if __name__ == '__main__':
    run()
