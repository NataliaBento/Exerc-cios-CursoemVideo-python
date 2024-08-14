#pessoas ={'nome': 'Natalia', 'sexo': 'F', 'idade': 22}
#print(pessoas['nome']) *mostra o nome natalia'
#print(f'A {pessoas["nome"]} tem {pessoas["idade"]} anos') *mosta Natalia 22
#print(pessoas.items()) 
#print(pessoas.keys()) *mostra apenas nome, sexo, idade
#print(pessoas.values()) *mostra nome e o conteúdo*
#print(pessoas.items())

#del pessoas['sexo'] #aqui deleta 
#pessoas['nome'] = 'Gustavo'
#pessoas['peso'] = '68.5'
#for k, v in pessoas.items():
    #print(f'{k}, = {v}')

#brasil = []
#estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
#estado2= {'uf': 'São Paulo', 'sigla': 'SP'}

#brasil.append(estado1)
#rasil.append(estado2)

#print(brasil[1] ['sigla'])

brasil = list()

for c in range(0, 3):
    estado = dict()  # Cria um novo dicionário para cada iteração
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
