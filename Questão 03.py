#Utilizando o comando "float" para identificar um número real e o comando "input" para que o aluno digite suas informações:
n1= float(input("Digite sua primeira nota: "))
n2= float(input("Digite sua segunda nota: "))
frequencia= int(input("Digite sua frequência em porcentagem: "))

#Utilindo o "+" para somar e o "/" para dividir e se ter a média das notas
media = (n1 + n2)/2

#Como se tem dois fatores para aprovação se utiliza "and":
aprovado = (media >= 7) and (frequencia >= 75)
#O comando "not" para completar o comando acima e indicar quem é reprovado
reprovado_falta = not (frequencia>=75)

#"print" e "{}" para mostrar a média do aluno
print(f"Sua média é: {media:.1f}")

#"if" e "elif" para identificar quem foi aprovado ou reprovado
if aprovado:
    print("PARABENS! Você foi aprovado!")
elif  reprovado_falta or (media < 7):
    print("Você está reprovado!")
