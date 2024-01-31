# Mundo 02: Exercício 70
"""
Crie um programa que leia  o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
    A. Qual é o total gasto
    b. Quantos produtos custam mais de R$1000.00
    C. Qual o nome do produto mais barato.
"""
soma = 0
maior = 0
menor = ''
menor_preco = float('inf')
print(40*'-')
print('{:^40}'.format('LOJA SUPER BARATÃO'))
print(40*'-')
continuar = 'S'
while continuar == 'S':
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    if preco >= 1000:
        maior += 1
    if preco < menor_preco:
        menor = nome
        menor_preco = preco
    soma += preco
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compro foi de R${soma:.2f}')
print(f'Temos {maior} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {menor} e custa R${menor_preco:.2f}')

"""soma = 0
maior = 0
menor = ''
menor_preco = float('inf')  # Inicializa com um valor muito alto
print(40*'-')
print('{:^40}'.format('LOJA SUPER BARATÃO'))
print(40*'-')
continuar = 'S'
while continuar == 'S':
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    if preco >= 1000:
        maior += 1
    if preco < menor_preco:  # Se o preço for menor que o menor preço atual
        menor = nome  # Atualiza o nome do produto mais barato
        menor_preco = preco  # Atualiza o menor preço
    soma += preco
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi de R${soma:.2f}')
print(f'Temos {maior} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {menor} e custa R${menor_preco:.2f}')"""