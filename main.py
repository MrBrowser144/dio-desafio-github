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
            [sg.Text('Corpo', size=(5, 0)), sg.Multiline(size=(35, 15), key='corpo')],
            [sg.Button('Enviar Email')],
            #[sg.Output(size=(30, 5), key='output')]
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
            login = self.values['login']
            senha = self.values['senha']
            email = self.values['para']
            print(login)
            print(senha)
            print(email)

            #Email
            host = 'smtp.gmail.com'
            port = '587'

            server = smtplib.SMTP(host, port)
            server.ehlo()
            server.starttls()
            server.login(login, senha)

            corpo = self.values['corpo']
            email_msg = MIMEMultipart()
            email_msg['From'] = login
            email_msg['To'] = email
            email_msg['Subject'] = "CV Lucas da Silva Bispo"
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
            #self.janela.FindElement('output').Update('')




tela = telapython()
tela.iniciar()
