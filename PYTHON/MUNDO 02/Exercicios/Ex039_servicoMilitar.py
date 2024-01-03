# Mundo 02: Exercício 39
"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date

ano = int(input('Qual seu ano de nascimento? '))
atual = date.today().year
idade = atual - ano
falta = 18 - idade
passou = idade - 18
if idade < 17:
    print('Falta {} anos para você se alistar!'.format(falta))
elif idade == 17:
    print('Você deve se alistar no próximo ano!')
elif idade == 18:
    print('Você deve se alistar nesse ano!')
elif idade == 19:
    print('Já passou um ano do prazo para se alistar!')
else:
    print('Ja passou {} anos do prazo para se alistar!'.format(passou))
