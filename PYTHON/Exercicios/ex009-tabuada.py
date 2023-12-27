num = eval(input('Digite um número para ver sua tabuada: '))
print('A tabuada de soma do {} é'.format(num))
for c in range(1, 11):
    print(f'{num} + {c} = {num+c}')
print('-'*34)
print('A tabuada de subtração de {} é'.format(num))
for c in range(1, 11):
    print(f'{num} - {c} = {num-c}')
print('-'*34)
print('A tabuada de multiplicação de {} é'.format(num))
for c in range(1, 11):
    print(f'{num} * {c} = {num*c}')
print('-'*34)
print('A tabuada de divisão de {} é'.format(num))
for c in range(1, 11):
    print('{} / {} = {:.2f}'.format(num, c, num/c))
