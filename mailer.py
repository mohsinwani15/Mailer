import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
import sys

recipient_email = sys.argv[1]
recipient_name = sys.argv[2]
subject = sys.argv[3]


html  = Template(Path("index.html").read_text())
email = EmailMessage()
email['from'] = 'your_name'
email['to'] = recipient_email
email['subject'] = subject

email.set_content(html.substitute({'name': recipient_name}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login #(  your_email,password/app password)
    smtp.send_message(email)
    print('all good boss!')

