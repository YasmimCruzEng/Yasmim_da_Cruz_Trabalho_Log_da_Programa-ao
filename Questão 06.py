#Utilizando o comando "float" para identificar um número real e o comando "input" para que o aluno digite suas informações:
n1= float(input("Digite sua primeira nota: "))
n2= float(input("Digite sua segunda nota: "))

#Utilindo o "+" para somar e o "/" para dividir e se ter a média das notas
media = (n1 + n2)/2
print(f"Sua média é: {media}")

#"if", "elif" e "else" para identificar se o auno foi aprovado, reprovado ou está de recueração:
if media >=7:
    print("PARABENS! Você foi aprovado!")
elif  media >=5:
    print("Foi quase! Você está de recuperação.")
else:
    print("Você está reprovado!")