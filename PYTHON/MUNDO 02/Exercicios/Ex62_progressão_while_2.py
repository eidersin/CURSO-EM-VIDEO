# Mundo 02: Exercício 61
"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
progressão.
"""
primeiro = int(input('Digite um valor inicial: '))
razao = int(input('Digite um valor para razão: '))
soma = 1
termos = []
total_termos = 10

while True:
    while soma <= total_termos:
        termo_atual = primeiro + (soma - 1) * razao
        termos.append(termo_atual)
        soma += 1
    print("Os termos da PA são:")
    for termo in termos:
        print(termo, end=' ')
    print()
    mais_termos = int(input('Deseja mostrar mais quantos termos? '))
    if mais_termos == 0:
        print('Fim do PROGRAMA.')
        break
    else:
        total_termos += mais_termos
