# 3) Considerando que cada estudante da turma EI22 (31 estudantes) tenham feito 3 avaliações
# de Algoritmos na 2° unidade elabores um programa usando laço de repetição:
# a) Solicite as três notas de cada estudante da turma
# b) Calcule e apresente a média de cada estudante
# c) Para cada estudante, apresente a mensagem Aprovado, caso o estudante tenha obtido a média igual ou superior
# a 6,0, ou Reprovado, caso a média seja inferior a 6,0.

nomes = []
notas = []
i = 0

while i < 2:
    # Considerando que cada nota vale 10, e no final a nota final sera
    # dividida por 3 para obter a media final.
    nome = input(f"Digite o nome do {i + 1} aluno:")
    nomes.append(nome)
    i += 1
i = 0
while i < 2:
    # Considerando que cada nota vale 10, e no final a nota final sera
    # dividida por 3 para obter a media final.
    nota = float(input(f"Digite a nota 1° do {nomes[i]} aluno:"))
    nota2 = float(input(f"Digite a nota 2° do {nomes[i]} aluno:"))
    nota3 = float(input(f"Digite a nota 3° do {nomes[i]} aluno:"))
    notaf = (nota + nota2 + nota3)/3  # nota final
    notas.append(notaf)
    i += 1
cont = 0
for i in notas:
    if i >= 6:
        print(f"média final do {nomes[cont]}: {i} (APROVADO)")
    else:
        print(f"média final do {nomes[cont]}: {i} (REPROVADO)")
    cont += 1
