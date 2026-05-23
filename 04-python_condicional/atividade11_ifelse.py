#autor: Guilherme Faveron de Macedo
#Projeto: Desvio Condicional

#Criação das variaveis
temperatura = float(input('Digite a temperatura em graus Celsius:'))

if temperatura >=40:
    print('Hoje está muito quente!')
elif temperatura >=30:
    print('Hoje está quente!')
elif temperatura >=20:
    print('Hoje está agradavél')
elif temperatura >=10:
    print('Hoje esta frio')
else:
    print('Hoje está muito frio!')