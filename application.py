from flask import Flask

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


@app.route("/<string:name>")
def dynamic(name):
    return f"Hello, {name}"
