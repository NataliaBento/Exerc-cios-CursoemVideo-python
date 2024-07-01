#tuplas - uma variável que guarda vários valores

lanche = ('hambuguer', 'suco', 'pizza', 'pudim')

print(lanche[1]) #vai aparecer suco 

print(lanche[:2]) #vai aparecer de hamburguer até suco, porque ele exclui o último

print(lanche[1]) #vai aparecer a partir da posição 1 ( que é suco), até o final

print(lanche[-1]) #vai tirar 1 de trás para frente vai aparecer pudim

print(lanche[-3:]) #vai pegar do objeto na posição 3 até o final no caso fica suco pizza e pudim

#as tuplas são imutáveis no python

for c in lanche:
    print(f'eu comi {c}')
print('Comi pra caralho')

#para cada iteração no for dentro do laço, eu vou pegar um elemento de dentro da tupla, até que seja finalizado 
#para c em CADA elemento dentro de LANCHE

#outra maneira de fazer

for cont in range (0, len(lanche)):
    print(f'Eu comi ', lanche[cont[2]])
print('Comi pra caralho')
 
#coloquei um contador, com um loopig de iteração, o 0 é eu dizendo onde eu quero começar, o len é pra a contagem, se eu mandar imprimir lanche, ele vai me dizer só os numeros que estão essas posições, mas se eu colocar cont a ideia é essa: lanche que é a tupla, na posição de cont! ou seja, cada iteração que ele fizer, ele vai passar por uma e vai imprimindo as posições atribuidas

#outra maneira de fazer

for pos, comida in enumerate (lanche):
    print(f'Eu vou comer {comida} na posição {pos}') 

#dessa modo, eu quero apresentar não só a tupla mas a posição que ela está, o pos será o contador enumerate para mostrar as posições que o contador POS está, e o lanche que é a tupla

#organizando tuplas esse comando organizar por ordem os itens das tuplas
print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c.count(5)) #aqui ele vai contar quantas vezes o numero entre parenteses aparece na tupla c
print(len(c)) #aqui ele vai mostrar o tamanho da tupla c, quantos itens ele tem 
print(c)
print(c.index(8)) #aqui ele vai mostrar a posição que 8 está
print(c.index(5, 1)) #nesse caso aqui tem dois 5, ele sempre vai considerar o primeiro, então eu tenho que especificar no segundo numero ao lado no caso o (1) em qual posição eu quero que comece a busca por ele, nesse caso ai o 5 ta na posição 0, ai eu coloquei para começar na posição 1 a contagem, e ai começa a partir do 1 e ai sim ele vai conseguir pegar o segundo 5

#as tuplas aceitam tipos diferentes, diferente do java que só aceita de um tipo, as tuplas para o python pode ter tipos diferentes, exemplo:
pessoa = ('Gustavo', '42', 'M', '1988')

#a tupla é imutável, mas se for para apagar ela toda pode, eu só não posso apagar um elemento de dentro
del(pessoa)
print(pessoa)#ele não vai mostrar mais porque foi deletado lá em cima

