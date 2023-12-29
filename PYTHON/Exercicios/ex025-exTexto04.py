# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

# Exercício 25 – Procurando uma string dentro de outra

print('====== Exercício 25 – Procurando uma string dentro de outra')
nome = str(input('Digite seu nome completo: ')).strip().lower()
print('Seu nome tem Silva? {}'.format('silva' in nome))
