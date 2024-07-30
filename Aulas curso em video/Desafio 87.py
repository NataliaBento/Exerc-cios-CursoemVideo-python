matriz = [[0, 0, 0], [0,0,0], [0,0,0]] 
spar = mai = scol = 0
for l in range (0, 3):
    for c in range (0,3):
        matriz [l] [c] = int(input(f'Digite um valor para {l} e {c}: '))
print('='*40)
for l in range (0, 3):
    for c in range (0, 3):
        print(f'[{matriz[l] [c]:^5}]', end='')
        if matriz [l][c] % 2 == 0:
            spar += matriz [l][c]
    print()
print('='*40)   
print(f'A soma dos valores pares foi: {spar}')
for l in range (0, 3): 
    scol += matriz [l][2] 
print(f'A soma dos elementos da terceira coluna foi: {scol}') #para conseguir a soma da terceira coluna, eu preciso avaliar o código, a terceira coluna nunca vai mudar, sempre vai ser a posição 2 da matriz. Então eu tenho que fazer um range para a LINHA PORQUE? porque a linha vai varear e a coluna não, então eu faço um range de 0 a 3, indicando na matriz LINHA [L] e especificando a coluna que antes era definida como C agora vai ser definida como 2, pois ela não mudará.
for c in range (0,3):
    if c == 0:
        mai = matriz [1][c]
    elif matriz [1] [c] > mai:
        mai = matriz [1][c]
print(f'O maior valor na segunda linha é: {mai}') #para conseguir o maior valor da segunda coluna, segue o mesmo raciocínio do primeiro só que o contrario, ou seja, a linha vai ser sempre a mesma, o que vai varear é a coluna, então irei fazer um for com IF para achar o maior valor para a COLUNA. Se no range a primeira iteração for 0 ela vai receber o maior, então maior recebe matriz na posição linha 1 e coluna na primeira, se não, se a matriz nessa iteração for a maior, o maior vai receber a matriz na iteração que for maior