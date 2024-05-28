from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/blog")
def blog():
    return "I made a new blog!"


@app.route("/blog/2020/dogs")
def blog2():
    return "I want a doggy!"
