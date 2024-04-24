soma = 0
cont = 0
contpar = 0
for c in range (1, 7):
    num = int(input("Digite um número: "))
    cont = cont + 1
    if num % 2 == 0:
        soma = soma + num
        contpar = contpar + 1
print(f"Você digitou {cont} números, sendo {contpar} PARES e a soma entre eles é: {soma}")

