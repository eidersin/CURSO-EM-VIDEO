# Mundo 02: Exercício 54
"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores.
"""
from datetime import date
soma_maior = 0
soma_menor = 0
for i in range(1, 8):
    ano = date.today().year
    nascimento = int(input(f'Digite o {i}º ano de nascimento: '))
    idade = ano - nascimento
    if idade >= 21:
        soma_maior += 1
    else:
        soma_menor += 1
print(f'Ao todo tivemos {soma_maior} pessoas maiores')
print(f'Ao todo tivemos {soma_menor} pessoas menores')