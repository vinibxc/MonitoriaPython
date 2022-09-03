# 1) Desenvolva um programa que leia 5 números inteiros e informe o maior
numeros = []
i = 0
while i < 5:
    num = int(input(f"Digite o {i}° numero: "))
    numeros.append(num)
print(f"O nmaior numero: {max(numeros)}")