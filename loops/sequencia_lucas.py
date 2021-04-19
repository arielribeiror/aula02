quantidade = int(input("Quantos números da sequência você deseja exibir?"))

anterior1= 1
anterior2= 3
atual= 0

for i in range(1, quantidade, 1):
  atual = anterior1 + anterior2
  anterior1 = anterior2
  anterior2 = atual
  print(atual)
  