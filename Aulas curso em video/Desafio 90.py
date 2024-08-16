aluno = {}

aluno['nome'] = str(input(f'Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado!'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação!'
else:
    aluno['situacao']= 'Reprovado!'

for k, v in aluno.items():
   print(f'{k} é igual a {v}')