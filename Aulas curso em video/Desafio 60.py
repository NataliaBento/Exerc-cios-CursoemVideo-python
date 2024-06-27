n = int(input('Digite um número para calcular seu fatorial: '))
c = 1
f = 1
print('Calculando =', n, end='')
while c > 0:
    print(c, end='')
    print('x' if c > 1 else '=', end='')
    f *= c
    c -= 1
print(f)