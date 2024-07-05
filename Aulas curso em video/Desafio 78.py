listanum = []
maior = menor = 0
for c in range (0, 5):
    listanum.append(int(input('Digite um valor: ')))
    if c == 0:
        maior = listanum[c]
        menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print(f'Você digitou os valores {listanum}')

print(f'O maior valor foi : {maior} na posições: ')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor falor foi {menor} nas posições: ')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')