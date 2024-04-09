peso = float(input('Qual seu peso? (Kg)'))
altura = float(input('Qual a sua altura? (m)'))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc}')
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc >= 18.5 and imc <= 25:
    print('Você está no seu peso ideal!')
elif imc >25 and imc <=30:
    print('Você está com sobrepeso')
elif imc > 30 and imc <= 40:
    print('Você está OBESO!')
elif imc >40:
    print('Você está com OBESIDADE MÓRBIDA, CUIDADO!')