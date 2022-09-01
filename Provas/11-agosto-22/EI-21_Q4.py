#4. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 100
# (utilize laço de repetição while para percorrer o intervalo de 1 até 100).
i = 1
impares = 0
while i <= 100:
    if i % 2  != 0:
        impares = impares + 1
    i = i + 1
print(f"Temos {impares} numeros impares.")