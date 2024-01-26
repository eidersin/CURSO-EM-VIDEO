# Mundo 02: Exercício 63
"""
Escreva um programa que leia um número n inteiro e mostre na tela os n primeiro elementos de uma sequencia de fibonacci
"""


num = int(input('Digite um número de termos para sequência de Fibonacci: '))
a, b = 0, 1
contador = 0
while contador < num:
    print(a, end=' ')
    a, b = b, a + b
    contador += 1