# 3) Elabore um programa que leia dois números inteiros positivos, sendo o primeiro menor que o segundo(teste
# essa condição no códico), e mostre na tela todos os múltiplos de 5 existentes neste intervalo. Caso a>b, apresente
# a mensagem "Números incorretos para o intervalo proposto!"
num1 = int(input("Digite um numero positivo"))
num2 = int(input("Digite um numero maior q o anterior"))
multiplos = []
while num1 >= num2:
    print("numeros incorretos para o intervalo proposto!")
    num2 = int(input(f"Digite um numero maior que {num1}: "))
i = num1 +1
while i < num2:
    if i % 5 == 0:
        multiplos.append(i)
    i += 1
print("Multiplos de 5:")
for i in multiplos:
    print(i)
