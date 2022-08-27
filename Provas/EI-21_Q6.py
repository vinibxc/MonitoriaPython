nome = input("Digite o nome do atleta:")
saltos = []
i = 0

while i < 5:
    saltos.append(float(input(f"Digite o vlor do {i + 1}° salto:")))
    i += 1

melhor = saltos[0]
pior = saltos[0]
i = 0

while i < 5:
    if saltos[i] > melhor:
        melhor = saltos[i]
    if saltos[i] < pior:
        pior = saltos[i]
    i += 1

i = 0
soma = 0.0

while i < 5:
    if saltos[i] != melhor and saltos[i] != pior:
        soma += saltos[i]
    i += 1

media = soma / 3
i = 0


print(f"Atleta: {nome}\n\nMelhor salto: {melhor}m\nPior salto: {pior}m\nMedia dos demais saltos: {media}m\n")

print(f"Resultado final \n{nome}: {media}m")
