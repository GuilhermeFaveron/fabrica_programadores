#autor: Guilherme Faveron de Macedo
#Projeto: Desvio Condicional

#Criação das variaveis
nome = input('Digite seu nome: ')
peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
resultado = peso / (altura * altura)
if resultado <=18.5:
    print('Você está magro')
elif resultado <=24.9:
    print('Você está com o peso normal')
elif resultado <=29.9:
    print('Você está com sobre peso, se cuide!')
elif resultado <=39.9:
    print('Você está com obesidade, tome cuidado!')
else:
    print('Você está com obesidada grave, procure um médico!')