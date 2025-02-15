from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

file = open("english.txt", "r")
words = []
words = file.readlines()
file.close()
words.append('A\n')
words.append('I\n')

@app.route("/spell_check", methods=['POST'])
def check_spelling():
    data = request.get_json()
    message = data.get("message")
    tokens = message.split()
    misspelled = []
    for token in tokens:
        if token.upper() + '\n' not in words:
            misspelled.append(token)
    return jsonify({"incorrect":misspelled})