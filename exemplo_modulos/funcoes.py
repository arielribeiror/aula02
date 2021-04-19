def calcularDesconto(valor_produto, desconto=5):
  desconto = valor_produto * (1-(desconto/100))
  return desconto

def validarCupom(cupom):
  if cupom == "DESCONTAO":
    return True
  else:
    return False

print(calcularDesconto(100, 10))