# Mundo 02: Exercício 57
"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
peça  a digitação novamente até ter um valor correto.
"""
sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
while 'F' != sexo != 'M':
    print('VALOR INCORRETO')
    sexo = str(input('Digite o sexo novamente [M/F]: ')).strip().upper()[0]
print('VALOR CORRETO')