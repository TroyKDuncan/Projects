import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


# Template object can replace things with $ in front of them
html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'TroyBoi'
email['to'] = 'tkduncan614@gmail.com'
email['subject'] = 'You won $1,000,000!!!'

email.set_content(html.substitute({'name': 'WinWin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # say hello to server
    smtp.starttls()  # encryption
    smtp.login('itmehi18@gmail.com', 'pvou gbsf kdhu yyjr')
    smtp.send_message(email)
    print('Job\'s done!')
