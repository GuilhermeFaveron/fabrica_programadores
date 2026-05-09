#autor: Guilherme Faveron
#Projeto: Entradas com f-string

#variaveis
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor:'))
resultado1 = valor1 + valor2
resultado2 = valor1 - valor2
resultado3 = valor1 * valor2
resultado4 = valor1 / valor2
resultado5 = valor1 // valor2
resultado6 = valor1 % valor2
resultado7 = valor1 ** valor2

#exibindo os resultados
print(f'O resultado da soma é: {resultado1}')
print(f'O resultado da subtração é: {resultado2}')
print(f'O resultado da multiplicação é: {resultado3}')
print(f'O resultado da divisão é: {resultado4}')
print(f'O resultado da divisão inteira é: {resultado5}')
print(f'O resultado do módulo é: {resultado6}')
print(f'O resultado da potência é: {resultado7}')