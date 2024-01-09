# Mundo 02: Exercício 51
"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
progressão.
"""
soma = 0
i = int(input('Digite um valor inicial: '))
r = int(input('Digite um valor para razão: '))
f = i + r * 10
for c in range(i, f, r):
    print((c), end= ' ')