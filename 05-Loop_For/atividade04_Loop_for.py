#Autor: Guilherme Faveron de Macedo
#Projeto: Loop For - Variáveis de inicio e fim

numero = int(input('Digite a tabuada que deseja (exemplo: 4 ):'))
numero_inicio = int(input('Digite o inicio da tabuada:'))
numero_fim = int(input('Digite o fim da tabuada: '))

for i in range (numero_inicio, numero_fim + 1):
    print(f'{numero} x {i} = {i * numero}')