#Primeiro se cria uma lista mas sem preencher ela:
numeros = []

#Com o comando "for", "in" e ".append" para se adiciona itens a lista, "range" para repetir o comando, o "input" para que o usuário digite o item e o "int" para identificar apenas números inteiros:
print("Digite 5 números inteiros:")
for n in range (5):
    valor = int(input(f"Digite o {n + 1}° número: "))
    numeros.append(valor)

#Com o print se mostrar os números e os comando "max" e "min" para identicar o maior e o menor:
print("\n RESPOSTAS")
print(f"Números digitados: {numeros}")
print(f"O maior número: {max(numeros)}")
print(f" O menor número: {min(numeros)}")