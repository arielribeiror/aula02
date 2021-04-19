irmao1 = int(input("Digite o ano de nascimento do 1º irmão"))
irmao2 = int(input("Digite o ano de nascimento do 2º irmão"))
irmao3 = int(input("Digite o ano de nascimento do 3º irmão"))
irmao4 = int(input("Digite o ano de nascimento do 4º irmão"))

if irmao1 < irmao2 and irmao1 < irmao3 and irmao1 < irmao4:
  print("O primeiro irmão é o mais velho")
elif irmao2 < irmao1 and irmao2 < irmao3 and irmao2 < irmao4:
  print("O segundo irmão é o mais velho")
elif irmao3 < irmao1 and irmao3 < irmao2 and irmao3 < irmao4:
  print("O terceiro irmão é o mais velho")
elif irmao4 < irmao1 and irmao4 < irmao3 and irmao4 < irmao2:
  print("O quarto irmão é o mais velho")
else:
  print("Existem irmãos com a mesma idade")