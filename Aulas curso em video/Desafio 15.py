dias = int(input("Quantos dias alugados? ")) #os dias foram multiplicados pelo valor dado de 60 
km = float(input("Quandos kms rodados? ")) #os km foram multiplicados pelo valor dado de 0.15
pago = (dias * 60) + (km * 0.15) #depois eu faço a soma do resultado dos dois 
print (f"O valor a pagar é de: {pago}") #pq o programa nada mais era, que saber o total a pagar por dias e kms no total sabend que cada dia de aluguel custava 60 e cada km 15 centavos