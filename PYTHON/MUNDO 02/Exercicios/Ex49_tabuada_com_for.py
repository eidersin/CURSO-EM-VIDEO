# Mundo 02: Exercício 49
"""
Faça um programa que calcule  a soma de um número que o usuário escolher, só que agora utilizando um laço for
"""
num = eval(input('Digite um número para ver sua tabuada: '))
print('A tabuada de soma do {} é'.format(num))
for valor in range(1, 11):
    print(f'{num} + {valor} = {num+valor}')