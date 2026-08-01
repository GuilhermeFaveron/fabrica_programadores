#autor: Guilherme Faveron de Macedo
#Projeto: Entendendo o tratamento de exceção

try:
    celsius = float(input('Digite a temperatura:'))
    fahrenheit = (celsius * (9/5))+32
    print(f'A conversão é: {fahrenheit:.2f}°F')
except:
    print('Ocorreu um erro durante a operação')