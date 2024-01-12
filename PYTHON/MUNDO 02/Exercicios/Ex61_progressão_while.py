# Mundo 02: Exercício 61
"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
progressão.
"""

primeiro = int(input('Digite um valor inicial: '))
razao = int(input('Digite um valor para razão: '))
soma = 1
termos = []
while soma <= 10:
    termo_atual = primeiro + (soma - 1) * razao
    termos.append(termo_atual)
    soma += 1
print("Os 10 primeiros termos da PA são:")
for termo in termos:
    print(termo, end=' ')
