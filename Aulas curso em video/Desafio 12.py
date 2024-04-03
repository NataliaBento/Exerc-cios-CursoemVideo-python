produto = float(input("Qual é o preço do produto? R$"))
desc = float(input("Digite o quanto de desconto você quer receber: "))
preco= produto - (produto * desc / 100) #o que está em parenteses é a representação gráfica do %#
print(f"O preço do produto com desconto de {desc} é de: R$ {preco}")
