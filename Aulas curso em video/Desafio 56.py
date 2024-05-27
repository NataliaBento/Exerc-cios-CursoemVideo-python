somaidade = 0
maioridade = 0
nomevelho = ""
contmenos = 0
for p in range (4):
    nome = str(input("Qual o seu nome?"))
    idade = int(input("Qual a sua idade?"))
    sexo = str(input("Qual gênero você se identifica? "))
    somaidade = somaidade + idade
    if p == 1 and sexo == "homem":
        maioridade = idade
        nomevelho = nome
    if idade > maioridade and sexo == "homem":
        maioridade = idade
        nomevelho = nome
    if sexo == "mulher" and idade < 20:
        contmenos = contmenos + 1



media = somaidade / 4 


print("A media das idades é: ", media,"anos")
print("A maior idade entre os homens é de", nomevelho, "com", maioridade, "anos")
print("A quantidade de mulheres com menos de 20 anos é", contmenos, "de mulheres")




