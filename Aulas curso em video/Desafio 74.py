from random import randint
maior = menor = 0
numero = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),
          randint(1,10))
for c in numero:
    print(f'{c}', end='')
print(f'\nO maior valor sorteado foi: {max(numero)}')
print(f'O menor valor sorteado foi: {min(numero)}')