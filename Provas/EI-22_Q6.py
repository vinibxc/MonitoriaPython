n = int(input("Digite ate onde a soma deve ir"))
i = 1
soma = 0
for i in range(1, n +1, 2):
    soma = soma + 1/i
print(f"Resultado = {soma}")