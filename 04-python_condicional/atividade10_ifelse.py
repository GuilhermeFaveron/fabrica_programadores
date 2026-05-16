#autor: Guilherme Faveron
#Projeto: Desvio Condicional

#variáveis
nome = input('Digite seu nome: ')
peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
resultado = peso / (altura * altura)
if resultado <=18.5:
    print('Você precisa dar uma engoradinha')
else:
    print('Seu peso está normal')