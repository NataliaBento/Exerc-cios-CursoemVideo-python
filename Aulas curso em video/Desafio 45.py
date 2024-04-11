#aqui ele importa da bilioteca random o randint
from random import randint
#aqui ele importa da biblioteca time para esperar 1 segundo
from time import sleep
#aqui fiz eu declarei a variável como uma lista, dos 3 elementos que irei trabalhar
itens = ('Pedra', 'Papel', 'Tesoura')
#aqui o computador vai randomizar 1, fiz uma lista da quantidade de elementos que existem la em cima, para o computador jogar
computador = randint(0,2)
print('''Suas opções:
      [0]Pedra
      [1]Papel
      [2]Tesoura''')
jogador = int(input('Qual a sua jogada?')) #input para perguntar a jogada do jogador
print('JO') #nessa parte estou difinindo o tempo de cada um dos prints
sleep(1)
print('KEN')
sleep(1)
print('POO')
#aqui eu mandei mostrar na tela um item na posição computador, ou seja, eu vou escolher na variável da variável ITENS, uma posição de 0 a 2, onde 0 é pedra, 1 é papel e 2 é tesoura
print(f'O computador escolheu {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
#aqui são as condições aninhadas, defino sempe o computador para me basear,e vou fazendo uma estrutura dentro da outra para definir as condições de perca ou ganho
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR GANHOU')
    elif jogador == 2:
        print('COMPUTADOR GANHOU')
    else:
        print('JOGADA INVÁLIDA')
if computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR GANHOU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR GANHOU')
    else:
        print('Jogada Inválida')
if computador == 2: #computador jogou TESOURA

    if jogador == 0:
        print('JOGADOR GANHOU')

    elif jogador == 1:
        print('COMPUTADOR GANHOU')
    
    elif jogador == 2:
        print('EMPATE')
    
    else:
        print('Jogada Inválida')