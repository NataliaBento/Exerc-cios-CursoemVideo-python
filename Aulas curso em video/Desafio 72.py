cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 
        'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
        'dezoito', 'dezenove', 'vinte')
continuar = '-'
while True: 
    num =int(input('Digite um número entre 0 e 20: '))
    if num >=0 and num <=20:
        print(f'Você digitou o numero {cont[num]}')
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if continuar == 'N':
            break
    else:
        print('Tente novamente!', end=' ')   
             



#enquanto isso for verdade faça o input, se o numero estiver entre 0 e 20 pode parar o programa ja mostrando o print final, o TENTE NOVAMENTE ta fora da identação do IF, então ele será mostrado caso o usuário não dgite entre 0 e 20. 
#no final o print mostra o cont mostrando a posição que o numero foi digitado