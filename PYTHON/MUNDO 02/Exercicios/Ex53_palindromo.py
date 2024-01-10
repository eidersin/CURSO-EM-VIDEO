# Mundo 02: Exercício 53
"""
Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
"""
frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
reverso = junto[::-1]
if junto == reverso:
    print('A frase {} digitada é um palindromo'.format(frase))
    print('O reverso da palavra {} é {}'.format(junto, reverso))
else:
    print('A frase {} digitada NÃO é um palindromo'.format(frase))
    print('O reverso da palavra {} é {}'.format(junto, reverso))