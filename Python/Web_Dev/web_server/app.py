from flask import Flask, render_template, request, redirect
import csv
import requests


app = Flask(__name__)


def send_ntfy():
    requests.post("https://ntfy.sh/tkd_portfolio_form_submission",
                  data="Someone just submittd a form to your portfolio site!".encode(encoding='utf-8'))


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        send_ntfy()
        csv_writer = csv.writer(
            db, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


def write_to_txt(data):
    with open('database.txt', mode='a') as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        db.write(f'\n{email},{subject},{message}')


@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong, try again'
