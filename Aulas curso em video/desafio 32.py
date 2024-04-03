#para achar se o ano é bissexto o ano tem que ser dividido por 4, porém existem exceções, que são ela: 
#o ano bissexto ocorre de quatro em 4 anos ou seja (multiplo de 4), exceto em anos multiplos de 100 ou seja (o resto da divisão do ano por 100 tem que ser diferente de zero) e que não são multiplos de 400. ou seja o ( o ano tem que ser divisivel por 400 ou seja, restar 0)
from datetime import date
ano = int(input("Que ano você quer analisar? Coloque 0 para analisar o ano atual: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano %400 == 0:
    print(f"O ano de {ano} é BISSEXTO")
else:
    print(f"O ano de {ano} NÃO é BISSEXTO")
