# Mundo 02: Exercício 61
"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
progressão.
"""

primeiro = int(input('Digite um valor inicial: '))
razao = int(input('Digite um valor para razão: '))
cont = 1
termos = primeiro
while cont <= 10:
    print(termos, end=' ')
    termos += razao
    cont += 1
print('FIM')