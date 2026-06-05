v1 = float(input("Digite qualquer número: "))
v2 = float(input("Digite outro número: "))

soma = v1 + v2
subtracao = v1 - v2
multipicacao = v1 * v2

if v2 !=0:
    divisao = v1 / v2
else:
    divisao = "não é possível dividir por zero!"

print("\n RESULTADOS:")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multipicacao}")
print(f"Divisão: {divisao}")