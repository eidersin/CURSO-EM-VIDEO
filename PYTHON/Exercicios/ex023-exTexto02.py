
# Exercício 23 – Separando dígitos de um número

print('====== Exercício 23 – Separando dígitos de um número')
# ano = input('Escreva um número de 0 a 9999: ')
# print('O número digitado foi {}.'.format(ano))
# print('Unidade: {}'.format(ano[3]))
# print('Dezena: {}'.format(ano[2]))
# print('Centena: {}'.format(ano[1]))
# print('Milhar: {}'.format(ano[0]))

ano = int(input('Escreva um número de 0 a 9999: '))
u = ano // 1 % 10
d = ano // 10 % 10
c = ano // 100 % 10
m = ano // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
