# Mundo 02: Exercício 71
"""
Crie um programa que simule o funcionamento de um caixa eletronico. No início, pergunte ao usuário qual será o
valor a ser sacado, (numero inteiro) e o programa vai informar quantas cédulas de ccada valor serão entregues:
OBS> Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.0
"""
print(40*'=')
print('{:^40}'.format('BANCO CEV'))
print(40*'=')
valor = int(input('Qual o valor a ser sacado: R$'))
sobra = valor

cedula_50 = sobra // 50
sobra %= 50
cedula_20 = sobra // 20
sobra %= 20
cedula_10 = sobra // 10
sobra %= 10
cedula_1 = sobra // 1
sobra %= 1

if cedula_50 > 0 :
    print(f'Total de {cedula_50:.0f} cédulas de R$50')
if cedula_20 > 0:
    print(f'Total de {cedula_20:.0f} cédulas de R$20')
if cedula_10 > 0:
    print(f'Total de {cedula_10:.0f} cédulas de R$10')
if cedula_1 > 0:
    print(f'Total de {cedula_1:.0f} cédulas de R$1')
print(40*'=')
print('Volte sempre ao BANCO DO CEV! Tenha um bom dia!')
