#esse é um programa que vai calcular o valor da viagem a partir do km dela, se a viagem for menos que 200 km, ela vai ser multiplicada por 50 centavos, caso seja maior que 200, ela vai ser multiplicada por 45 centavos. 
#nesse começo aqui eu peço pra o usuário digitar a distância da viagem
distancia = float(input('Qual é a distância da sua viagem?'))
print(f'Você está prestes a começar uma viagem de {distancia}')
#aqui está a condição, se a viagem digitada for menor que 200 vai ser multiplicada por 50 centavos
#só que eu tenho que fazer também uma variável para o preço, pra eu poder atribuir esse valor. 
#então preço vai receber a distancia digitada multiplicado por 50 centavos
if distancia <= 200:
    preco = distancia * 0.50
    #nessa parte aqui é o senão, ai pq eu não coloco a distancia aqui? pq essa já é uma condição contraria a outra que n precisa de complemento, uma condição composta. 
    #será só o preço multiplicado por 45 centavos
else: 
    preco = distancia * 0.45
    #esse print no python, ele ta com um recuo pra tras, significa que ele ta fora da condição porém, ele vai executar a partir do valor digitado no input, pq o programa vai correr assim, o usuário vai digitar o numero, ele vai reconhecer se é maior ou menor que 200 e vai fazer a conta e jogar o print dentro da variável preço
print (f'Sua viagem é de R${preco}')

#para simplificar mais ainda, temos o operador terciário, que vai simplificar essa condição, e ficará assim:
#preco = distancia * 0.50 if distância <=200 else distância * 0.45   