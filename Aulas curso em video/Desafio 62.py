print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1 
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <=total:
        print('->>', termo, end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais= int(input('Quantos termos a mais você quer?'))
print('Progressão finalizada com ', total, 'termos mostrados')