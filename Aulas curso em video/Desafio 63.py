print('-' *30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos voce quer mostrar? '))
t1 = 0
t2= 1
print('~'*30)
print(t1, t2, end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(t3, end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
