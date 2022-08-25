num1 = int(input("Digite um numero inteiro"))
num2 = int(input("Digite outro numero inteiro"))


if num1 < num2:
    while num1 < num2 -1 :
        num1 = num1 + 1
        print(f"{num1}")
if num2 < num1:
    while num2 < num1 -1:
        num2 = num2 + 1
        print(f"{num2}")