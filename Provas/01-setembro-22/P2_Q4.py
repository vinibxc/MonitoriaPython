# 4) O ano 2022 é um ano eleitora. Suponha que na ciadade de Eunápolis existam 4 candidatos
# para deputado estadual. Faça um programa que peça o número total de eleitores.
# Em seguida, seu programa deve solicitar que cada eleitor vote. Considere que todos os votos
# seja válidos. Ao final mostre o percentual de votos de cada cnadidato
eleitores = int(input("Digite o número total de eleitores:"))
i = 1
print("-------------------------------------CANDIDATOS---------------------------------")
print("1° candidata Lucinha do MST, Número 13100")

print("----------------------------------------------------------------------")
print("2° candidato Fulado de lá, Número 22100")

print("----------------------------------------------------------------------")
print("3° candidato Sicrano de cá, Número 11100")

print("----------------------------------------------------------------------")
print("4° candidato Beltrano, Número 12100")

lucinha = 0
fulano = 0
sicrano = 0
beltranho = 0
while i <= eleitores:
    voto = int(input("Digite seu voto: "))
    if voto == 13100:
        lucinha +=1
    if voto == 22100:
        fulano +=1
    if voto == 11100:
        sicrano +=1
    if voto == 12100:
        beltranho += 1
    i += 1
percentualL = (lucinha*100)/eleitores
percentualF = (fulano*100)/eleitores
percentualS = (sicrano*100)/eleitores
percentualB = (beltranho*100)/eleitores

print(f"Lucinha: {percentualL}%")
print(f"fulano: {percentualF}%")
print(f"Sicrano: {percentualS}%")
print(f"Beltrano: {percentualB}%")