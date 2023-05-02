from flask import Flask, render_template, request
import json

app = Flask(__name__)

def load_conversations():
    with open('conversations.json') as file:
        conversations = json.load(file)
    return conversations

conversations = load_conversations()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    message = request.form['message']
    response = generate_response(message)
    return response

def generate_response(message):
    for conversation in conversations:
        if message.lower() == conversation['message']:
            return f"{conversation['response']}"
    return "I'm sorry, I don't understand that."

if __name__ == '__main__':
    app.run()
