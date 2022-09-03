# 2) Elabore um programa que receba 25 números inteiros informados pelo usuário (positivos, nulos, negativos) e apresente
# a) Quantidade de números pares e ímpares.
# b) Percentual de números pares e percentual de ímpares.
numeros = []
pares = 0
impares = 0
percentualP = 0
percentualI = 0
i=0

while i < 25:
    num = int(input(f"Digite o {i+1}° numero: "))
    numeros.append(num)
    i += 1

for i in numeros:
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Numeros pares: {pares}")
print(f"Numeros impares: {impares}")

percentualI = (impares*100) / 25
percentualP = (pares*100) / 25
print(f"percentual de impares: {percentualI}%")
print(f"percentual de pares: {percentualP}%")
