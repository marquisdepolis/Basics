from flask import Flask, render_template, request, jsonify
from callgpt import Chatbot

app = Flask(__name__)
chatbot = Chatbot()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/message', methods=['POST'])
def handle_message():
    user_message = request.form['user_message']
    chatbot_response = chatbot.route_user_message(user_message)
    print("Chatbot response:", chatbot_response)  # Add this line
    return jsonify({'response': chatbot_response})


if __name__ == '__main__':
    app.run(debug=True)
