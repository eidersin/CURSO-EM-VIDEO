# Mundo 02: Exercício 47
"""
Crie um programa que mostre na tela todos os números pares que estão no intervalo de 0 e 50
"""
# 2º EXEMPLO
for c in range(1, 51):
    if c % 2 == 0:
        print(f'{c}', end=' ')
print('\n')
# 1º EXEMPLO
for c in range(2, 51, 2):
    print(f'{c}', end=' ')