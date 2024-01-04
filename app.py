from flask import Flask, render_template, url_for, request
from transformers import pipeline
# classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api", methods = ['GET'])
def returnAngry():
    dict = {}
    inputSentence = str(request.args['sentence'])
    answer = str("angry")
    dict['output'] = answer
    return answer

# @app.route("/hug",methods=["GET"])
# def returnSentiment():
#     try:
#         dict = {}
#         inputSentence = str(request.args['sentence'])
#         answer =  classifier(inputSentence)
#         dict['output'] = answer[0]
#         return answer
#     except Exception as e:
#         return e


if __name__ == "__main__":
    app.run(host="0.0.0.0")

