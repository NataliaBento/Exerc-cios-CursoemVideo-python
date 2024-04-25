soma = 0
contPar = 0
cont = 0
for c in range (1, 7):
    num = int(input("Digite um número: "))
    cont = cont + 1
    if num % 2 == 0:
        soma = soma + num
        contPar = contPar + 1
print(f"Você digitou {c} números, no total de {contPar} números pares e a soma dos valores par é {soma}")


    




