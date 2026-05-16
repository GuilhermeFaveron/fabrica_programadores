#autor: Guilherme Faveron
#Projeto: Desvio Condicional

#Criação das variaveis
nome = input('Digite seu nome: ')
salario = float(input('Digite o seu salário: ')) 
resultado = salario * 0.10
if resultado >100:
    print('Você é rico em')
else:
     print('Você é pobre')