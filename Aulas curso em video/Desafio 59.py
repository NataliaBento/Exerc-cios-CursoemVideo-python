n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))

while True:
    print('+=================+')
    print('| MENU OPERAÇÕES  |')
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NÚMEROS')
    print('[5] SAIR DO PROGRAMA')

    op = int(input('>>>>>> Qual é a sua opção: '))

    if op == 5:
        break
    elif op == 1:
        soma = n1 + n2
        print('O resultado da soma entre, ', n1, 'e', n2, 'é:', soma)
    elif op == 2:
        multiplicar = n1 * n2
        print('O resultado da multiplicação entre ', n1, 'e', n2, 'é:', multiplicar)
    elif op == 3:
        if n1 > n2:
            maior = n1
            print('O maior valor entre: ', n1, 'e', n2, 'é: ', maior)
        elif n1 == n2:
            print('Os números são iguais!')    
        else:
            maior = n2  
            print('O maior valor entre: ', n1, 'e', n2, 'é: ', maior)  
    elif op == 4:
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    else:
        print('Digite uma opção válida!')
    