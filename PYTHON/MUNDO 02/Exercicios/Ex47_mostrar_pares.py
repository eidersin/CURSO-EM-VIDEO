# Mundo 02: Exercício 47
"""
Crie um programa que mostre na tela todos os números pares que estão no intervalo de 0 e 50
"""
soma = 0
for c in range(1, 51):
    if c % 2 == 0:
        soma += c
print(soma)