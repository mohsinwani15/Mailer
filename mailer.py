import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

def mailer (email, name, subject):
    html  = Template(Path("index.html").read_text())
    email = EmailMessage()
    email['from'] = #youremail
    email['to'] = email
    email['subject'] = subject

    email.set_content(html.substitute({'name': name}), 'html')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login( # your_email,password/ app password)
        smtp.send_message(email)
        print('all good boss!')