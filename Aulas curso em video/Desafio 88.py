from random import randint #aqui eu estou importando a biblioteca de números
from time import sleep #aqui to importando a biblioteca de tempo 
lista = [] #crio uma lista para armazenar os numeros como copias e depois limpar
jogos = [] #nessa outra lista eu crio para armazenar os numeros
print('='*40)
print('         JOGA NA MEGA SENA              ')
print('='*40)
resp = int(input('Quantos jogos você quer que eu sorteie? ')) #aqui eu pergunto ao usuário quantas vezes ele quer que o sistema sorteie
tot = 1 #esse contador seve para contar até achar a resposta do input
while tot <= resp: #enquanto o total for menor ou igual a resposta eu faço esse outro looping
    cont = 0 #esse contador serve para eu contar os numeros dentro da lista 
    while True: #o laço começa definindo a variável que vai gerar esses números junto com os numeros de importação
        num = randint (1, 60)
        if num not in lista: #se o numero não esta na lista 
            lista.append(num) #eu faço um append e o numero vai aparecer 
            cont += 1 #depois eu vou utilizar o contador de la de cima o 'cont' para contar as iterações dentro da lista
        if cont >= 6: #se chegar a 6 ou for maior ele vai parar
            break
    lista.sort()    #aqui eu organizo os itens por ordem dentro da lista
    jogos.append(lista[:]) #aqui eu estou utilizando outra lista para receber a lista com copia, como funciona?  quando eu utilizo a cópia, eu estou utilizando a lista apenas para armazenar aqueles numeros momentaneamento, porque depois eles serão apagados em lista, e não em jogos, sendo assim a lista de jogos vai receber as copias e as listas serão apagadas a cada iteração para receber novos numeros
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {resp} JOGOS', '-=' * 3) #aqui apenas um recurso visual para mostrar quantos jogos o usuário pediu
for i, l in enumerate(jogos): #aqui ele vai fazer para cada indice da lista ele vai enumerar cada jogo e mostrar suas posições
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! > ', '-=' * 5)



