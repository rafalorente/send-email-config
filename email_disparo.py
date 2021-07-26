import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def disparo_email(user, password, destinatario):
    # Configuração
    host = 'smtp.gmail.com'
    port = 587

    # Criando objeto
    print('Criando objeto servidor...')
    server = smtplib.SMTP(host, port)

    # Login com servidor
    print('Login...')
    server.ehlo()
    server.starttls()
    server.login(user, password)

    # Criando mensagem
    message = 'Mensagem que deverá ser enviada'
    print('Criando mensagem...')
    email_msg = MIMEMultipart()
    email_msg['From'] = user
    email_msg['To'] = destinatario
    email_msg['Subject'] = 'E-mail python'
    print('Adicionando texto...')
    email_msg.attach(MIMEText(message, 'plain'))

    # Enviando mensagem
    print('Enviando mensagem...')
    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
    print('Mensagem enviada!')
    server.quit()
    print('Quit')
