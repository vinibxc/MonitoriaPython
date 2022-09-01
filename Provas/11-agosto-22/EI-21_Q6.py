# 6. Em uma competição de salto em distância o atleta tem direito a cinco saltos. No final da série de saltos
# do atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores
# restantes. Você deve fazer um programa que leia do usuário o nome e as cinco distâncias alcançadas pelo
# atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar
# o melhor e o pior salto e depois calcular a média). Os saltos são informados na ordem da execução,
# portanto não são ordenados. A saída do programa deve ser conforme o exemplo abaixo:
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
