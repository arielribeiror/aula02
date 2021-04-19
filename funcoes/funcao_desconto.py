def desconto(valor_produto):
  resultado = valor_produto * .95
  return resultado  
  
valor = float(input("Digite o valor do produto"))
descontado = desconto(valor)
print("O valor original era R${} e agora é R${}".format(valor, descontado))
  