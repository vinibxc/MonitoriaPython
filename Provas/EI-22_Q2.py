i = 0
pares = 0
impares = 0
numero = []
while i <= 9:
    numero.append(float(input(f"Digite o {i + 1}° numero:")))
    i = i +1
i = 0
while i <= 9:
    if numero[i] % 2 = 0 and numero[i] != 0:
        pares += 1
    if numero[i] % 2 != 0 and numero[i] != 0:
        impares += 1
    i = i + 1
print(f" Pares: {pares}\n Impares: {impares}")