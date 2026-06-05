#Utilizando o comando "float" para identificar um número real e o comando "input" para que o usuário informe um número:
numero= float(input("Digite um número: "))

print(f"A tabuada do {numero} é: ")

#Utilizar "for" "in", o "range" (para repetição) e "*" para a multipicação da tabuada
for n in range (1, 11):
    resultado = numero * n
    #print para mostrar ao usuário o resultado da tabuada
    print(f"{numero} X {n} = {resultado}")