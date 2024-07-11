numero = []
par = []
impar = []
while True:
    numero.append(int(input('Digite um número: ')))
    continuar = str(input('Quer continuar? [S/N]'))
    if continuar in 'Nn':
        break
print('='*30)
numero.sort()
print(f'O valores da lista são: {numero}')

for c in numero:
    if c % 2 == 0:
        par.append(c)
        
    else:
        impar.append(c)
        
print(f'Os numeros pares foram {par}')
print(f'Os numeros ímpares foram {impar}')