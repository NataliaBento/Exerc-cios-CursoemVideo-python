salario = float(input("Qual o salário do funcionário? R$ "))
desejo = float(input("Quanto de aumento você quer receber? "))
aumento = salario + (salario*desejo/100)
print (f"O funcionario quer receber R${aumento} de salário")
