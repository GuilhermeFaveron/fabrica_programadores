#autor: Guilherme Faveron
#Projeto: Desvio Condicional

#Criação das variaveis
nome = input('Digite seu nome: ')
telefone = float(input('Digite seu numero de telefone: '))
cidade = input('Informe onde você mora: ')
salario = float(input('Digite seu renda mensal: '))
if salario >=1000:
    print('Você possui uma boa renda')
elif salario >=700:
    print ('Você possui uma renda razoável')
elif salario >=500:
    print('Você possui uma renda baixa')
else:
    print('Você possui uma renda muito baixa')