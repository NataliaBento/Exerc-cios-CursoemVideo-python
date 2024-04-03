n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print(f"O maior valor digitado foi {maior}")   
menor = n2
if n1 < menor:
    menor = n1
if n3 < menor:
    menor = n3
print(f"O menor valor digitado foi: {menor}")


#para verificar o maior e o menor numero, eu poderia validar verificando um por um, porém para simplificar, eu posso definir uma variavel jogando um maior, e validar a partir dessa variável, exemplo se eu definir uma variavel para maior 'tal variavel é maior', eu vou validando a partir disso. Se a variavel maior que eu defini for n1 eu posso fazer a partir dela, se n2 for maior que a variavel a variavel vai receber n2... e assim por diante