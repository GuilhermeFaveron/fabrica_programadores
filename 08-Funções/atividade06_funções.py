#Autor: Guilherme Faveron de Macedo
#Projeto: Função calculadora

#entradas de dados
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))

#função calcular
def calcular (valor1,valor2):
    somar = valor1 + valor2
    subtrair = valor1-valor2
    multiplicar = valor1*valor2
    dividir = valor1/valor2 

    #imprimindo os resultados
    print(f'O resultado da soma é: {somar}')
    print(f'O resultado da Subtração é: {subtrair}')
    print(f'O resultado da Multiplicação é: {multiplicar}')
    print(f'O resultado da Divisão é: {dividir}')

# Chamada da função
calcular(valor1,valor2)
