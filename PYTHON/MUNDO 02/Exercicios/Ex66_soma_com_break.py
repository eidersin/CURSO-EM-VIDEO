# Mundo 02: Exercício 66
"""
Crie um programa que leia vários numeros inteiros pelo teclado. O programa só vai parar quando ousuário digitar o valor
999, que é a condição de parada. Nofinal mostre quantos números foram digitados e qual foi a soma entre eles.
"""
resp = soma = cont = n = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    cont += 1
    soma += n

print(f'Foram digitados {cont} numeros e a soma entre eles é {soma}')