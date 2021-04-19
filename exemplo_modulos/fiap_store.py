from funcoes import *

produtos = []

while "S" in input("Quer continuar digitando? S ou N"):
  produtos.append(float(input("Digite o preço do produto")))
  
cupom = input("Digite o seu cupom de desconto")

if validarCupom(cupom):
  for produto in produtos:
    print("O produto passou a custar {}".format(calcularDesconto(produto)))
else:
  for produto in produtos:
    print("O produto custa {}".format(produto))
