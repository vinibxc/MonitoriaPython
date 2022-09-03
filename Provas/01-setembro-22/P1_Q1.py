# 1) Desenvolva um programa que leia 5 números inteiros e informe o menor dentre os três últimos números lidos.
numeros = []
i = 1
while i <= 5:
    num = int(input(f"Digite o {i}° numero:"))
    numeros.append(num)
    i += 1
i = 2
menor = numeros[i]
maior = numeros[i]
while i <= 4:
    if numeros[i] <= menor:
        menor = numeros[i]
    if numeros[i] >=maior:
        maior = numeros[i]
    i += 1
print(f"Maior numero: {maior}")
print(f"menor numero: {menor}")
