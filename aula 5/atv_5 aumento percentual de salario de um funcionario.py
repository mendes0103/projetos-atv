print("aumento percentual de salario de um funcionario")
salario= float(input("quanto é o atual salario?"))
percentual= float(input("qual o percentual?"))
aumento= salario * percentual /100
novo_salario= aumento + salario
print(f"o valor de aumento é: R${aumento} e voce tera um salario de: R${novo_salario}")