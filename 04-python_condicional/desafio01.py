#autor: Guilherme Faveron
#Projeto: Desvio Condicional

#Criação das variaveis
nome = input("Digite seu nome: ")
pedido = input("digite seu pedido (1 Café ; 2 Chá ou 3 Irei pedir depois): ")
if pedido =="1":
    print(nome, 'Você pediu Café')
elif pedido =="2":
    print('Você pediu Chá')
else:
    print('Estarei aguardando seu pedido')