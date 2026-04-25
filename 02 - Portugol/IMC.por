programa {
  funcao inicio() {
    real peso, altura, imc
    real divisao
    real multiplicacao
    cadeia nome
    escreva("Digite seu nome: ")
    leia (nome)
    escreva ("Digite o peso: ")
    leia (peso)
    escreva ("Digite sua altura: ")
    leia (altura)
    // não esquecer de colocar a multiplicação
    // entre parenteses (altura * altura)
    imc = peso / (altura * altura)
    escreva("---Bem vindo---", nome)
    escreva ("\n O resultado do seu imc é:", imc ) 

  
    

  }
}
