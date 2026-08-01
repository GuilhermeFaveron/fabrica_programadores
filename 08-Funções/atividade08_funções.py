#autor: Guilherme Faveron de Macedo
#Projeto: Desvio Condicional

#Criação das variaveis
nome = input('Digite seu nome: ')
nota = float(input('Digite a nota final: ')) 

def status (nota):
    if nota >=6:
        print('Aluno Aprovado')
    else:
        print('Aluno Reprovado')

status(nota)