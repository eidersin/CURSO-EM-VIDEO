# Mundo 02: Exercício 64
"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor
999, que é a condição deparada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.
(desconsiderando o flag)
"""

num = 0
soma = 0
num_digitados = 0
print('Digite 999 para parar')
num = int(input('Digite um número inteiro para a soma: '))
while num != 999:
    soma += num
    num = int(input('Digite um número inteiro para a soma: '))
    num_digitados += 1
print('A quantidade de numeros digitados foi {}'.format(num_digitados))
print('A soma entre os valores digitados é {}'.format(soma))
print('Fim do PROGRAMA!')
