# Mundo 02: Exercício 49
"""
Desenvolva um programa que leia seis número inteiro e mostre a soma apenas daqueles que forem pares.
Se o valor digitador for impar, desconsidere-o.
"""
num = 0
for i in range(1, 7):
    valor = int(input(f"Digite o {i}º número inteiro: "))
    if valor % 2 == 0:
        num += valor
print('A soma dos pares digitados é: {}'.format(num))
