import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# https://www.abstractapi.com/guides/sending-email-with-python

gmail_user = 'diver.vlz@gmail.com'
gmail_password = '5z7AQd!Z#m'

sent_from = gmail_user
sent_to = ['diver.vlz@gmail.com']
subject = 'Test message'
body = 'Test message body'

message = MIMEMultipart()
message['From'] = sent_from
message['To'] = sent_to
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(gmail_user, gmail_password)

text = message.as_string()

session.sendmail(sent_from, sent_to, text)
session.quit()

print('Done!')
