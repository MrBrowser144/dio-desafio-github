import PySimpleGUI as sg
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class telapython:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Email', size=(5, 0)), sg.Input(size=(30, 0), key='login')],
            [sg.Text('Senha', size=(5, 0)), sg.Input(size=(30, 0), key='senha')],
            [sg.Text('Para', size=(5, 0)), sg.Input(size=(30, 0), key='para')],
            [sg.Text('Assunto', size=(5, 0)), sg.Input(size=(30, 0), key='assunto')],
            [sg.Text('Corpo', size=(5, 0)), sg.Multiline(size=(35, 15), key='corpo')],
            [sg.Button('Enviar Email')],
            [sg.Output(size=(30, 5), key='output')]
        ]
        # Janela
        self.janela = sg.Window("Email").layout(layout)
        # Extair dados da tela
        self.button, self.values = self.janela.Read()

    def iniciar(self):
        while True:
            # Extair dados da tela
            self.button, self.values = self.janela.Read()
            if self.values == sg.WIN_CLOSED:
                break

    def email(self):
            #Email
            login1 = self.values['login']
            senha1 = self.values['senha']
            email1 = self.values['para']
            login = f'{login1}'
            senha = f'{senha1}'
            email = f'{email1}'
            host = 'smtp.gmail.com'
            port = '587'
            print('Email enviado!')
            print(f'Email: {login1}')
            print(f'Para: {email1}')

            server = smtplib.SMTP(host, port)
            server.ehlo()
            server.starttls()
            server.login(login, senha)

            corpo = self.values['corpo']
            email_msg = MIMEMultipart()
            email_msg['From'] = login
            email_msg['To'] = email
            email_msg['Subject'] = self.values['para']
            email_msg.attach(MIMEText(corpo, 'plain'))

            arqui = 'C:\\Users\\Lucas\\Documents\\CV Lucas da Silva Bispo.pdf'
            attchment = open(arqui, 'rb')

            att = MIMEBase('application', 'octet-stream')
            att.set_payload(attchment.read())
            encoders.encode_base64(att)

            att.add_header('Content-Disposition', f'attachment; filename= CV Lucas da Silva Bispo.pdf')
            attchment.close()
            email_msg.attach(att)

            server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())

            server.quit()
            self.janela.FindElement('output').Update('')




tela = telapython()
tela.iniciar()
tela.email()
