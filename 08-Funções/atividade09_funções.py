#autor: Guilherme Faveron de Macedo
#Projeto: Desvio Condicional

nome = input('Digite seu nome: ')
salario = float(input('Digite seu renda mensal: '))

def status (salario):
    if salario >=1000:
        print('Você possui uma boa renda')
    elif salario >=700:
        print ('Você possui uma renda razoável')
    elif salario >=500:
        print('Você possui uma renda baixa')
    else:
         print('Você possui uma renda muito baixa')

status(salario)