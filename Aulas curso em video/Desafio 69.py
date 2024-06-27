print('-'*30)
print('CADASTRE UMA PESSOA')
print('-'*30)
i = s = c = 0
idade = int(input('Idade: '))
sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
while continuar == 'S':
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if idade > 18:
        i +=1
    if sexo == 'M':
        s += 1
    if sexo == 'F' and idade < 20:
        c += 1

print(f'Total de pessoas com mais de 18 anos: {i}')
print(f'Ao todo temos {s} homens cadastrados')
print(f'E temos {c} mulheres com menos de 20 anos')