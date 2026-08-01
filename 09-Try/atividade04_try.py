#autor: Guilherme Faveron de Macedo
#Projeto: Entendendo o tratamento de exceção

try:
    nome = input('Digite seu nome: ')
    peso = float(input('Digite seu peso em kg: '))
    altura = float(input('Digite sua altura em metros: '))
    resultado = peso / (altura * altura)

    print(f'O seu imc é: {resultado:.2f}')

except:
    print('Ocorreu um erro durante a operação')