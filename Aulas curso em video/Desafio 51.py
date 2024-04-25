print("10 TERMOS DE UMA PA")


termo1 = int(input("Digite o primeiro termo: "))
razao = int(input("Razão: "))
decimo = termo1 + (10 - 1) * razao
for c in range (termo1, decimo + razao, razao):
    print(f"{c}", end= "-->")
print("ACABOU")