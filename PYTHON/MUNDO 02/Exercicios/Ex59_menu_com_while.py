# Mundo 02: Exercício 59
"""
Crie um programa que leia dois valores e mostre um menu na tela:
"""
from time import sleep
num1 = int(input('Digite primeiro valor: '))
num2 = int(input('Digite segundo valor: '))
escolha_opcao = ()
while escolha_opcao != 5:
    print(f'\033[0mO primeiro valor digitado foi {num1} e o segundo valor foi {num2}')
    print('[1] Somar  [2] Multiplicar  [3] Maior  [4] Novos números  [5] Sair do programa')
    escolha_opcao = int(input('Escolha uma opção do MENU:'))
    if escolha_opcao == 1:
        soma = num1 + num2
        print('-=-' * 20)
        print(f'\033[92m{num1} + {num2} = {soma}')
        print('\033[0m-=-' * 20)
    if escolha_opcao == 2:
        multiplicacao = num1 * num2
        print('-=-' * 20)
        print(f'\033[92mResultado: {num1} x {num2} = {multiplicacao}')
        print('\033[0m-=-' * 20)
    if escolha_opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('-=-' * 20)
        print('\033[92mO maior valor digitado foi {}'.format(maior))
        print('\033[0m-=-' * 20)
    if escolha_opcao == 4:
        num1 = int(input('Digite primeiro valor: '))
        num2 = int(input('Digite segundo valor: '))
    if escolha_opcao > 5:
        print('\033[91mOpção inválida. Tente novamente.')
    sleep(1)
print('\033[92mFim do programa')
