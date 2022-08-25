i = 0
negativos = 0
nulos = 0
positivos = 0
numero = []
while i <= 9:
    numero.append(float(input(f"Digite o {i + 1}° numero:")))
    i = i +1
i = 0
while i <= 9:
    if numero[i] < 0:
        negativos = negativos + 1
    if numero[i] > 0:
        positivos = positivos + 1
    if numero[i] == 0:
        nulos = nulos + 1
    i = i + 1
print(f" Nulos: {nulos} \n Positivos {positivos} \n Negativos {negativos}")
