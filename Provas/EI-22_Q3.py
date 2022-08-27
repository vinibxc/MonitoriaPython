numero= []
i = 0
while  i < 4:
    num = int(input("Digite um numero inteiro"))
    numero.append(num)
    i += 1

i = 0
while  i < 4:
    if numero[i] % 10 == 0:
        print(f"{i+1}°)O numero {numero[i]} é multiplo de 10")
    else:
        print(f"{i+1}°)O numero {numero[i]} não é multiplo de 10")
    i += 1