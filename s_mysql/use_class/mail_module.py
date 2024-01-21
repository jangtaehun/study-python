import smtplib
import ssl
# import requests
# import certifi

#ln -s /etc/ssl/* /Library/Frameworks/Python.framework/Versions/3.10/etc/openssl


# response = requests.get('https://google.com', verify=certifi.where())
# ssl._create_default_https_context = ssl._create_unverified_context
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(receiver, message):
    port = 587

    smtp_server = 'smtp.gmail.com'
    sender_email = 'jangth0056@gmail.com'
    receiver_email = receiver
    password = 'ncuk tjrs uydm idzi'
    message = message


    msg = MIMEText(message, 'html')
    data = MIMEMultipart()
    data.attach(msg)

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, data.as_string())