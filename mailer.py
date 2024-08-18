import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
import sys

recipient_email = sys.argv[1]
subject = sys.argv[2]
message = sys.argv[3]


html  = Template(Path("index.html").read_text())
email = EmailMessage()
email['from'] = 'your_name'
email['to'] = recipient_email
email['subject'] = subject

email.set_content(html.substitute({'Message': message}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('mohsinwani00@gmail.com', 'npewfrxeebaxveap')
    #smtp.login (your_email,password/app password)
    smtp.send_message(email)
    print('all good boss!')


