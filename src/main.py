import os

from flask import Flask, render_template, request, jsonify
from chatbot_model import bag_of_words, model, words, labels, data
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    result = model.predict([bag_of_words(userText, words)])
    results_index = np.argmax(results)
    tag = labels[results_index]

    for tg in data["intents"]:
        if tg['tag'] == tag:
            responses = tg['responses']

    return jsonify(random.choice(responses))


# def main():
#     app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    app.run()
    home()
