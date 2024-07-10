numero = []

while True:
    n = int(input('Digite um valor: '))
    if n not in numero:
        numero.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar!')
    continua = str(input('Quer continuar? [S/N]')).upper()[0]
    if continua in 'Nn':
        break
numero.sort()
print('='*30)
print(f'Você digitou os valoes: {numero}')





