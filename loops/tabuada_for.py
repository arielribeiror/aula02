valor = int(input("Digite um valor para calcular a tabuada"))

for i in range(1,11,1):
  resultado = i * valor
  print("{} X {} = {}".format(valor, i, resultado))