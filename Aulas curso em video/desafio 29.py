velociat = float(input('Qual sua velocidade atual?'))
limite = 80
multa = (velociat -80) * 7

if velociat > limite:
    print(f'MULTADO! VOCÊ EXCEDEU O LIMITE PERMITIDO QUE É DE 80Km/h. Você deve pagar uma multa de R${multa}')
print(f'Sua velocidade atual é de {velociat}, tenha uma excelente viagem!')