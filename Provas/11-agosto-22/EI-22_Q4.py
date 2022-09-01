# 4. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 100 (utilize laço de repetição
# while para percorrer o intervalo de 1 até 100).
i = 1
impares = 0
cont = 1
while i <= 100:
    if i % 2 != 0:
        print(f"{cont}° numero impar: {i} ")
        cont += 1
    i = i + 1