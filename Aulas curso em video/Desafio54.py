from datetime import date

ano_atual = date.now().year


somamaior = 0
somamenor = 0
for c in range(1,8):
    ano = int(input(f"Em que ano a {c} º pessoa nasceu? "))
    ano_atual = ano_atual - ano
    if ano < 18:
        somamenor = somamenor + 1 
    else:
        somamaior = somamaior + 1

print(f"Ao todo tivemos {somamaior} pessoas maiores de idade, e {somamenor} pessoas menores de idade") 
