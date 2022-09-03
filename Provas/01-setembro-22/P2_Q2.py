# 2) Elabore um programa que receba 50 números inteiros informados pelo usuário (positivos, nulo, negativos) e apresente:
# a) Quantidade de números negativos, positivos e nulos.
# b) Média dos números negativos.
# c) Média dos números positivos.
# d) Média geral.
numeros = []
negativos = 0
somaN = 0 # soma dos valores negativos
nulos = 0
positivos = 0
somaP = 0 # soma dos valores positivos
somaG = 0 # soma de todos os valores
i = 0
while i < 50:
    num = int(input(f"Digite o {i}° número:"))
    somaG += num
    numeros.append(num)
for i in numeros:
    if i < 0:
        negativos += 1
        somaN += i
    if i == 0:
        nulos  += 1
    if i > 0:
        positivos += 1
        somaP += i
mediaP = somaP / positivos
mediaN = somaN / negativos
mediaG = somaG / 50
print(f"Negativos:{negativos}\nPositivos: {positivos}\nNulos: {nulos}")
print(f"Media dos numeros negativos: {mediaN}")
print(f"Media dos numeros positivos: {mediaP}")
print(f"Media geral: {mediaG}")