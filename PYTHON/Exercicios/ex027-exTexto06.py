# Crie um programa que leia uma frase pelo teclado e mostre:

# Exercício 27 – Primeiro e último nome de uma pessoa

print('====== Exercício 26 – Exercício 27 – Primeiro e último nome de uma pessoa')
nome = str(input('Escreva seu nome completo: ')).strip().capitalize()
recortar = nome.split()
print(' O seu nome completo é {} '.format(nome))
print(' O seu primeiro nome é {}'.format(recortar[0]))
print(' O seu último nome é {}'.format(recortar[-1]))
