num = int(input('Digite um número: '))
total = 0
primo = 0
nPrimo = 0
for item in range(1,num+1):
    if num % item == 0:
        total += 1
        print(f'Número {num} e total divisão {total}')
if total == 2:
    print('É PRIMO')
    primo += 1
else:
    print('NÃO É PRIMO')
    nPrimo += 1
