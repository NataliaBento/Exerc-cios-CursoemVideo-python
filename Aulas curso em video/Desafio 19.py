from random import choice
n1 = input("Primeiro aluno: ")
n2 = input("Segundo Aluno: ")
n3 = input("Terceiro Aluno: ")
n4= input("Quarto Aluno: ")
lista= [n1, n2, n3, n4]
escolhido = choice(lista)
print (f"O aluno escolhido foi: {escolhido}")