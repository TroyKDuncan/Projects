import requests


def send_ntfy():
    requests.post("https://ntfy.sh/tkd_portfolio_form_submission",
                  data="Someone just submittd a form to your portfolio site!".encode(encoding='utf-8'))
