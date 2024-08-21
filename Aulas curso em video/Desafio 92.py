from datetime import datetime 

dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['CTPS']= int(input('Carteira de trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados ['idade'] +(dados['Contratação'] + 35) - (datetime.now().year)
print('-=' * 40) 
for k, v in dados.items():
    print(f'  - {k} = {v}')