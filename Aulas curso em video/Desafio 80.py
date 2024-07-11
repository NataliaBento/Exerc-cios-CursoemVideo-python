lista = []
for c in range(0,5):
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[-1]: #se c for igual a 0, ele será o primeiro valor, ou seja só preciso adicionar normal com append ou se o número for maior do que o numero que está no final
        lista.append(n)
        print('Adicionado ao final da lista...')
    else: #para esse caso eu preciso varrer o vetor inteiro para descobrir em que posição o numero está e para isso eu faço: 
        pos = 0 #aqui eu crio uma variavel de posição que vai receber 0 no início
        while pos <= len(lista): #enquanto a posição for menor que o len de lista, ou seja, eu vou do 0 até a ultima posição da lista varrendo os vetores
            if n <= lista[pos]: #aqui eu verifico se o numero que eu quero inserir ou seja o n, é menor ou igual a ele, a ele quem? a cada numero da lista, por isso o pos, de posição. 
                lista.insert(pos, n)#e se for, eu não vou usar o append eu vou usar o  insert, que vou colocar na posição POS, o valor n 
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1 #aqui eu vou varrendo as posições 1 por 1 

print('='*30)
print(f'O valores digitados em ordem foram: {lista}')