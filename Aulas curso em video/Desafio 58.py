#jogo da advinhação
from random import randint
computador = randint(0, 10)
print('Sou seu computador...')
print('Acabei de pensar em número entre 0 e 10')
print('Será que você consegue advinhar qual foi?')

acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Qual o seu palpite: ?"))
    palpites +=1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Menos... Tente mais uma vez')
        elif jogador < computador:
            print('Mais... Tente mais uma vez: ')
print('Você acertou com: ', palpites, 'palpites')
    