total = totmil = menor = maior =cont=  0
barato = '-'
caro = '-'
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço R$ '))
    cont += 1
    total = total + preco
    if preco > 1000:
        totmil += 1
    resp = '-'
    if cont == 1:
        menor = preco
        maior = preco
        barato = produto
        caro = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
        if preco > maior:
            maior = preco
            caro = produto
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
    
print('-'*30)
print(f'O total da compra foi: {total}')
print(f'{totmil} passaram de R$1.000')
print(f'O produto mais barato foi o {barato} que custa {menor} e o produto mais caro foi o {caro} custando {maior}')