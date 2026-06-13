#Autor: Guilherme Faveron de Macedo
#Projeto: Listas em Python

nomes = ['Guilherme', 'Eloha', 'Junior', 'Ronaldo']
print (*nomes)

#adicionando um nome na lista
nomes.append('José')
print(*nomes)

#removendo um nome da lista
del nomes [3]
print(*nomes)

removido = nomes.pop(3)
print(f'Após o pop foi removido o nome: {removido}', nomes)