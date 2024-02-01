# Mundo 02: Exercício 67
"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo:
"""

while True:
    numero = int(input('Digite um valor para ver sua tabuada: '))
    if numero <= 0:
        break
    print(40 * '-')
    for c in range(1, 11):
        soma = numero * c
        print(f'{numero} x {c} = {soma} ')
    print(40 * '-')
print(40 * '-')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')