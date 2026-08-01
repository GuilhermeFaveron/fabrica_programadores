#autor: Guilherme Faveron de Macedo
#Projeto: Entendendo o tratamento de exceção

try:
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor:'))
    resultado1 = valor1 + valor2
    resultado2 = valor1 - valor2
    resultado3 = valor1 * valor2
    resultado4 = valor1 / valor2
    
    print(f'O resultado da soma é: {resultado1}')
    print(f'O resultado da subtração é: {resultado2}')
    print(f'O resultado da subtração é: {resultado2}')
    print(f'O resultado da multiplicação é: {resultado3}')
    print(f'O resultado da divisão é: {resultado4}')

except:
    print('Ocorreu um erro durante a operação')