from flask import Flask

app = Flask(__name__)

all_messages = []





def add_message(sender, text):
    new_message = {
        'sender': sender,
        'text': text,
        'time': '21:16',
    }
    all_messages.append(new_message)


@app.route('/')
def index_page():
    return {'messages': all_messages}

app.run()
