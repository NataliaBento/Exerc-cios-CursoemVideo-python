ficha = []

while True:
    nome = str(input('Nome: '))
    Nota1 = float(input('Primeira Nota: '))
    Nota2 = float(input('Segunda nota: '))
    media = (Nota1 + Nota2) / 2
    ficha.append([nome, [Nota1, Nota2], media])

    resp = str(input('Quer continuar? [S/N]')).strip().upper()
    if resp in 'nN':
        break
print('='*30)
print(f'{"No.":<4} {"NOME":<10} {"MEDIA":>8}')
print('='*26)
for i, a in enumerate(ficha):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8.1f}')
while True:
    print('='*35)
    opc = int(input('Digite o numero correspondente ao aluno para mostrar suas notas ou digite 999 para interromper: '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) -1:
        print(f'As Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('VOLTE SEMPRE!')
