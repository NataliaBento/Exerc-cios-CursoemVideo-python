salario = float(input("Qual o salário do funcionário? "))



if salario >= 1250: 
    aumento2= salario + (salario * 15 / 100)
    print (f"O funcionário que ganhava {salario} receberá {aumento2} de aumento")

else: 
    aumento = salario + (salario * 10 / 100)
    print(f"O Funcionário que ganhava {salario} receberá {aumento} de aumento")

