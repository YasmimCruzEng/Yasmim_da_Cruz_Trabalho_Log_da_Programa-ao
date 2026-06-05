#Primeiro se cria uma lista mas sem preencher ela:
listadecompras = []

#Com o comando "for", "in" e ".append" para se adiciona itens a lista, "range" para repetir o comando e o "input" para que o usuário digite o item:
print("Quais são seus 5 itens de compra?")
for compras in range(5):
    item = input(f"O {compras+1}° da sua lista: ")
    listadecompras.append(item)

#Com o print se mostra a lista de compras completa:
print("\n Aqui está sua lista de compras:")
for item in listadecompras:
    print(f" - {item}")