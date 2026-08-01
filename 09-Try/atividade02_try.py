#autor: Guilherme Faveron de Macedo
#Projeto: Entendendo o tratamento de exceção

num1 = ValueError((input('Digite o primeiro número:')))
num2 = ValueError((input('Digite o segundo número:')))

try:
    soma = num1 + num2
    print(f'A soma dos numeros é: {soma}')
except:
    print('Ocorreu um erro durante a operação')