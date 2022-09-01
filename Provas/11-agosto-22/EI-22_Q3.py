# 3. Faça um programa que receba 4 números inteiros (informados pelo usuário) e apresente uma mensagem
# informando se são ou não múltiplos de 10.
numero= []
i = 0
while  i < 4:
    num = int(input("Digite um numero inteiro"))
    numero.append(num)
    i += 1

i = 0
while  i < 4:
    if numero[i] % 10 == 0:
        print(f"{i+1}°)O numero {numero[i]} é multiplo de 10")
    else:
        print(f"{i+1}°)O numero {numero[i]} não é multiplo de 10")
    i += 1