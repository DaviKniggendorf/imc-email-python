import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from funcao_imc import classifica_imc

def enviar_email(destino, conteudo):
	# Configuração
	host = 'smtp.gmail.com'
	port = 587
	user = 'email de origem'
	password = open('dados/senha.txt', encoding='UTF-8').read().strip()

	# Criando objeto
	print('Criando objeto servidor...')
	server = smtplib.SMTP(host, port)

	# Login com servidor
	print('Login...')
	server.ehlo()
	server.starttls()
	server.login(user, password)

	# Criando mensagem
	message = conteudo

	print('Criando mensagem...')
	email_msg = MIMEMultipart()
	email_msg['From'] = user
	email_msg['To'] = destino
	email_msg['Subject'] = 'Resultado do seu IMC'
	print('Adicionando texto...')
	email_msg.attach(MIMEText(message, 'html'))

	# Enviando mensagem
	print('Enviando mensagem...')
	server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
	print('Mensagem enviada!')
	server.quit()
