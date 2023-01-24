from flask import Flask
import random

app = Flask(__name__)

jokes = [
    "Joke 1:1",
    "joke 2:2",
    "joke 3:3",
    "joke 4:4"

]

@app.get("/")
def hello_world():
    joke = random.choice(jokes)
    return f"<p>{joke}<p>"
