from funcao_imc import classifica_imc

def exibe_titulo():
    print(f'''{exibe_asterisco()}
* Calculadora IMC *
{exibe_asterisco()}
''')
 
def exibe_asterisco(valor=19):
    asterisco = valor * '*'
    return asterisco