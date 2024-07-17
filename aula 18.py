#teste = []
#teste.append('Natalia')
#teste.append(32)
#galera = []
#galera.append(teste[:])
#teste[0] = ('Naty')
#teste[1] = (23)
#galera.append(teste[:])
#print(galera)

#galera = [['Natalia', 32], ['Cecilia', 31], ['Mariana', 35],['Rafaela', 28]]
#for p in galera:
    #print(f'{p[0]} tem {p[1]} de idade')

galera = []
dado = []
totmaior = totmenor = 0
for c in range (0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear() #evita que dentro do looping os numeros de repitam a cada iteração

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade!')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade!')
        totmenor += 1
print(f'No total temos {totmaior} pessoas maiores de idade e {totmenor} pessoas menor de idade')