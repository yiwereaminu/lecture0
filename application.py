from flask import flask

app = Flask(__name__)
@app.route("/")
def index():
    return "hello world"

@app.route("/amin")
def amin():
    return "Hello, Amin"

@app.route("/yiwere")
def yiwere():
    return "Hello, Yiwere"

//dynamic route
@app.route("/<string:name>")
def dynamic(name):
    return f"Hello, {name}"
