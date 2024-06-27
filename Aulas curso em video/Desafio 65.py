resp = 'S'
cont = soma = maior = menor = 0

while resp in 'Ss':
    n = int(input('Digite um número: '))
    resp = str(input('Quer Continuar? [S/N] ')).upper().strip()[0]
    cont += 1
    soma += n
    
    if cont == 1:
        maior = menor = n 
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
media = soma / cont   
print('Você digitou', cont, 'numeros', 'a soma deles é: ', soma, 'e a media entre eles é: ', media)    
print('O maior valor digitado foi: ', maior, 'e o menor valor foi: ', menor)