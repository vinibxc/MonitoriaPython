# 5. Faça um programa que leia nome e altura de 20 alunos. O primeiro valor representa o nome do aluno e o
# segundo representa a sua altura. Encontre o aluno mais alto e o mais baixo. Mostre o nome do aluno mais
# alto e o nome do aluno mais baixo, junto com suas alturas
nomes = []
alturas = []
i = 1
while i <= 2:
    nome = input(f"Digite o nome do {i}° aluno:")
    altura = float(input(f"Digite a altura deste aluno:"))
    nomes.append(nome)
    alturas.append(altura)
    i += 1
ibaixo = 0
ialto = 0
menor = alturas[1]
maior = alturas[1]
i = 0
while i < 2:
    if alturas[i] >= maior:
        maior = alturas[i]
        ialto = i
    if alturas[i] <= menor:
        menor = alturas[i]
        ibaixo = i
    i += 1
print(ibaixo)
print(f"O maior:\n {nomes[ialto]} com {alturas[ialto]} de altura")
print(f"O menor:\n {nomes[ibaixo]} com {alturas[ibaixo]} de altura")