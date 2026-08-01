#autor: Guilherme Faveron de Macedo
#Projeto: Entendendo o tratamento de exceção

try:
    dolar = 5.08
    real = float(input('Digite seu valor em reais:'))
    converasão = real / dolar
    print(f'A conversão é: {converasão:.2f}')

except:
    print('Ocorreu um erro durante a operação')