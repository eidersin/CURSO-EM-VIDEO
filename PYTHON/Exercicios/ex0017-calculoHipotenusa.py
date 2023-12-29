from math import hypot

co = float(input('Entre com o valor do cateto oposto: '))
ca = float(input('Entre com o valor do cateto adjacente: '))

# hipot = (co ** 2 + ca ** 2) ** (1 / 2)

# print('A hipotenusa vai medir {:.2f}'.format(hipot))
print('A hipotenusa vai medir {:.2f}'.format(hypot(co, ca)))
