nome = str(input("Digite seu nome completo:")).strip()
print("Analisando seu nome...")
print(f"Seu nome em maiúscula é {(nome.upper())}" )
print(f"Seu nome em minúscula é: {(nome.lower())}")
print(f"Seu nome tem ao todo tem {len(nome)} caracteres" )
#print(f"Seu primeiro nome tem {(nome.find(""))}")
separa = nome.split()
print(f"Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras")


