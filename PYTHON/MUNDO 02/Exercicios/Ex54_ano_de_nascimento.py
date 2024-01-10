# Mundo 02: Exercício 54
"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores.
"""
from datetime import date
menor_idade = 0
maior_idade = 0
for nascimento in range(1, 8):
    ano_nascimento = int(input(f'Qual o ano de nascimento da {nascimento}º pessoa nasceu?: '))
    idade = date.today().year - ano_nascimento
    if idade < 21:
        menor_idade += 1
    else:
        maior_idade += 1
print(f'Ao todo tivemos {menor_idade} pessoas menores de 21 Anos')
print(f'Ao todo tivemos {maior_idade} pessoas maiores de 21 Anos')
