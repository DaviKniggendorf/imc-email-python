from os import system
from funcao_imc import classifica_imc
from estilo_imc import exibe_titulo, exibe_asterisco #Isso importa as funções especificadas
from preencher_usuario import dados_usuario
from funcao_email import enviar_email

system('cls') # Isso serve para limpar a tela do meu terminal
exibe_titulo()

#Coleta dados do usuário
dados = dados_usuario()
nome = dados[0]
idade = dados[1]
sexo = dados[2]
email = dados[3]
peso = dados[4]
altura = dados[5]

#calcula o imc e classifica 
imc = classifica_imc(peso, altura)

#Mensagem que será enviada para o usuário
conteudo = f"""
	
		<!DOCTYPE html>
		<html>
			<head>
				<meta charset="utf-8">
			</head>
			<body>

				<h1 style="color: #FF8C64;">Olá {nome}, tudo bem?</h1>
				<h3 style="text-align:left;font-size:12pt;">Verificamos e 
				calculamos seu imc a partir das informações 
				fornecidas no formulário:</h3>

				<ul style="list-style:none;font-size:13pt;margin:0;padding:0;">
					<li>Nome: {nome}</li>
					<li>Idade: {idade} Anos</li>
					<li>Sexo: {sexo}</li>
					<li>Peso: {peso} Kg</li>
					<li>Altura: {altura} cm</li>
				</ul>

				<h3>De acordo com os resultados você está com o <span style="color: #FF8C64;">{imc[1]}
				</span>, seu imc é <span style="color: #FF8C64;">{imc[0]}<span>.</h3>

			</body>
		</html>
			"""

system('cls')

exibe_titulo()

#Aqui exibe as informações para o email do usuário
enviar_email(email, conteudo)

print(f'Os resultados do seu imc foi enviado para o email {email}')