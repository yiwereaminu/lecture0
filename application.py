from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("layout.html")

#@app.route("/bye")
#def bye():
#    headline = "Good bye!"
#    return render_template("index.html", headline=headline)

#@app.route("/callUsNow")
#def callUsNow():
#    callUsNow = "0558263462"
#    return render_template("index.html", callUsNow=callUsNow)

@app.route("/hello", methods = ["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)
