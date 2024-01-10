# Mundo 02: Exercício 48
"""
Faça um programa que calcule  a soma entre todos os números impares que são multiplos de três e que se encontram no
intervalo de 1 até 500:
"""
# EXEMPLO 01
soma = 0
cont = 0
for numero in range(0, 501, 3):
    if numero % 2 != 0:
        cont += 1
        soma += numero
print('A soma dos {} números ímpares múltiplos de 3 no intervalo de 1 a 500 é: {}'.format(cont, soma))

# EXEMPLO 02
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma dos {} números ímpares múltiplos de 3 no intervalo de 1 a 500 é: {}'.format(cont, soma))
