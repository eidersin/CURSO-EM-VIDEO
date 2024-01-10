# Mundo 02: Exercício 51
"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
progressão.
"""
soma = 0
primeiro = int(input('Digite um valor inicial: '))
razao = int(input('Digite um valor para razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print((c), end=' ')
