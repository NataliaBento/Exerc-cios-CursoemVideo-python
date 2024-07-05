#num = [2,5,9,1] aqui é uma lista comum
#num[2] = 3 aqui é uma lista na posição 2, que vai receber 3
#num.append(7) aqui adiciona um valor no final da lista de valor 7
#num.sort(reverse=True) aqui ele conta a lista de trás para a frente
#num.insert(2,0) aqui eu to colocando na posição DOIS (2) o valor ZERO (0)
#num.insert(2,2) aqui eu to olocando na posição DOIS (2) o valor (2)
#if 5 in num: #aqui eu coloquei um if para verificar se 5 está em num
    #num.remove(5) #se sim, ele vai remover dos num 
#else:
    #print('Não achei o numero 5') #se o 5 não estiver em num, ele não vai achar e não vai fazer nada 
#print(num) 
#print(f'Essa lista tem {len(num)} elementos') #aqui ele conta quantos elementos tem em uma lista, com a função LEN 

#valores=[]

#valores.append(5)
#valores.append(9)
#valores.append(4)

#for v in valores: #para cada valor in valores
    #print(v)

#for cont in range(0,5): #aqui eu fiz um for para definir um contador e fazer um input e embaixo eu só fiz mostrar os indices de acordo com os valores digitados aqui em cima, para isso peguei a lista valores, fiz o apprend para adicionar e fiz um input para o usuário digitar os valores que ele queria 
    #valores.append(int(input('Digite um valor: ')))

#se eu quiser os indices e as chaves
#for i, v in enumerate(valores): #o enumerate pega tanto a chave quanto o valor, ou seja tanto o i quanto o c
    #print(f'Na posição {i}, encontrei o valor {v}')  
#print('Cheguei ao final da lista')

a = [2,3,4,7]
#b= a
b = a[:] #quando faço isso ele cria uma copia de A para B, então sendo assim nesse caso ele só irá mudar o B como pedido #B recebe todos os itens de A com esse comando [:]
b[2] = 8 #quando faço isso no python, ele não duplica ele junta uma lista na outra, ou seja tanto a lista A quanto a lista B, serão alteradas, isso é uma peculariedade do python
print(f'Lista A: {a}')
print(f'Lista B: {b}') 
