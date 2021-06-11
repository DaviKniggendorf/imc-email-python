'''
Parte responsavel pelas funções de calcular IMC e
Classificalos de acordo com o resultado do IMC.
'''

def classifica_imc(peso, altura):
    
    imc_calculado = round(peso / (altura * altura))

    if (imc_calculado < 18.5):
        classifcacao_imc = 'Peso baixo'
    elif (imc_calculado < 25):
        classifcacao_imc = 'Peso Normal'
    elif (imc_calculado < 30):
        classifcacao_imc = 'Sobrepeso'
    elif (imc_calculado < 35):
        classifcacao_imc = 'Obesidade (Grau I)'   
    elif (imc_calculado < 40):
        classifcacao_imc = 'Obesidade Severa (Grau II)'
    else:
        classifcacao_imc = 'Obesidade Mórbida (Grau III)'
        
    return imc_calculado, classifcacao_imc
