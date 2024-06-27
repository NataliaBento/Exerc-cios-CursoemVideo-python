
sexo = str(input("Informe seu sexo: [M/F]")).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input("Dados Inválidos. Por favorm informe seu sexo: [M/F]"))
print('Sexo Registrado com sucesso!')

#jogo da advinhação
num = int(input("Digite um número de 0 a 20: "))
while num != 15:
    if num > 20:
        print('Digite um número dentro dos limites permitidos!')
    elif num < 5:
        print('O número secreto é a maior!')
    elif num == 14:
        print('você está muito perto!')

print("Parabéns você acertou!")
