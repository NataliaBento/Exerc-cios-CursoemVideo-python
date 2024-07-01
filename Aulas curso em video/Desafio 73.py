times = ('Corinthians', 'Palmerias', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 
         'São Paulo', 'Fluminense', 'Sport-Recife', 
         'EC-Viória', 'Curitiba', 'Avaí', 'Ponte-Preta', 
         'Atlético-GO')
print('-='*15)
print(f'Lista de times, do Brasileirão {times}')
print('-='*15)
print(f'Os cinco primeiros times são {times[0:5]}') #aqui ele vai contar de  0 a 5
print('-='*15)
print(f'Os 4 ultimos colocados são {times[-4:]}') #aqui ele vai contar até o item 4 de trás para frente, os dois pontos significa 'até'
print('-='*15)
print(f'Times em ordem alfabética: {sorted(times)} ') #aqui ele vai ajustar por ordem alfabética
print('-='*15)
print(f'O chapecoense está na {times.index('Chapecoense')+1}','posição')#para mostrar a posição se usa o index, como começa com zero, eu uso o +1 para ele reconhecer a posição