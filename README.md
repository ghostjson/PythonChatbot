## Python Commandline Chatbot
This chatbot is a wrapper around Chatterbot python library. In this chatbot, everything works in commandline so this chatbot is best work with other program in different languages. 
[**ChatterBot**](https://github.com/gunthercox/ChatterBot) is a machine-learning based conversational dialog engine build in Python which makes it possible to generate responses based on collections of known conversations. The language independent design of ChatterBot allows it to be trained to speak any language.

## Requirements:
All required dependencies are listed in requirements.txt.  
If you are using pip, then use 
``pip install -r requirements.txt``

## Quick Test:  
Run this command to get quick response  
``python main.py reply_instant "Hello"``

Here **reply_instant** is command and **"Hello"** is the message

## How To Use
1. Install the required dependencies
2. Create a json array with required ID inside convos folder (For Example: convos/1.json)
3. Enter message inside 1.json like ``["hello"]``
4. run ``python main.py reply 1``
5. You can get the response inside 1_reply.json `"hello there!"`

## Basic Usage
``python main.py command ID/message``

### Available commands:
1. reply  
``python main.py reply 1``  
Here **1** is the id of the file.

2. reply_respond  
``python main.py reply_respond "Hello"``  
Here **"Hello"** is the messsage.
3. train  
``python main.py train``  
Here json array from **convos/train.json** file is taken as the training data.

4. end  
``python main.py end 1``  
Here **1** is the id of the file.


## License
This program is licensed under the [BSD 3-clause license](https://opensource.org/licenses/BSD-3-Clause)
