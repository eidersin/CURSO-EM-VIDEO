# Mundo 02: Exercício 69
"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o uruário quer ou não continuar.
No final mostre:
    A. Quantas pessoas tem mais de 18 anos.
    b. Quantos homens foram cadastrados.
    C. Quantas mulheres tem menos de 20 anos
"""
maior18 = 0
menor18 = 0
quantos_homens = 0
continuar = 'S'
while continuar == 'S':
    print(30 * '-')
    print(5 * ' ', 'CADASTRE UMA PESSOA')
    print(30 * '-')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        quantos_homens += 1
    if sexo == 'F' and idade <= 20:
        menor18 += 1
    print(30 * '-')
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]


print('======= FIM DO PROGRAMA =======')
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todos temos {quantos_homens} homens cadastrados')
print(f'E temos {menor18} mulheres com menos de 18 anos')
