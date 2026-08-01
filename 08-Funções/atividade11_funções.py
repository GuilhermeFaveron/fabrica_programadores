#Autor: Guilherme Faveron de Macedo
#Projeto: Função com juros composto


emprestimo = int(input('Digite o valor do Empréstimo:'))
juros = float(input('Digite a porcentagem do Juros composto:'))
meses = int(input('Digite em quantas vezes você quer parcelar:'))
porcentagem = int(input('Digite quantos porcento você pode pagar a mais do que o valor do empréstimo:'))

def desafiar (emprestimo,juros,meses):
    valor1 = emprestimo * (juros / 100) * meses