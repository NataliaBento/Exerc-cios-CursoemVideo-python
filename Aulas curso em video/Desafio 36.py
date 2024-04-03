valorCasa = float(input('Valor da casa:R$'))
salarioComprador = float(input('Salário do comprador:R$'))
anosFinanciamento = int(input('Quantos anos de financiamento:?'))
prestacao = valorCasa / (anosFinanciamento * 12)
minimo = salarioComprador * 30 / 100
print(f'Para pagar uma casa de R${valorCasa} em {anosFinanciamento} anos, a prestação sera de R${prestacao}')
if prestacao <= minimo:
    print('O emprestímo foi AUTORIZADO')
elif prestacao > minimo:
    print('O emprestímo foi NEGADO.')
