from flask import Flask, request, jsonify
from chatbot import generate_response  # Make sure this module exists and is correct

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = generate_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(port=5000, debug=True)


