#Autor: Guilherme Faveron de Macedo
#Projeto: Listas em Python

nomes = ['Pelé', 'Messi', 'Ronaldinho', 'Ronaldo']
print (*nomes)

#adicionando um nome na lista
nomes.append('Pedro')
print(*nomes)

#adicionando um nome em uma posição específica
nomes.insert(4,'Neymar Jr.')
print(*nomes)

#Modificar uma pessoa da lista
nomes [5] = 'Mbappe'
print(*nomes)

#removendo um nome da lista
del nomes [1]
print(*nomes)

#Removendo um nome
#Buscar o nome e apagar o primeiro que aparecer
nomes.remove('Ronaldo')
print(*nomes)

#Usando o poo para mostrar o nome removido
#  0      1          2         3
#Pelé Ronaldinho Neymar Jr. Mbappe
removido = nomes.pop(1)
print(f'Após o pop foi removido o nome: {removido}', nomes)