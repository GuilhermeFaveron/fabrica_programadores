#autor: Guilherme Faveron
#Projeto: Desvio Condicional

#Criação das variaveis
nome = input('Digite seu nome: ')
nota1 = float(input('Digite a primeira nota do aluno: ')) 
nota2 = float(input('Digite a segunda nota do aluno: ')) 
nota3 = float(input('Digite a terceira nota do aluno: ')) 
resultado = nota1 + nota2 + nota3 / 3
if resultado >=7:
     print('Aluno Aprovado')
elif nota >=4:
    print('Aluno em recuperação')
else:
    print('Aluno Reprovado!:')