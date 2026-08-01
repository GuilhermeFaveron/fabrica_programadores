#Autor: Guilherme Faveron de Macedo
#Projeto: Função IMC

nome = input('Digite seu nome: ')
peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))

def calcular(peso, altura):
    imc= peso /  (altura * altura)
    print(f'O resultado seu Imc é: {imc:.2f}')

calcular(peso,altura)