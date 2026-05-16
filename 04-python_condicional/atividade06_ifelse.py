#autor: Guilherme Faveron
#Projeto: Desvio Condicional

#Criação das variaveis
nome = input('Digite seu nome: ')
nota = float(input('Digite a nota do aluno: ')) 
if nota >=7:
     print('Aluno Aprovado')
elif nota >=5:
    print('Aluno em recuperação')
else:
    print('Aluno Reprovado!:')