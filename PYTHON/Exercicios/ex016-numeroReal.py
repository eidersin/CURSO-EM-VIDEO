'''from math import trunc
num = float(input('Digite um valor: '))

print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))
print('sendo o resto {:.3f}'.format((num % trunc(num))))'''

num = float(input('Digite um valor: '))
print('O valor digitado foi {} sua parte inteira é {} e seu resto é {:.3f}'.format(num, int(num), num % int(num)))