itens_mesa = []

resposta = "Sim"

while ("Sim" in resposta):
  itens_mesa.append(input("Digite algo que tem na mesa"))
  resposta = input("Deseja informar mais um item? Sim ou Não")

for item in itens_mesa:
  print(item)
  
itens_mesa.insert(1, "Pote")
print(itens_mesa)

itens_mesa.pop(1)
print(itens_mesa)

itens_mesa.sort(reverse=True)
print(itens_mesa)

print("Nessa lista tem {} itens".format(len(itens_mesa)))

itens_mesa.clear()
print(itens_mesa)