import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pack import getpass_ak, pw
from time import sleep


def send(mail):
    print(" ")
    email_user = input(str("Enter sender gmail: "))
    email_password = pw.pw() # getpass_ak.getpass("Enter your password: ")
    email_send = mail #input(str("Enter destination email: "))
    subject = 'Custom list'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body =  "Here's your list!"
    msg.attach(MIMEText(body, 'plain'))

    filename = 'info.txt'
    attachment = open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, email_password)

    server.sendmail(email_user, email_send, text)
    server.quit()
    print("Operation successful!")
    sleep(2)
