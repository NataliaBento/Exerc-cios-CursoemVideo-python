nota1 = float(input('Primeira Nota: '))
nota2 = float (input('Segunda Nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1} e {nota2} a médida do aluno é: {media}')
if media >= 7:
    print('O aluno está aprovado!!')
elif media >= 4 and media <= 6.9:
    print('O aluno está em recuperação')
else:
    print('O aluno está reprovado')    