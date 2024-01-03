# Mundo 02: Exercício 36
"""
Escreva um programa que leia um número inteiro qualquer e mostre e peça para o usuário escolher qual será a
base de conversão
"""
num = int(input('Qual o número que deseja converter? '))
print(' 1 - para Binário\n 2 - para Octal\n 3 - para Hexadecimal\n 4 - para Todos ')
base = int(input('Para qual base deseja converter? '))
binario = bin(num)
octal = oct(num)
hexad = hex(num)
if base == 1:
    print('O número {} convertido para a base de binário é: {}'.format(num, binario))
elif base == 2:
    print('O número {} convertido para a base de octal é: {}'.format(num, octal))
elif base == 3:
    print('O número {} convertido para a base de hexadecimal é: {}'.format(num, hexad))
elif base == 4:
    print('O número {} convertido para a base de binário é: {}'.format(num, binario))
    print('O número {} convertido para a base de octal é: {}'.format(num, octal))
    print('O número {} convertido para a base de hexadecimal é: {}'.format(num, hexad))
