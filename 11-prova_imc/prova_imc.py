#autor: Guilherme Faveron de Macedo
#Projeto: Prova IMC

#Criação das variaveis
nome = input('Digite seu nome: ')
peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
resultado = peso / (altura ** 2)

print(f'IMC: {resultado:.2f}')

if resultado <=18.5:
    print('Você está abaixo do peso ⚖️')
elif resultado <=24.9:
    print('Você está com o peso normal 💪')
elif resultado <=29.9:
    print('Você está com sobre peso 🍔')
elif resultado <=34.9:
    print('Você está com obesidade Grau I 🟠')
elif resultado <=39.9:
    print('Você está com obesidade Grau II 🔴')
else:
    print('Você está com obesidade Grau III 🚨 (mórbida)')
