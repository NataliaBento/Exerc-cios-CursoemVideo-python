from random import randint
v = 0
while True:
    jogador = int(input("Digite um valor: "))
    computador = randint(0,10)
    tipo = '-'
    total = jogador + computador
    while tipo not in 'PI':
        tipo = str(input("Par ou Ímpar? ")).strip().upper()[0]
    print(f"Você jogou {jogador} e o computador {computador}, no total {total}")
    print(f"DEU PAR" if total % 2 == 0 else "DEU IMPAR")
    if tipo == 'P':
        if total % 2 == 0:
            print("Você ganhou!")
            v += 1
        else:
            print("O computador ganhou")
            break
    elif tipo  == 'I':
        if total % 2 != 0:
            print("Você Ganhou")
            v += 1
        else:
            print("O computador ganhou!")
            break
    print("Vamos jogar novamente...")
print(f"GAME OVER! Você venceu {v} vezes")