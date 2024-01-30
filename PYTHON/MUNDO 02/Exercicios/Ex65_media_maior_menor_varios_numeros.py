# Mundo 02: Exercício 65
"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução mostre:
Media entre todos os valores
Maior valor
Menor valor
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
resp = 's'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
media = soma / quant
print('FIM DO PROGRAMA')
print(f'A quantidade de valores digitados foi {quant}')
print(f'A soma dos valores digitados foi {soma}')
print(f'A média dos valores é {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')