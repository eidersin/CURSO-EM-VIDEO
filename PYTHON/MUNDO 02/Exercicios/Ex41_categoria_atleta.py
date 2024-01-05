# Mundo 02: Exercício 41
"""
A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categirua, de acordo com a idade:
 - Até 9 anos: MIRIM
 - Até 14 anos: INFANTIL
 - Até: 19 anos: JUNIOR
 - Até: 20 anos: SENIOR
 - Acima: MASTER
"""
from datetime import date

ano = int(input('Qual o ano de nascimento do atleta? '))
atual = 2017
idade = atual - ano
print(f'O atleta tem {idade} anos de idade.')
if idade <= 9:
    print('A sua categoria é: MIRIM')
elif idade <= 14:
    print('A sua categoria é: INFANTIL')
elif idade <= 19:
    print('A sua categoria é: JUNIOR')
elif idade <= 25:
    print('A sua categoria é: SÊNIOR')
else:
    print('A sua categoria é: MASTER')
