#5.O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um
#conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas,
#bem como a média das temperaturas. A temperatura 999 representa a saída do laço de repetição.
conjuntoTemp = []
temperatura = 0
soma = 0
cont = 0
condicional = 0
while condicional != 999:
    temperatura = float(input("Digite o valor da temperatura em Graus Celsius(ou 999 para encerrar):"))
    if temperatura != 999:
        soma  = soma + temperatura
        cont = cont + 1
        conjuntoTemp.append(temperatura)
    else:
        condicional = temperatura
maiorTemp = conjuntoTemp[1]
menorTemp = conjuntoTemp[1]
for temp in conjuntoTemp:
    if temp < menorTemp:
        menorTemp = temp
    if temp > maiorTemp and temp != 999:
        maiorTemp = temp
media = soma / cont

print(f"Menor temperatura: {menorTemp}\nMaior temperatura: {maiorTemp}\nMedia: {media}")
