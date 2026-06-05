#Primeiro se utiliza o "inpunt" para que o usuário digite as informações necessárias
Celsius = float(input("Digite a temperatura em Celsius: "))

#Usando o "+" para a soma, "*" para multiplicação e "/" para divisão , assim o pycham pode realizar a formula:
fahrenheit = ((9*Celsius)/5) + 32

#Por fim, se utiliza o comando "print" para mostrar ao usuário o resultado:
print(f"A temperatura em fahrenheit é: {fahrenheit:.2f}°F")