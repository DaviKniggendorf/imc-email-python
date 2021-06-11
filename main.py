from os import system
from funcao_imc import classifica_imc
from estilo_imc import exibe_titulo, exibe_asterisco #Isso importa as funções especificadas
from funcao_email import enviar_email


system('cls') # Isso serve para limpar a tela do meu terminal
exibe_titulo()

# Aqui pego os dados do usuário
"""
nome = input('Digite o seu nome e aperte enter: ')
idade = int(input('Digite sua idade e aperte enter: '))
sexo = int(input("Qual é seu gênero (1)FEMININO (2)MASCULINO (3)OUTRO: "))
email = input('Digite seu email e aperte enter: ') 
peso = float(input('Digite o seu peso em quilos e aperte enter: '))
altura = float(input('Digite a sua altura em metros e aperte enter: '))
"""
nome = 'Davi'
idade = 16
sexo = 2
email = 'freefirefrefas07@gmail.com'
peso = 65
altura = 1.75

if sexo == 1:
	sexo = 'Feminino'
elif sexo == 2:
	sexo = 'Masculino'
else:
	sexo = 'Outro'

imc = classifica_imc(peso, altura)

conteudo = f"""
	
	<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
	</head>
	<body>

		<h1 style="color: #FF8C64;">Olá {nome}, tudo bem?</h1>
		<h3 style="text-align:left;font-size:12pt;">Verificamos e calculamos seu imc a partir das informações 
		fornecidas no formulário:</h3>

		<ul style="list-style:none;font-size:12pt;margin:0;padding:0;">
			<li>Nome: {nome}</li>
			<li>Idade: {idade}</li>
			<li>Sexo: {sexo}</li>
			<li>Peso: {peso}</li>
			<li>Altura: {altura}</li>
		</ul>

		<h3>De acordo com os resultados você está com o <span style="color: #FF8C64;">{imc[1]}</span>, seu imc é <span style="color: #FF8C64;">{imc[0]}<span>.</h3>

	</body>
</html>


"""

system('cls')

exibe_titulo()

#Aqui exibe as informações para o email do usuário

enviar_email(email, conteudo)

print(f'Os resultados do seu imc foi enviado para o email {email}')