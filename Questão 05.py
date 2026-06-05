#Utilizando o comando "float" para identificar um número real e o comando "input" para que o usuário informe um número
numero = float(input("Digite um número: "))

#Utilizando o "if", "elif" e o "else" para identificar as opções de como esse número seria:
if numero > 0:
    print("O número é positivo")
elif numero < 0:
    print("O número é negativo")
else:
    print("O número é zero")