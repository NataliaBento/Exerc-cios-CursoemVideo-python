num = (
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: '))
)

print(f'Você digitou os valores {num}')
print(f'Você digitou o valor 9, {num.count(9)} vezes')

if 3 in num:
    print(f'O valor 3 apareceu na posição {num.index(3) + 1}')
else:
    print('O valor 3 não apareceu!')

print('Os valores pares digitados foram:', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
