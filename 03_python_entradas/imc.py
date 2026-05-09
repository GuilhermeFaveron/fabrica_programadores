#autor: Guilherme Faveron
#Projeto: Entradas do imc

#variáveis
nome = input('Digite seu nome: ')
peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
resultado = peso / (altura * altura)

#exibindo o resultado
print(f'O seu imc é: {resultado:.2f}')