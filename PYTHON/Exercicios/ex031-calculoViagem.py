km = eval(input('Qual a distância da viagem em KM: '))
if km <= 200:
    km = km * 0.50
else:
    km = km * 0.45
print('O valor da passagem vai ser: R${:.2f}'.format(km))
