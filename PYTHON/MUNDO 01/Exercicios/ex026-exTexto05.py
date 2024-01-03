# Crie um programa que leia uma frase pelo teclado e mostre:

# Exercício 26 – Primeira e última ocorrência de uma string

print('====== Exercício 26 – Primeira e última ocorrência de uma string')
frase = str(input('Digite uma frase: ')).strip().upper()
print('A frase digitada foi: {}'.format(frase))
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A aparece na {} '.format(frase.find('A')+1))
print('A ultima letra A aparece na {} '.format(frase.rfind('A')+1))
