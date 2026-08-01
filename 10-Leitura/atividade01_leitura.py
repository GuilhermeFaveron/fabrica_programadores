#autor: Guilherme Faveron de Macedo
#Projeto: Trabalhando com arquivos

nome = input('Digite seu nome: ')
email = input('Digite seu e-mail: ')
telefone = input('Digite seu numero de telefone:')

arquivo = open("pessoa.txt", 'a')
arquivo.write(nome + "|" + email + '|' + telefone + "\n")
arquivo.close()