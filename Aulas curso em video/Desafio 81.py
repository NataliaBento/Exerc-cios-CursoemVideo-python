valores = []

while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar? [S/N]'))
    if continuar in 'Nn':
        break
print('='*30)
print(f'Você digitou {len(valores)} valores')
valores.sort(reverse=True)
print(f'O valores em ordem decrescente são: {valores}') 
if 5 in valores:
    print('O valor 5 faz parte da lista!') 
else:
    print('O valor 5 não faz parte da lista!')  