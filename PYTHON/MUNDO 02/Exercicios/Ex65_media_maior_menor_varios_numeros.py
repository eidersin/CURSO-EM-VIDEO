# Mundo 02: Exercício 65
"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução mostre:
Media entre todos os valores
Maior valor
Menor valor
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
# media = 0
# maior = float('-inf')
# menor = float('inf')
# num = 0
# soma = 0
# num_digitados = 0
# print('Digite 999 para parar')
# num = float(input('Digite um número inteiro para a soma: '))
# while True:
#     while num != 999:
#         soma += num
#         num = float(input('Digite um número inteiro para a soma: '))
#         if num != 999:
#             if num > maior:
#                 maior = num
#             if num < menor:
#                 menor = num
#         num_digitados += 1
#
#     continuar = str(input('Deseja mostrar mais números? ')).strip().upper()[0]
#     if continuar == 'S':
#         while num != 999:
#             soma += num
#             num = float(input('Digite um número inteiro para a soma: '))
#     else:
#         break
# media = soma / num_digitados
# print('A média entre os valores digitados foi {}'.format(media))
# print('O maior valor digitado foi {}'.format(maior))
# print('O menor valor digitado foi {}'.format(menor))
#
# print('\nFim do PROGRAMA.')

media = 0
maior = float('-inf')
menor = float('inf')
num = 0
soma = 0
num_digitados = 0
print('Digite 999 para parar')
num = float(input('Digite um número inteiro para a soma: '))
while num != 999:
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    num_digitados += 1
    num = float(input('Digite um número inteiro para a soma: '))
while True:
    continuar = str(input('Deseja mostrar mais números? ')).strip().upper()[0]
    if continuar == 'S':
        num = float(input('Digite um número inteiro para a soma: '))
        while num != 999:
            soma += num
            if num > maior:
                maior = num
            if num < menor:
                menor = num
            num_digitados += 1
            num = float(input('Digite um número inteiro para a soma: '))
    else:
        break
if num_digitados != 0:
    media = soma / num_digitados
print('A média entre os valores digitados foi {}'.format(media))
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))

print('\nFim do PROGRAMA.')
