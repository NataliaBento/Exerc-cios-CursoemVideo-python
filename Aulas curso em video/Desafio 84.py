temp = []
princ = []
totmaior = totmenor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    continuar = (str(input('Quer continuar? [S/N]')))
    temp.append(temp[:])
    temp.clear()
    print(princ) #evita que dentro do looping os numeros de repitam a cada iteração
    if continuar in 'Nn':
        print('Programa finalizado')
        break

