import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pack import getpass_ak, pw
from time import sleep


def send(mail):
    print(" ")
    # input(str("Ingrese su gmail para enviar datos: "))
    email_user = ""
    # getpass_ak.getpass("Ingrese su contraseña: ")
    email_password = pw.pw()
    #input(str("Ingrese el correo del destinatario: "))
    email_send = mail
    subject = 'Lista personalizada'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = '¡Esta es la lista de memes!'
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
    print("Operación completada con éxito!")
    sleep(2)
