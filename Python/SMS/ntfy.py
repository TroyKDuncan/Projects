import requests

requests.post("https://ntfy.sh/test_tkd",
    data="This is literally the easiest thing to use in the whole world!".encode(encoding='utf-8'),
    headers={
        "Title": "Unauthorized access detected",
        "Priority": "urgent",
        "Tags": "warning",
        # "Delay": "0m",
        "Click": "mailto: troyduncanbusiness@gmail.com"
              })
