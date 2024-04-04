from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
if idade == 18:
    print('Você deve se alistar imediatamente!!')
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print(f'Você ja deveria ter se alistado ha {saldo}')
    print(f'Você deveria ter se alistado em {ano}')

elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print(f'Ainda faltam {saldo} para se alistar')
    print(f'Você vai se alistar em {ano}')