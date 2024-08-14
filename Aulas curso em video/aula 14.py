#c = 1
#while c < 10:
    #print(c)
    #c = c + 1
#print("FIM")

#r = 's'
#while r == 's':
    #n = int(input("Digite um valor: "))
    #r = str(input("Quer continuar? [S/N]"))
#print("FIM")

n = 1
par = impar = 0

while n !=0:
    n = int(input("Digite um valor: "))
    if n != 0:
        if n % 2 == 0:
            par +=1
        else:
            impar +=1
print('O total de números pares é:', par, "e o total de numeros impares é: ", impar)