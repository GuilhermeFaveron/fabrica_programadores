#Autor: Guilherme Faveron de Macedo
#Projeto: Tabuada com Loop For

numero = int(input('Digite a tabuada que deseja (exemplo: 4 ):'))

for i in range (1,11):
    print(f'{numero} x {i} = {i * numero}')