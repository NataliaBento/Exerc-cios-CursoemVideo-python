from random import randint
from time import sleep
print('===========================================================')
print('Vou pensar em um numero de 0 a 5. Em que número eu pensei? ')
print('=============================================================')
computador = randint(0, 5)
jogador = int(input('Qual número você escolhe?'))
print('Processando')
sleep(2)
if jogador == computador:
    print('Parabéns você conseguiu me vencer!')
else: 
    print(f'Ganhei eu pensei no numero {computador} e não no numero {jogador}')
