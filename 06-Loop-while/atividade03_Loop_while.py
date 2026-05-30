#Autor: Guilherme Faveron de Macedo
#Projeto: Loop While

numero = int(input('Digite a tabuada que deseja:'))
numero_inicio = int(input('Digite o inicio da tabuada:'))
numero_fim = int(input('Digite o fim da tabuada: '))

while numero_inicio <= numero_fim:
    print(f'{numero} x {numero_inicio} = {numero * numero_inicio}')
    numero_inicio = numero_inicio + 1