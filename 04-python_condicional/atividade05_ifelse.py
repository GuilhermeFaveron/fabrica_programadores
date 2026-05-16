#autor: Guilherme Faveron
#Projeto: Desvio Condicional

#Criação das variaveis
nome = input('Digite seu nome: ')
idade = input('Digite sua idade:')
cnh = input(('Tem carteira de motorista? (Sim ou Nao): ')) 
if cnh == 'Sim' and idade >=18:
     print('Pode dirigir')
else:
     print('Não pode dirigir')