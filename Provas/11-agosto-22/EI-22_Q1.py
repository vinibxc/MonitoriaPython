#1. Faça um programa que leia 5 números e informe a soma desses números.
i = 1
soma = 0
while i <= 5:
    num = int(input(f"Digite o {i}° numero: "))
    soma = soma + num
    i += 1
print(f"Soma dos 5 numeros: {soma}")