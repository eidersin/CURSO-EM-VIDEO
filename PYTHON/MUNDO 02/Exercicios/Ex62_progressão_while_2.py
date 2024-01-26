# Mundo 02: Exercício 61
"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
progressão.
"""
primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termos = int(input('Digite a quantidade de termos da PA: '))
termo = primeiro
contador = 1
total = 0
while termos != 0:
    total += termos
    while contador <= total:
        print(termo, end=' ')
        termo += razao
        contador += 1
    print('\nPAUSE')
    termos = int(input('\nQuantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')