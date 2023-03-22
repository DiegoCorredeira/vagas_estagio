import smtplib
from email.mime.multipart import MIMEMultipart
import email.mime.application
from email.mime.text import MIMEText
import pandas as pd
from dotenv import load_dotenv
import os

config = load_dotenv(".env")
EMAIL_PRINCIPAL = os.getenv('EMAIL')
EMAIL_CONVIDADO = os.getenv('EMAIL_CONVIDADO')
APP_SENHA = os.getenv('APP_SENHA')

mensagem = MIMEMultipart()
mensagem['Subject'] = 'Sua atualização diária de vagas de estágio chegou!'
mensagem['From'] = EMAIL_PRINCIPAL
mensagem['To'] = EMAIL_CONVIDADO
conteudo = 'Segue as vagas capturadas!'
mensagem.attach(MIMEText(conteudo))

vagas = 'vagas.xlsx'
fp=open(vagas, 'rb')
anexando = email.mime.application.MIMEApplication(fp.read(), _subtype='xlsx')
fp.close()
anexando.add_header('Content-Disposition', 'attachment', filename=vagas)
mensagem.attach(anexando)

servidor = smtplib.SMTP('smtp.gmail.com', port=587)
servidor.starttls()
servidor.login(EMAIL_PRINCIPAL, APP_SENHA)
servidor.sendmail(mensagem['From'], mensagem['To'], mensagem.as_string())
print('E-mail enviado com sucesso!')
servidor.quit()
