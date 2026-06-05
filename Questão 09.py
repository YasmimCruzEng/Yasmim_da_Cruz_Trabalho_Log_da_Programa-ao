#Primeiro de digita as informações do aluno com "{}":
aluno1 = {
    "Nome": "Yasmim da Cruz",
    "Idade": 24,
    "Curso": "Engenharia Civil"
}

#Depois com os comandos "for", "in" e "print" se mostra as informações:
print("Informações da Aluna:")
for chave, valor in aluno1.items():
    print(f"- {chave.capitalize()}: {valor}")