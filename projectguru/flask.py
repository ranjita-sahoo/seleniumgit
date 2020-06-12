from flask import Flask
projectguru = Flask(__name__)

@projectguru.route("/")
def hello():
    return "Hello World!"


