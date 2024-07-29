matriz = [ [0, 0, 0], [0, 0 , 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range (0, 3):
    for c in range (0,3):
        matriz [l] [c] = int(input(f'Digite um valor para [{l}, {c}]:'))
print('='* 40)
for l in range (0, 3):
    for c in range (0, 3):
        print(f'[{matriz[l] [c]:^5}]', end='')
        if matriz [l] [c] % 2 ==0:
            spar += matriz [l][c]
        if len(matriz[c]) == 2:
            scol += matriz[c]
    print()
print('=' * 40)
print(f'A soma dos numeros pares é: {spar}')
print(f'O maior número digitado: {mai}')
print(f'A soma da coluna é: {scol}')