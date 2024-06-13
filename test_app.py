from flask import Flask, request
from random import randint
from time import sleep


app = Flask(__name__)


@app.route("/")
def index():
    return "OK"


@app.route("/about")
def about():
    return "OK"


@app.route("/random")
def rndm():
    sleep(randint(0, 2))
    return "OK"


@app.route("/item")
def items():
    item_id = request.args.get("id", None)
    return f"OK - {item_id}"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "OK_POST"
    else:
        return "OK_GET"


if __name__ == "__main__":
    app.run()
