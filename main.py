from flask import Flask, request, jsonify
import random
import numpy as np
import markdown.extensions.fenced_code
import tools.sql_queries as sqll
from IPython.display import Image

#from nltk.sentiment.vader import SentimentIntensityAnalyzer
#nltk.downloader.download('vader_lexicon')
#sia = SentimentIntensityAnalyzer()

app = Flask(__name__)

# Render the markdwon
@app.route("/")
def readme ():
    readme_file = open("README.md", "r")
    return markdown.markdown(readme_file.read(), extensions = ["fenced_code"])

# GET ENDPOINTS: SQL 
# SQL get everything
@app.route("/entities/")
def ents ():
    return jsonify(sqll.get_entities())

@app.route("/sql/")
def sql ():
    return jsonify(sqll.get_all())


@app.route("/sql/<name>")
def get_messages_person (name):
    return jsonify(sqll.get_everything_from_person(name))

@app.route("/frequency/")
def freq ():
    return jsonify(sqll.get_freq())

@app.route("/sentiment/")
def sentiment ():
    return jsonify(sqll.get_Sentiment())

####### POST
@app.route("/insertrow", methods=["POST"])
def try_post ():
    # Decoding params
    my_params = request.args
    print(my_params)
    Name = my_params["Name"]
    Message = my_params["Message"]
    # Passing to my function: do the insert
    sqll.insert_one_row(Name,Message)
    return f"Query succesfully inserted"

if __name__ == "__main__":
    app.run(port=9000, debug=True)

