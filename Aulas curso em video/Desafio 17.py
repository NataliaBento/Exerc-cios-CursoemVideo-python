import math
oposto = float(input("Comprimento do Cateto Oposto: "))
adjacente = float(input("Comprimento do Cateto Adjacente: "))
hip = math.hypot(oposto, adjacente)
print (f"A hipotenusa é:{hip}")