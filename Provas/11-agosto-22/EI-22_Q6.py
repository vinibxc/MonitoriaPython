# 6. Faça um programa que mostre os n termos da Série a seguir:
# S = 1/1 + 1/3 + 1/5 + 1/7 + 1/9 + ... + 1/n.
# Imprima no final a soma da série. Considere n um número que o usuário irá informar.
n = int(input("Digite ate onde a soma deve ir"))
i = 1
soma = 0
for i in range(1, n +1, 2):
    soma = soma + 1/i
print(f"Resultado = {soma}")