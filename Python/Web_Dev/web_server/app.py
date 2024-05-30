from flask import Flask, render_template

app = Flask(__name__)


@app.route("/<username>/<int:my_num>")
def hello_world(username=None, my_num=None):
    return render_template('index.html', name=username, on_page_num=my_num)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/blog")
def blog():
    return "I made a new blog!"


@app.route("/blog/2020/dogs")
def blog2():
    return "I want a doggy!"
