from random import shuffle
n1 = input("Digite o primeiro aluno: ")
n2 = input("Digite o segundo aluno: ")
n3 = input("Digite o terceiro aluno: ")
n4 = input("Digite o quarto aluno: ")
lista = [n1, n2, n3, n4]
shuffle(lista)
print("A ordem de apresentação ficará assim: ")
print(lista)