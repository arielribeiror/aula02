numero = int(input("Digite o número do qual deseja obter a tabuada"))
i = 1
while(i<=10):
  resultado = numero * i  
  print("{} X {} = {}".format(numero, i, resultado))
  i+=1