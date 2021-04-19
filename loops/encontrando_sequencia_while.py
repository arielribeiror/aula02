procurado = int(input("Qual número você quer ver se está na sequência de Lucas?"))

achei = False
anterior1 = 1
anterior2 = 3
atual = 0

while not achei and procurado > atual:
  atual = anterior1 + anterior2
  anterior1 = anterior2
  anterior2 = atual
  
  if procurado == atual:
    achei = True
    print("Encontrei o número!")
    
if not achei:
  print("O número não está na sequência")