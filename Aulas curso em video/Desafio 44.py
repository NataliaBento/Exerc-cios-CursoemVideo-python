print('=========LOJAS GUANABARA==========')
preco= float(input('Preços das compras: R$ '))
print('''FORMAS DE PAGAMENTO')
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual a opção?'))
if opcao == 1:
    desc = preco - (preco * 10 / 100)
    print(f'Sua compra de R${preco} vai custar R${desc} com 10% de desconto!')   
elif opcao == 2: 
    desc = preco - (preco * 5 / 100)
    print(f'Sua compra de R${preco} vai custar R${desc} com 5% de desconto!')
elif opcao == 3:
        print(f'Sua compra de R${preco} em 2x vai custar o preço normal de R${preco}')
elif opcao == 4:
         totparc = int(input('Quantas parcelas?'))
         total = preco + (preco * 20 / 100)
         parcela = total / totparc
         print(f'Sua compra de será parcela em {totparc} de {parcela} e o preco final será: {total} com juros')  
else:
    print('Digite uma opção valida!')
