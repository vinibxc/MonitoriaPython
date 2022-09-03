# Suponha que o  diretor de uma escola queira presentear o funcionário mais antigo da instituição. Para
# isso, elabore um programa que:
# a) Solicite a quantidade de funcionários da escola;
# b) Com uso do laço de repetição, leia a idade e o tempo de serviço de cada funcionário;
# c) Calcule e apresente a idade média dos funcionários;
# d) Mostre a idade do funcionário mais velho;
# e) Apresente o tempo de serviço ddo funcionário mais antigo e o ano em que ele começou a trabalhar na escola.
# (Considere o ano atual = 2022)
funcionarios = [] # nome dos funcionarios
tempo = [] # tempo de trabalho
idade = [] # idade do funcionario
somaI = 0 #soma das idades
loop = True
while loop:
    nome = input("Digite o nome do funcionario ou deixe em branco para encerrar. ")
    if nome == "":
        loop = False
    else:
        funcionarios.append(nome)
tamanho = len(funcionarios)
i = 0
while i < tamanho:
    temp = int(input(f"Digite o tempo de trabalho em anos do funcionario{funcionarios[i]}"))
    tempo.append(temp)
    ida = int(input(f"Digite a idade do funcionario{funcionarios[i]}"))
    somaI += idade
    idade.append(ida)
    i += 1
media = somaI / tamanho
Mvelho = max(idade) # mais velho
antigo = max(tempo) # funcionario mais antigo
ano = 2022 - antigo
print(f"idade media dos funcionarios: {media}")
print(f"Idade do funcionario mais velho: {Mvelho}")
print(f"Tempo de serviço do mais antigo: {antigo}\nEntrou no ano de: {ano}")