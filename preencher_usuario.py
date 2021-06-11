# Recolhe os dados do usuário

def dados_usuario():
	nome = input('Digite o seu nome e aperte enter: ').title().strip()
	idade = int(input('Digite sua idade e aperte enter: '))
	sexo = int(input("Qual é seu gênero (1)FEMININO (2)MASCULINO (3)OUTRO: "))
	email = input('Digite seu email e aperte enter: ').strip()
	peso = float(input('Digite o seu peso em quilos e aperte enter: '))
	altura = float(input('Digite a sua altura em metros e aperte enter: '))

	if sexo == 1:
		sexo = 'Feminino'
	elif sexo == 2:
		sexo = 'Masculino'
	else:
		sexo = 'Outro'

	return nome, idade, sexo, email, peso, altura
