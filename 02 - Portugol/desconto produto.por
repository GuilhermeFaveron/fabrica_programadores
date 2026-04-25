programa {
  funcao inicio() {
    real valor_produto, percentual_desconto, valor_desconto
    // valor do produto = R$ 200
    //percentual de desconto = 10%
    //valor do desconto = R$ 20,00
    escreva ("Escreva o valor do produto: ")
    leia (valor_produto)
    escreva ("Quanto de desconto tem a vista?: ")
    leia (percentual_desconto)
    
    valor_desconto = valor_produto * (percentual_desconto / 100)
    
  }
}
