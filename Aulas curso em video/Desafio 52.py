n = int(input("Digite um número: "))
tot = 0
for c in range (1, n+1):
    if n % c == 0:
        tot = tot + 1   
if tot == 2:
        print(f"O numero foi divisível {tot} vezes, ele é primo")
else:
       print(f"O numero foi divisível {tot} vezes, ele não é primo")
