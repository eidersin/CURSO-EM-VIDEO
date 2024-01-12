# Mundo 02: Exercício 60
"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
"""
num = int(input('Digite um numero para calcular seu fatorial: '))
fatorial = 1
while num > 0:
    fatorial = num * fatorial
    num -= 1
print(fatorial)

"""fatorial = 1
for c in range(num, 0, -1):
    fatorial *= c
print(f'O fatorial de {num}! é {fatorial}')"""

